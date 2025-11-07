# Generated from gramatica/MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#compilationUnit.
    def enterCompilationUnit(self, ctx:MiniCParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by MiniCParser#compilationUnit.
    def exitCompilationUnit(self, ctx:MiniCParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by MiniCParser#preprocessorDirective.
    def enterPreprocessorDirective(self, ctx:MiniCParser.PreprocessorDirectiveContext):
        pass

    # Exit a parse tree produced by MiniCParser#preprocessorDirective.
    def exitPreprocessorDirective(self, ctx:MiniCParser.PreprocessorDirectiveContext):
        pass


    # Enter a parse tree produced by MiniCParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:MiniCParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:MiniCParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#declaration.
    def enterDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#declaration.
    def exitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:MiniCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by MiniCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:MiniCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#initializer.
    def enterInitializer(self, ctx:MiniCParser.InitializerContext):
        pass

    # Exit a parse tree produced by MiniCParser#initializer.
    def exitInitializer(self, ctx:MiniCParser.InitializerContext):
        pass


    # Enter a parse tree produced by MiniCParser#initializerList.
    def enterInitializerList(self, ctx:MiniCParser.InitializerListContext):
        pass

    # Exit a parse tree produced by MiniCParser#initializerList.
    def exitInitializerList(self, ctx:MiniCParser.InitializerListContext):
        pass


    # Enter a parse tree produced by MiniCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:MiniCParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:MiniCParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#structOrUnion.
    def enterStructOrUnion(self, ctx:MiniCParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by MiniCParser#structOrUnion.
    def exitStructOrUnion(self, ctx:MiniCParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:MiniCParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:MiniCParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:MiniCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:MiniCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:MiniCParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:MiniCParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDeclarator.
    def enterStructDeclarator(self, ctx:MiniCParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDeclarator.
    def exitStructDeclarator(self, ctx:MiniCParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#declarator.
    def enterDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#declarator.
    def exitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:MiniCParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:MiniCParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:MiniCParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:MiniCParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameterList.
    def enterParameterList(self, ctx:MiniCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameterList.
    def exitParameterList(self, ctx:MiniCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:MiniCParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:MiniCParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#pointer.
    def enterPointer(self, ctx:MiniCParser.PointerContext):
        pass

    # Exit a parse tree produced by MiniCParser#pointer.
    def exitPointer(self, ctx:MiniCParser.PointerContext):
        pass


    # Enter a parse tree produced by MiniCParser#typeName.
    def enterTypeName(self, ctx:MiniCParser.TypeNameContext):
        pass

    # Exit a parse tree produced by MiniCParser#typeName.
    def exitTypeName(self, ctx:MiniCParser.TypeNameContext):
        pass


    # Enter a parse tree produced by MiniCParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:MiniCParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:MiniCParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:MiniCParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:MiniCParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#typedefName.
    def enterTypedefName(self, ctx:MiniCParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by MiniCParser#typedefName.
    def exitTypedefName(self, ctx:MiniCParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#constantExpression.
    def enterConstantExpression(self, ctx:MiniCParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#constantExpression.
    def exitConstantExpression(self, ctx:MiniCParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:MiniCParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:MiniCParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by MiniCParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:MiniCParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:MiniCParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:MiniCParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:MiniCParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:MiniCParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:MiniCParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#andExpression.
    def enterAndExpression(self, ctx:MiniCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#andExpression.
    def exitAndExpression(self, ctx:MiniCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#castExpression.
    def enterCastExpression(self, ctx:MiniCParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#castExpression.
    def exitCastExpression(self, ctx:MiniCParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryOperator.
    def enterUnaryOperator(self, ctx:MiniCParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryOperator.
    def exitUnaryOperator(self, ctx:MiniCParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by MiniCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:MiniCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:MiniCParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by MiniCParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:MiniCParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by MiniCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#labeledStatement.
    def enterLabeledStatement(self, ctx:MiniCParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#labeledStatement.
    def exitLabeledStatement(self, ctx:MiniCParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:MiniCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#blockItemList.
    def enterBlockItemList(self, ctx:MiniCParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by MiniCParser#blockItemList.
    def exitBlockItemList(self, ctx:MiniCParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by MiniCParser#blockItem.
    def enterBlockItem(self, ctx:MiniCParser.BlockItemContext):
        pass

    # Exit a parse tree produced by MiniCParser#blockItem.
    def exitBlockItem(self, ctx:MiniCParser.BlockItemContext):
        pass


    # Enter a parse tree produced by MiniCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MiniCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:MiniCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#iterationStatement.
    def enterIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#iterationStatement.
    def exitIterationStatement(self, ctx:MiniCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#forCondition.
    def enterForCondition(self, ctx:MiniCParser.ForConditionContext):
        pass

    # Exit a parse tree produced by MiniCParser#forCondition.
    def exitForCondition(self, ctx:MiniCParser.ForConditionContext):
        pass


    # Enter a parse tree produced by MiniCParser#forDeclaration.
    def enterForDeclaration(self, ctx:MiniCParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#forDeclaration.
    def exitForDeclaration(self, ctx:MiniCParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#jumpStatement.
    def enterJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#jumpStatement.
    def exitJumpStatement(self, ctx:MiniCParser.JumpStatementContext):
        pass



del MiniCParser