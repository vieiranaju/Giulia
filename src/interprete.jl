using JSON

"""
A Tabela de Símbolos. Em vez de guardar ponteiros (AllocaInst),
vamos guardar os VALORES atuais das variáveis.
É um simples Dicionário.
"""
const tabela_de_simbolos = Dict{String, Any}()
const tabela_de_tipos = Dict{String, String}()
const tabela_de_inicializacao = Dict{String, Bool}()

"""
Função recursiva que CALCULA o valor de uma expressão.
É o equivalente ao seu `fator/termo/expr` do C++.
"""
function avaliar_expressao(expr_json)
    
    # Caso 1: A expressão é um número literal
    if isa(expr_json, Number)
        return expr_json
    end

    # Se for um dict JSON/Object com tipo explícito (String/Char/ArrayAccess/BinaryOp...)
    if isa(expr_json, AbstractDict)
        t = get(expr_json, "type", nothing)
        if t == "String"
            return expr_json["value"]
        elseif t == "Char"
            return expr_json["value"]
        elseif t == "ArrayAccess"
            # avalia array e índice; o campo "array" pode ser String (nome) ou um outro node
            arr_node = expr_json["array"]
            idx = avaliar_expressao(expr_json["index"])
            # recupera array do símbolo
            arr_ref = isa(arr_node, String) ? (haskey(tabela_de_simbolos, arr_node) ? tabela_de_simbolos[arr_node] : throw(ErrorException("Variável não declarada: $arr_node"))) : avaliar_expressao(arr_node)
            if !(arr_ref isa AbstractVector)
                error("Tentativa de indexar algo que não é array: $arr_node")
            end
            # índice deve ser inteiro
            if !(isa(idx, Number))
                error("Índice de array não é numérico: $idx")
            end
            i = Int(idx)
            if i < 0 || i+1 > length(arr_ref)
                error("Índice fora do limite: $i")
            end
            return arr_ref[i+1]
        end
    end

    # Caso 2: A expressão é o nome de uma variável (identificador simples)
    if isa(expr_json, String)
        name = expr_json
        if haskey(tabela_de_simbolos, name)
            val = tabela_de_simbolos[name]
            # verificação de inicialização
            if haskey(tabela_de_inicializacao, name) && tabela_de_inicializacao[name] == false
                error("Variável usada antes de inicialização: $name")
            end
            return val
        else
            error("Variável não declarada: $name")
        end
    end

    # Caso 3: A expressão é uma Operação Binária (BinaryOp)
    # JSON.parsefile retorna objetos do tipo JSON.Object (que é um AbstractDict). Usamos AbstractDict para ser mais genérico.
    if isa(expr_json, AbstractDict) && get(expr_json, "type", nothing) == "BinaryOp"
        op = expr_json["op"]
        
        # Recursivamente CALCULA os lados esquerdo e direito
        left_val = avaliar_expressao(expr_json["left"])
        right_val = avaliar_expressao(expr_json["right"])

        # Executa a operação matemática ou relacional IMEDIATAMENTE
        if op == "+"
            return left_val + right_val
        elseif op == "-"
            return left_val - right_val
        elseif op == "*"
            return left_val * right_val
        elseif op == "/"
            return left_val / right_val
        elseif op == "%"
            return left_val % right_val
        elseif op == "<"
            return left_val < right_val
        elseif op == ">"
            return left_val > right_val
        elseif op == "<="
            return left_val <= right_val
        elseif op == ">="
            return left_val >= right_val
        elseif op == "=="
            return left_val == right_val
        elseif op == "!="
            return left_val != right_val
        elseif op == "&&"
            return left_val && right_val
        elseif op == "||"
            return left_val || right_val
        else
            error("Operador binário desconhecido: $op")
        end
    end
    
    error("Estrutura de expressão não reconhecida: $expr_json")
end

"""
Função auxiliar que executa uma lista de statements e propaga retornos.
Retorna `nothing` se nenhum 'Return' foi encontrado, ou o valor retornado.
"""
function executar_statements(statements)
    for stmt in statements
        resultado = executar_statement(stmt)
        # Se encontrar um Return, propaga o valor imediatamente
        if !isnothing(resultado)
            return resultado
        end
    end
    return nothing
end

"""
Função que executa UM statement individual.
Retorna `nothing` se não for um Return, ou o valor retornado caso seja.
"""
function executar_statement(stmt)
    stmt_type = get(stmt, "type", nothing)
    
    if stmt_type == "Declaration"
        # Declaração de variável (ex: int a = 5)
        var_name = stmt["name"]
        # Guarda o tipo declarado (se fornecido)
        if haskey(stmt, "varType") && !isnothing(stmt["varType"])
            tabela_de_tipos[var_name] = stmt["varType"]
        end

        # Arrays
        if get(stmt, "isArray", false)
            size = get(stmt, "size", nothing)
            if !isnothing(size) && isa(size, Int)
                # Inicializa com 0 ao invés de nothing para permitir atribuição direta
                tabela_de_simbolos[var_name] = zeros(Int, size)
            else
                tabela_de_simbolos[var_name] = Any[]
            end
            tabela_de_inicializacao[var_name] = false
            # Se houve inicializadores (lista), converte e preenche
            if !isnothing(get(stmt, "value", nothing))
                vals = stmt["value"]
                if isa(vals, Array)
                    arr = tabela_de_simbolos[var_name]
                    for i = 1:min(length(arr), length(vals))
                        arr[i] = avaliar_expressao(vals[i])
                    end
                    tabela_de_inicializacao[var_name] = true
                end
            end

        else
            if !isnothing(get(stmt, "value", nothing))
                valor = avaliar_expressao(stmt["value"])
                tabela_de_simbolos[var_name] = valor
                tabela_de_inicializacao[var_name] = true
                println("   (Atribuindo $var_name = $valor)")
            else
                # Declaração sem inicialização (ex: int a;)
                tabela_de_simbolos[var_name] = nothing
                tabela_de_inicializacao[var_name] = false
            end
        end
        
    elseif stmt_type == "Assignment"
        # Atribuição (ex: a = 10)
        target = stmt["name"]
        valor = avaliar_expressao(stmt["value"])

        # Se target é um acesso a array
        if isa(target, AbstractDict) && get(target, "type", nothing) == "ArrayAccess"
            # Avalia referência de array (pode ser nome ou expressão)
            arr_node = target["array"]
            arr_ref = isa(arr_node, String) ? (haskey(tabela_de_simbolos, arr_node) ? tabela_de_simbolos[arr_node] : throw(ErrorException("Variável não declarada: $arr_node"))) : avaliar_expressao(arr_node)
            idx = avaliar_expressao(target["index"])
            i = Int(idx)
            if !(arr_ref isa AbstractVector)
                error("Tentativa de indexar algo que não é array: $arr_node")
            end
            if i < 0 || i+1 > length(arr_ref)
                error("Índice fora do limite: $i")
            end
            arr_ref[i+1] = valor
            println("   (Atribuindo elemento de array $arr_node[$i] = $valor)")
            # marca inicialização da variável (array) como verdadeira
            if isa(arr_node, String)
                tabela_de_inicializacao[arr_node] = true
            end

        else
            # Nome simples
            var_name = target
            tabela_de_simbolos[var_name] = valor
            tabela_de_inicializacao[var_name] = true
            println("   (Atribuindo $var_name = $valor)")
        end
        
    elseif stmt_type == "If"
        # Estrutura if (sem else)
        condicao = avaliar_expressao(stmt["condition"])
        println("   (If: condição = $condicao)")
        
        if condicao
            resultado = executar_statements(stmt["thenBody"])
            if !isnothing(resultado)
                return resultado
            end
        end
        
    elseif stmt_type == "IfElse"
        # Estrutura if...else
        condicao = avaliar_expressao(stmt["condition"])
        println("   (IfElse: condição = $condicao)")
        
        if condicao
            resultado = executar_statements(stmt["thenBody"])
            if !isnothing(resultado)
                return resultado
            end
        else
            resultado = executar_statements(stmt["elseBody"])
            if !isnothing(resultado)
                return resultado
            end
        end
        
    elseif stmt_type == "While"
        # Laço while
        println("   (Entrando no While)")
        iteracao = 0
        while avaliar_expressao(stmt["condition"])
            iteracao += 1
            println("      [While iteração $iteracao]")
            resultado = executar_statements(stmt["body"])
            if !isnothing(resultado)
                return resultado
            end
        end
        println("   (Saindo do While após $iteracao iterações)")
        
    elseif stmt_type == "DoWhile"
        # Laço do...while
        println("   (Entrando no DoWhile)")
        iteracao = 0
        while true
            iteracao += 1
            println("      [DoWhile iteração $iteracao]")
            resultado = executar_statements(stmt["body"])
            if !isnothing(resultado)
                return resultado
            end
            
            # Testa condição após executar o corpo
            if !avaliar_expressao(stmt["condition"])
                break
            end
        end
        println("   (Saindo do DoWhile após $iteracao iterações)")
        
    elseif stmt_type == "For"
        # Laço for (init; condition; increment)
        println("   (Entrando no For)")
        
        # Inicialização (pode ser Declaration ou Assignment)
        if !isnothing(get(stmt, "init", nothing))
            executar_statement(stmt["init"])
        end
        
        iteracao = 0
        # Laço principal
        while isnothing(get(stmt, "condition", nothing)) || avaliar_expressao(stmt["condition"])
            iteracao += 1
            println("      [For iteração $iteracao]")
            
            resultado = executar_statements(stmt["body"])
            if !isnothing(resultado)
                return resultado
            end
            
            # Incremento: pode ser um Assignment ou BinaryOp
            if !isnothing(get(stmt, "increment", nothing))
                incr = stmt["increment"]
                if isa(incr, AbstractDict)
                    if get(incr, "type", nothing) == "Assignment"
                        # É um Assignment já estruturado
                        var_name = incr["name"]
                        novo_valor = avaliar_expressao(incr["value"])
                        tabela_de_simbolos[var_name] = novo_valor
                    elseif get(incr, "type", nothing) == "BinaryOp"
                        # É um BinaryOp, atualiza a variável (assume que left é o nome)
                        var_name = incr["left"]
                        novo_valor = avaliar_expressao(incr)
                        tabela_de_simbolos[var_name] = novo_valor
                    else
                        # Outro tipo, apenas avalia
                        avaliar_expressao(incr)
                    end
                else
                    avaliar_expressao(incr)
                end
            end
        end
        println("   (Saindo do For após $iteracao iterações)")
        
    elseif stmt_type == "Switch"
        # Switch com casos e default
        println("   (Entrando no Switch)")
        valor_switch = avaliar_expressao(stmt["value"])
        println("      (Valor do switch: $valor_switch)")
        
        encontrou_caso = false
        executar_restante = false  # Para simular fall-through
        
        for caso in stmt["cases"]
            if caso["type"] == "Case"
                valor_case = avaliar_expressao(caso["value"])
                
                if valor_switch == valor_case || executar_restante
                    println("      (Executando case $valor_case)")
                    encontrou_caso = true
                    executar_restante = true
                    
                    resultado = executar_statements(caso["body"])
                    if !isnothing(resultado)
                        return resultado
                    end
                    
                    # Se houver break, para a execução
                    if get(caso, "hasBreak", false)
                        executar_restante = false
                        break
                    end
                end
                
            elseif caso["type"] == "Default"
                if !encontrou_caso
                    println("      (Executando default)")
                    resultado = executar_statements(caso["body"])
                    if !isnothing(resultado)
                        return resultado
                    end
                end
            end
        end
        println("   (Saindo do Switch)")
        
    elseif stmt_type == "Return"
        # Instrução de retorno (ex: return b - 1)
        
        # Calcula o valor da expressão de retorno
        valor_retorno = avaliar_expressao(stmt["value"])
        
        println("   (Return: $valor_retorno)")
        # Retorna o valor final da função
        return valor_retorno
        
    else
        @warn "Instrução não implementada: $stmt_type"
    end
    
    return nothing
end

"""
Função que "executa" uma função do seu código.
Ela processa as declarações e retornos.
"""
function executar_funcao(func_json::AbstractDict)
    # Pega o corpo da função (a lista de instruções)
    body_json = func_json["body"]
    
    resultado = executar_statements(body_json)
    
    if !isnothing(resultado)
        println("Função terminou com sucesso.")
        return resultado
    else
        # Se a função terminar sem um 'return' (como em C)
        println("Função terminou (sem retorno explícito).")
        return 0
    end
end

# Função principal que controla todo o processo.
function main()
    if length(ARGS) != 1
        println("Uso: julia interprete.jl <arquivo_json_simplificado>")
        return
    end
    json_path = ARGS[1]

    println("Iniciando Interpretador...")

    local ast
    try
        ast = JSON.parsefile(json_path)
    catch e
        println("ERRO ao ler ou processar o arquivo JSON '$json_path':")
        println(e)
        return
    end
    
    # Encontra a função 'main' no JSON
    # (Assumindo que é a primeira e única função, por enquanto)
    main_func_json = ast[1]
    
    if main_func_json["name"] == "main"
        println("Executando função 'main'...")
        try
            # Executa a função e pega o resultado
            resultado_final = executar_funcao(main_func_json)
            
            println("======================================")
            println("Resultado Final da Execução: $resultado_final")
            println("======================================")
        catch e
            println("\nERRO DURANTE A EXECUÇÃO:")
            println(e)
        end
    else
        println("Não foi encontrada a função 'main' no arquivo JSON.")
    end
end

main()