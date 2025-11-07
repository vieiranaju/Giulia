using JSON

"""
A Tabela de Símbolos. Em vez de guardar ponteiros (AllocaInst),
vamos guardar os VALORES atuais das variáveis.
É um simples Dicionário.
"""
const tabela_de_simbolos = Dict{String, Any}()

"""
Função recursiva que CALCULA o valor de uma expressão.
É o equivalente ao seu `fator/termo/expr` do C++.
"""
function avaliar_expressao(expr_json)
    
    # Caso 1: A expressão é um número literal 
    if isa(expr_json, Number)
        return expr_json
    end
    
    # Caso 2: A expressão é o nome de uma variável
    if isa(expr_json, String)
        if haskey(tabela_de_simbolos, expr_json)
            # Retorna o VALOR atual da variável da tabela
            return tabela_de_simbolos[expr_json]
        else
            error("Variável não declarada: $expr_json")
        end
    end

    # Caso 3: A expressão é uma Operação Binária (BinaryOp)
    if isa(expr_json, Dict) && haskey(expr_json, "type") && expr_json["type"] == "BinaryOp"
        op = expr_json["op"]
        
        # Recursivamente CALCULA os lados esquerdo e direito
        left_val = avaliar_expressao(expr_json["left"])
        right_val = avaliar_expressao(expr_json["right"])

        # Executa a operação matemática IMEDIATAMENTE
        if op == "+"
            return left_val + right_val
        elseif op == "-"
            return left_val - right_val
        elseif op == "*"
            return left_val * right_val
        elseif op == "/"
            return left_val / right_val
        else
            error("Operador binário desconhecido: $op")
        end
    end
    
    error("Estrutura de expressão não reconhecida: $expr_json")
end

"""
Função que "executa" uma função do seu código.
Ela processa as declarações e retornos.
"""
function executar_funcao(func_json::Dict)
    # Pega o corpo da função (a lista de instruções)
    body_json = func_json["body"]

    for stmt in body_json
        stmt_type = stmt["type"]
        
        if stmt_type == "Declaration"
            # Declaração de variável (ex: int a = 5)
            var_name = stmt["name"]
            
            if !isnothing(stmt["value"])
                # Se a variável tem um valor (ex: a = 5 ou b = a + 10)
                # Nós calculamos esse valor
                valor = avaliar_expressao(stmt["value"])
                
                # E o armazenamos na nossa tabela de símbolos
                tabela_de_simbolos[var_name] = valor
                println("   (Atribuindo $var_name = $valor)")
            else
                # Declaração sem inicialização (ex: int a;)
                tabela_de_simbolos[var_name] = nothing
            end
            
        elseif stmt_type == "Return"
            # Instrução de retorno (ex: return b - 1)
            
            # Calcula o valor da expressão de retorno
            valor_retorno = avaliar_expressao(stmt["value"])
            
            println("Função terminou com sucesso.")
            # Retorna o valor final da função
            return valor_retorno
        else
            @warn "Instrução não implementada: $stmt_type"
        end
    end
    
    # Se a função terminar sem um 'return' (como em C)
    println("Função terminou (sem retorno explícito).")
    return 0
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