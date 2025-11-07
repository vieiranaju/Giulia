# Generated from gramatica/MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MiniCParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#preprocessorDirective.
    def visitPreprocessorDirective(self, ctx:MiniCParser.PreprocessorDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:MiniCParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declaration.
    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initializer.
    def visitInitializer(self, ctx:MiniCParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#initializerList.
    def visitInitializerList(self, ctx:MiniCParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:MiniCParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structOrUnion.
    def visitStructOrUnion(self, ctx:MiniCParser.StructOrUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:MiniCParser.StructDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDeclaration.
    def visitStructDeclaration(self, ctx:MiniCParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:MiniCParser.StructDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDeclarator.
    def visitStructDeclarator(self, ctx:MiniCParser.StructDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declarator.
    def visitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:MiniCParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:MiniCParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameterList.
    def visitParameterList(self, ctx:MiniCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:MiniCParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#pointer.
    def visitPointer(self, ctx:MiniCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typeName.
    def visitTypeName(self, ctx:MiniCParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:MiniCParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:MiniCParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typedefName.
    def visitTypedefName(self, ctx:MiniCParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#constantExpression.
    def visitConstantExpression(self, ctx:MiniCParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MiniCParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:MiniCParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:MiniCParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:MiniCParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#andExpression.
    def visitAndExpression(self, ctx:MiniCParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#castExpression.
    def visitCastExpression(self, ctx:MiniCParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryOperator.
    def visitUnaryOperator(self, ctx:MiniCParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#postfixExpression.
    def visitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:MiniCParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#labeledStatement.
    def visitLabeledStatement(self, ctx:MiniCParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#blockItemList.
    def visitBlockItemList(self, ctx:MiniCParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#blockItem.
    def visitBlockItem(self, ctx:MiniCParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#selectionStatement.
    def visitSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#iterationStatement.
    def visitIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forCondition.
    def visitForCondition(self, ctx:MiniCParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forDeclaration.
    def visitForDeclaration(self, ctx:MiniCParser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#jumpStatement.
    def visitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        return self.visitChildren(ctx)



del MiniCParser