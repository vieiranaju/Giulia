# src/parse_c.py
import sys
import os
import json
from antlr4 import *

# --- ATUALIZAÇÃO IMPORTANTE ---
# Adiciona a pasta 'gramatica' (que está um nível acima e
# depois "para dentro" de 'gramatica') ao path do Python.
script_dir = os.path.dirname(__file__)
grammar_dir = os.path.join(script_dir, '..', 'gramatica')
sys.path.append(os.path.abspath(grammar_dir))

# Agora o Python consegue encontrar estes ficheiros dentro da pasta /gramatica
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor

class AstVisitor(MiniCVisitor):

    def visitCompilationUnit(self, ctx:MiniCParser.CompilationUnitContext):
        resultados = []
        for decl in ctx.externalDeclaration():
            resultado_visit = self.visit(decl)
            if resultado_visit:
                resultados.append(resultado_visit)
        return resultados

    # --- CORREÇÃO IMPORTANTE AQUI ---
    def visitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        return_type = self.visit(ctx.typeSpecifier())
        
        # Lógica melhorada para encontrar APENAS o nome da função
        declarator_ctx = ctx.declarator()
        direct_decl_ctx = declarator_ctx.directDeclarator()
        
        # Navega para a "raiz" do nome, caso esteja aninhado
        # (ex: em 'main()', 'main' é o 'directDeclarator' filho)
        while direct_decl_ctx.directDeclarator():
             direct_decl_ctx = direct_decl_ctx.directDeclarator()
             
        # Pega o texto do 'Identifier' (o nome puro)
        name = direct_decl_ctx.Identifier().getText()
        
        body = self.visit(ctx.compoundStatement())
        
        return {
            "type": "Function",
            "name": name, # <- Agora será "main", e não "main(void)"
            "returnType": return_type,
            "body": body
        }
    # --- FIM DA CORREÇÃO ---

    def visitCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        body = []
        if ctx.blockItemList():
            body = self.visit(ctx.blockItemList())
        return body

    def visitBlockItemList(self, ctx:MiniCParser.BlockItemListContext):
        items = []
        for item in ctx.blockItem():
            resultado_item = self.visit(item)
            if resultado_item:
                items.append(resultado_item)
        return items

    def visitBlockItem(self, ctx:MiniCParser.BlockItemContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        if ctx.declaration():
            return self.visit(ctx.declaration())
        return None

    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        var_type = self.visit(ctx.typeSpecifier())
        
        if ctx.initDeclaratorList():
            init_decl = ctx.initDeclaratorList().initDeclarator(0)
            
            name = init_decl.declarator().getText()
            value = None
            is_array = False
            array_size = None

            # Detecta se o declarator contém '[]' (array) via texto simples
            if '[' in name and name.endswith(']'):
                is_array = True
                # separa o nome da parte do colchete: ex: a[10] -> ('a','10')
                base = name.split('[')[0]
                size_part = name[name.find('[')+1:-1]
                name = base
                if size_part.strip() != '':
                    try:
                        array_size = int(size_part)
                    except:
                        array_size = None

            if init_decl.initializer():
                # initializer pode ser assignmentExpression ou initializerList
                init = init_decl.initializer()
                if init.assignmentExpression():
                    value = self.visit(init.assignmentExpression())
                elif init.initializerList():
                    # constrói uma lista de valores a partir do initializerList
                    values = []
                    for it in init.initializerList().initializer():
                        # cada initializer pode ser assignmentExpression ou outra lista
                        if it.assignmentExpression():
                            values.append(self.visit(it.assignmentExpression()))
                        else:
                            # aninhado; fallback para None
                            values.append(None)
                    value = values
            return {"type": "Declaration", "varType": var_type, "name": name, "value": value, "isArray": is_array, "size": array_size}
        
        elif ctx.declarator():
             name = ctx.declarator().getText()
             return {"type": "Declaration", "varType": var_type, "name": name, "value": None}

        return None

    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return ctx.getText()

    def visitStatement(self, ctx:MiniCParser.StatementContext):
        if ctx.jumpStatement():
            return self.visit(ctx.jumpStatement())
        elif ctx.selectionStatement():
            return self.visit(ctx.selectionStatement())
        elif ctx.iterationStatement():
            return self.visit(ctx.iterationStatement())
        elif ctx.expressionStatement():
            return self.visit(ctx.expressionStatement())
        elif ctx.compoundStatement():
            # Para compound statements aninhados, retorna o body diretamente
            return {"type": "Block", "body": self.visit(ctx.compoundStatement())}
        return None

    def visitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        if ctx.Return():
            value = None
            if ctx.expression():
                value = self.visit(ctx.expression())
            return {"type": "Return", "value": value}
        return None

    def visitSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        if ctx.If():
            condition = self.visit(ctx.expression())
            then_stmt = self.visit(ctx.statement(0))
            
            # Verifica se tem else
            if len(ctx.statement()) > 1:
                else_stmt = self.visit(ctx.statement(1))
                # Extrai o body se for um Block
                then_body = then_stmt["body"] if then_stmt and then_stmt.get("type") == "Block" else [then_stmt] if then_stmt else []
                else_body = else_stmt["body"] if else_stmt and else_stmt.get("type") == "Block" else [else_stmt] if else_stmt else []
                return {"type": "IfElse", "condition": condition, "thenBody": then_body, "elseBody": else_body}
            else:
                then_body = then_stmt["body"] if then_stmt and then_stmt.get("type") == "Block" else [then_stmt] if then_stmt else []
                return {"type": "If", "condition": condition, "thenBody": then_body}
        
        elif ctx.Switch():
            value = self.visit(ctx.expression())
            # O statement do switch deve ser um compoundStatement com cases
            switch_body = ctx.statement(0)
            cases = []
            if switch_body.compoundStatement():
                # Processa os blockItems que são labeledStatements (Case/Default)
                if switch_body.compoundStatement().blockItemList():
                    cases = self.processSwitchCases(switch_body.compoundStatement().blockItemList())
            return {"type": "Switch", "value": value, "cases": cases}
        
        return None
    
    def processSwitchCases(self, blockItemList):
        """Processa os cases de um switch"""
        cases = []
        current_case = None
        
        for item in blockItemList.blockItem():
            if item.statement() and item.statement().labeledStatement():
                labeled = item.statement().labeledStatement()
                
                # Se havia um case anterior, adiciona à lista
                if current_case:
                    cases.append(current_case)
                
                if labeled.Case():
                    case_value = self.visit(labeled.constantExpression())
                    current_case = {
                        "type": "Case",
                        "value": case_value,
                        "body": [],
                        "hasBreak": False
                    }
                    # Processa o statement do case
                    case_stmt = self.visit(labeled.statement())
                    if case_stmt:
                        if case_stmt.get("type") == "Block":
                            current_case["body"] = case_stmt["body"]
                        else:
                            current_case["body"] = [case_stmt]
                
                elif labeled.Default():
                    current_case = {
                        "type": "Default",
                        "body": []
                    }
                    # Processa o statement do default
                    default_stmt = self.visit(labeled.statement())
                    if default_stmt:
                        if default_stmt.get("type") == "Block":
                            current_case["body"] = default_stmt["body"]
                        else:
                            current_case["body"] = [default_stmt]
            else:
                # Adiciona ao body do case atual
                if current_case:
                    stmt = None
                    if item.statement():
                        stmt = self.visit(item.statement())
                        # Verifica se é um break
                        if stmt and stmt.get("type") == "Break":
                            current_case["hasBreak"] = True
                            continue
                    elif item.declaration():
                        stmt = self.visit(item.declaration())
                    
                    if stmt:
                        if stmt.get("type") == "Block":
                            current_case["body"].extend(stmt["body"])
                        else:
                            current_case["body"].append(stmt)
        
        # Adiciona o último case
        if current_case:
            cases.append(current_case)
        
        return cases
    
    def visitIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        if ctx.While() and not ctx.Do():
            # While loop
            condition = self.visit(ctx.expression())
            body_stmt = self.visit(ctx.statement())
            body = body_stmt["body"] if body_stmt and body_stmt.get("type") == "Block" else [body_stmt] if body_stmt else []
            return {"type": "While", "condition": condition, "body": body}
        
        elif ctx.Do():
            # Do-While loop
            body_stmt = self.visit(ctx.statement())
            body = body_stmt["body"] if body_stmt and body_stmt.get("type") == "Block" else [body_stmt] if body_stmt else []
            condition = self.visit(ctx.expression())
            return {"type": "DoWhile", "body": body, "condition": condition}
        
        elif ctx.For():
            # For loop
            for_cond = ctx.forCondition()
            
            # Init (pode ser declaration ou expression)
            init = None
            if for_cond.forDeclaration():
                init = self.visit(for_cond.forDeclaration())
            elif for_cond.expression(0):
                # Se for uma atribuição simples
                init = self.visitExpressionAsStatement(for_cond.expression(0))
            
            # Condition
            condition = None
            if len(for_cond.expression()) > 1:
                condition = self.visit(for_cond.expression(1))
            elif len(for_cond.expression()) == 1 and not for_cond.forDeclaration():
                condition = self.visit(for_cond.expression(0))
            
            # Increment
            increment = None
            if len(for_cond.expression()) >= 2:
                increment = self.visit(for_cond.expression(2))
            elif len(for_cond.expression()) == 2 and not for_cond.forDeclaration():
                increment = self.visit(for_cond.expression(1))
            
            # Body
            body_stmt = self.visit(ctx.statement())
            body = body_stmt["body"] if body_stmt and body_stmt.get("type") == "Block" else [body_stmt] if body_stmt else []
            
            return {
                "type": "For",
                "init": init,
                "condition": condition,
                "increment": increment,
                "body": body
            }
        
        return None
    
    def visitForDeclaration(self, ctx:MiniCParser.ForDeclarationContext):
        """Processa a declaração no init de um for"""
        var_type = self.visit(ctx.typeSpecifier())
        init_decl = ctx.initDeclaratorList().initDeclarator(0)
        name = init_decl.declarator().getText()
        value = None
        is_array = False
        array_size = None
        if '[' in name and name.endswith(']'):
            is_array = True
            base = name.split('[')[0]
            size_part = name[name.find('[')+1:-1]
            name = base
            if size_part.strip() != '':
                try:
                    array_size = int(size_part)
                except:
                    array_size = None

        if init_decl.initializer():
            init = init_decl.initializer()
            if init.assignmentExpression():
                value = self.visit(init.assignmentExpression())
            elif init.initializerList():
                values = []
                for it in init.initializerList().initializer():
                    if it.assignmentExpression():
                        values.append(self.visit(it.assignmentExpression()))
                    else:
                        values.append(None)
                value = values

        return {"type": "Declaration", "varType": var_type, "name": name, "value": value, "isArray": is_array, "size": array_size}
    
    def visitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        """Processa expressionStatement (geralmente atribuições ou chamadas de função)"""
        if ctx.expression():
            return self.visitExpressionAsStatement(ctx.expression())
        return None
    
    def visitExpressionAsStatement(self, expr_ctx):
        """Converte uma expressão em um statement (geralmente Assignment)"""
        # Verifica se é uma atribuição (detecta pelo operador '=')
        if expr_ctx.assignmentExpression():
            assign_expr = expr_ctx.assignmentExpression(0)
            # Verifica se tem operador de atribuição
            if assign_expr.assignmentOperator():
                # É uma atribuição
                var_name = self.visit(assign_expr.unaryExpression())  # lado esquerdo
                value = self.visit(assign_expr.assignmentExpression())  # lado direito
                return {"type": "Assignment", "name": var_name, "value": value}
            else:
                # É apenas uma expressão (pode ser chamada de função, etc)
                return self.visit(assign_expr)
        return None
    
    def visitConstantExpression(self, ctx:MiniCParser.ConstantExpressionContext):
        """Processa constant expression (usado em case)"""
        return self.visit(ctx.conditionalExpression())

    # --- Expressões ---
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression(0))
    
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        # Verifica se tem atribuição (unaryExpression assignmentOperator assignmentExpression)
        if ctx.assignmentOperator():
            var_name = self.visit(ctx.unaryExpression())
            value = self.visit(ctx.assignmentExpression())
            return {"type": "Assignment", "name": var_name, "value": value}
        return self.visit(ctx.conditionalExpression())
    
    def visitConditionalExpression(self, ctx:MiniCParser.ConditionalExpressionContext):
        return self.visit(ctx.logicalOrExpression())
    
    def visitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": "||", "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.logicalAndExpression(0))
    
    def visitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": "&&", "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.inclusiveOrExpression(0))
    
    def visitInclusiveOrExpression(self, ctx:MiniCParser.InclusiveOrExpressionContext):
        return self.visit(ctx.exclusiveOrExpression(0))
    
    def visitExclusiveOrExpression(self, ctx:MiniCParser.ExclusiveOrExpressionContext):
        return self.visit(ctx.andExpression(0))
    
    def visitAndExpression(self, ctx:MiniCParser.AndExpressionContext):
        return self.visit(ctx.equalityExpression(0))
    
    def visitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": ctx.getChild(1).getText(), "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.relationalExpression(0))
    
    def visitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": ctx.getChild(1).getText(), "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.additiveExpression(0))
    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        # Processa expressões aditivas: a + b - c + d
        # A gramática é: multiplicativeExpression ( (Plus | Minus) multiplicativeExpression )*
        result = self.visit(ctx.multiplicativeExpression(0))
        
        # Se houver múltiplas expressões multiplicativas, processa cada operador
        mult_count = len(ctx.multiplicativeExpression())
        for i in range(1, mult_count):
            # O operador está entre as expressões multiplicativas
            # getChild(i*2 - 1) pega o operador (índices ímpares)
            op_index = i * 2 - 1
            op = ctx.getChild(op_index).getText()
            right = self.visit(ctx.multiplicativeExpression(i))
            result = {"type": "BinaryOp", "op": op, "left": result, "right": right}
        
        return result
    
    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        # Processa expressões multiplicativas: a * b / c % d
        result = self.visit(ctx.castExpression(0))
        
        cast_count = len(ctx.castExpression())
        for i in range(1, cast_count):
            op_index = i * 2 - 1
            op = ctx.getChild(op_index).getText()
            right = self.visit(ctx.castExpression(i))
            result = {"type": "BinaryOp", "op": op, "left": result, "right": right}
        
        return result
    
    def visitCastExpression(self, ctx:MiniCParser.CastExpressionContext):
        return self.visit(ctx.unaryExpression())
    
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        return self.visit(ctx.postfixExpression())
    
    def visitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        # Trata postfix expressions (por exemplo: a[0], a[i+1], chamadas) --
        # implementamos aqui suporte mínimo para acesso a arrays: a[expr]
        node = self.visit(ctx.primaryExpression())

        # Os sufixos (como [ expression ]) aparecem como filhos adicionais.
        # Iteramos sobre as crianças para detectar colchetes e construir
        # nós do tipo ArrayAccess encadeados (para casos como a[b][c]).
        i = 1
        child_count = ctx.getChildCount()
        while i < child_count:
            child = ctx.getChild(i)
            txt = child.getText()
            if txt == '[':
                # índice é o próximo filho
                index_ctx = ctx.getChild(i+1)
                index_node = self.visit(index_ctx)
                node = {"type": "ArrayAccess", "array": node, "index": index_node}
                # pula os 3 tokens: '[' expression ']'
                i += 3
                continue
            # Para outros sufixos (chamada, . , ->, ++, --) não implementados — apenas ignoramos
            i += 1

        return node
    
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        # Identificadores retornam uma STRING simples (nome da variável)
        if ctx.Identifier():
            return ctx.Identifier().getText()

        # Constant pode ser Integer, Floating ou CharacterConstant
        if ctx.Constant():
            txt = ctx.Constant().getText()
            # Character literal: 'a' ou escapes
            if txt.startswith("'") and txt.endswith("'"):
                # remove as aspas simples e trata escapes simples (\') e (\\)
                inner = txt[1:-1]
                # remove escape backslash if presente
                if inner.startswith('\\') and len(inner) >= 2:
                    val = inner[1]
                else:
                    val = inner
                return {"type": "Char", "value": val}

            # Floating point (contém '.')
            if '.' in txt:
                try:
                    return float(txt)
                except:
                    return float(txt)

            # Inteiro
            try:
                return int(txt)
            except:
                return int(txt)

        # StringLiteral(s) (podem ser concatenadas): juntamos todas
        if ctx.StringLiteral():
            parts = []
            for i in range(len(ctx.StringLiteral())):
                s = ctx.StringLiteral(i).getText()
                # remove aspas duplas e trata escapes simples
                inner = s[1:-1]
                inner = inner.replace('\\"', '"').replace('\\\\', '\\')
                parts.append(inner)
            full = ''.join(parts)
            return {"type": "String", "value": full}

        if ctx.LeftParen():
            return self.visit(ctx.expression())
        return None

# --- Função Main ---
def main(argv):
    # O primeiro argumento (argv[1]) será o *caminho* para o ficheiro de teste
    # ex: "exemplos/teste.c"
    input_path = argv[1]

    # O ficheiro de saída será guardado na pasta raiz (ou onde você preferir)
    output_path = "codigo_simplificado.json"

    input_stream = FileStream(input_path)
    lexer = MiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    tree = parser.compilationUnit()

    visitor = AstVisitor()
    ast_simplificada = visitor.visit(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ast_simplificada, f, indent=2)

    print(f"✅ AST simplificada gerada em {output_path}")

if __name__ == '__main__':
    main(sys.argv)