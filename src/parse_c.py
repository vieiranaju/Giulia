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
            if init_decl.initializer():
                value = self.visit(init_decl.initializer().assignmentExpression())
                
            return {"type": "Declaration", "varType": var_type, "name": name, "value": value}
        
        elif ctx.declarator():
             name = ctx.declarator().getText()
             return {"type": "Declaration", "varType": var_type, "name": name, "value": None}

        return None

    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return ctx.getText()

    def visitStatement(self, ctx:MiniCParser.StatementContext):
        if ctx.jumpStatement():
            return self.visit(ctx.jumpStatement())
        return None

    def visitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        if ctx.Return():
            value = None
            if ctx.expression():
                value = self.visit(ctx.expression())
            return {"type": "Return", "value": value}
        return None

    # --- Expressões (Sem alterações) ---
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression(0))
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        return self.visit(ctx.conditionalExpression())
    def visitConditionalExpression(self, ctx:MiniCParser.ConditionalExpressionContext):
        return self.visit(ctx.logicalOrExpression())
    def visitLogicalOrExpression(self_exp, ctx:MiniCParser.LogicalOrExpressionContext):
        return self_exp.visit(ctx.logicalAndExpression(0))
    def visitLogicalAndExpression(self_exp, ctx:MiniCParser.LogicalAndExpressionContext):
        return self_exp.visit(ctx.inclusiveOrExpression(0))
    def visitInclusiveOrExpression(self_exp, ctx:MiniCParser.InclusiveOrExpressionContext):
        return self_exp.visit(ctx.exclusiveOrExpression(0))
    def visitExclusiveOrExpression(self_exp, ctx:MiniCParser.ExclusiveOrExpressionContext):
        return self_exp.visit(ctx.andExpression(0))
    def visitAndExpression(self_exp, ctx:MiniCParser.AndExpressionContext):
        return self_exp.visit(ctx.equalityExpression(0))
    def visitEqualityExpression(self_exp, ctx:MiniCParser.EqualityExpressionContext):
        return self_exp.visit(ctx.relationalExpression(0))
    def visitRelationalExpression(self_exp, ctx:MiniCParser.RelationalExpressionContext):
        return self_exp.visit(ctx.additiveExpression(0))
    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": ctx.getChild(1).getText(), "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.getChild(0))
    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 3:
            return {"type": "BinaryOp", "op": ctx.getChild(1).getText(), "left": self.visit(ctx.getChild(0)), "right": self.visit(ctx.getChild(2))}
        return self.visit(ctx.getChild(0))
    def visitCastExpression(self, ctx:MiniCParser.CastExpressionContext):
        return self.visit(ctx.unaryExpression())
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        return self.visit(ctx.postfixExpression())
    def visitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        return self.visit(ctx.primaryExpression())
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        if ctx.Identifier():
            return ctx.Identifier().getText()
        if ctx.Constant():
            return int(ctx.Constant().getText())
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