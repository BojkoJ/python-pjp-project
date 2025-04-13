# Generated from c:/Users/roryb/Desktop/PJP/project-py/grammar/Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by LanguageParser#program.
    def enterProgram(self, ctx:LanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by LanguageParser#program.
    def exitProgram(self, ctx:LanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by LanguageParser#statement.
    def enterStatement(self, ctx:LanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#statement.
    def exitStatement(self, ctx:LanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#emptyStatement.
    def enterEmptyStatement(self, ctx:LanguageParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#emptyStatement.
    def exitEmptyStatement(self, ctx:LanguageParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:LanguageParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:LanguageParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#variableList.
    def enterVariableList(self, ctx:LanguageParser.VariableListContext):
        pass

    # Exit a parse tree produced by LanguageParser#variableList.
    def exitVariableList(self, ctx:LanguageParser.VariableListContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionStatement.
    def enterExpressionStatement(self, ctx:LanguageParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionStatement.
    def exitExpressionStatement(self, ctx:LanguageParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#readStatement.
    def enterReadStatement(self, ctx:LanguageParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#readStatement.
    def exitReadStatement(self, ctx:LanguageParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#writeStatement.
    def enterWriteStatement(self, ctx:LanguageParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#writeStatement.
    def exitWriteStatement(self, ctx:LanguageParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionList.
    def enterExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionList.
    def exitExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by LanguageParser#blockStatement.
    def enterBlockStatement(self, ctx:LanguageParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#blockStatement.
    def exitBlockStatement(self, ctx:LanguageParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#ifStatement.
    def enterIfStatement(self, ctx:LanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#ifStatement.
    def exitIfStatement(self, ctx:LanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#whileStatement.
    def enterWhileStatement(self, ctx:LanguageParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#whileStatement.
    def exitWhileStatement(self, ctx:LanguageParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#assignmentExpr.
    def enterAssignmentExpr(self, ctx:LanguageParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#assignmentExpr.
    def exitAssignmentExpr(self, ctx:LanguageParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#variableExpr.
    def enterVariableExpr(self, ctx:LanguageParser.VariableExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#variableExpr.
    def exitVariableExpr(self, ctx:LanguageParser.VariableExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#notExpr.
    def enterNotExpr(self, ctx:LanguageParser.NotExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#notExpr.
    def exitNotExpr(self, ctx:LanguageParser.NotExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:LanguageParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:LanguageParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#literalExpr.
    def enterLiteralExpr(self, ctx:LanguageParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#literalExpr.
    def exitLiteralExpr(self, ctx:LanguageParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#orExpr.
    def enterOrExpr(self, ctx:LanguageParser.OrExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#orExpr.
    def exitOrExpr(self, ctx:LanguageParser.OrExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:LanguageParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:LanguageParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#relationalExpr.
    def enterRelationalExpr(self, ctx:LanguageParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#relationalExpr.
    def exitRelationalExpr(self, ctx:LanguageParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:LanguageParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:LanguageParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#parenExpr.
    def enterParenExpr(self, ctx:LanguageParser.ParenExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#parenExpr.
    def exitParenExpr(self, ctx:LanguageParser.ParenExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#equalityExpr.
    def enterEqualityExpr(self, ctx:LanguageParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#equalityExpr.
    def exitEqualityExpr(self, ctx:LanguageParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#andExpr.
    def enterAndExpr(self, ctx:LanguageParser.AndExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#andExpr.
    def exitAndExpr(self, ctx:LanguageParser.AndExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#type.
    def enterType(self, ctx:LanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by LanguageParser#type.
    def exitType(self, ctx:LanguageParser.TypeContext):
        pass


    # Enter a parse tree produced by LanguageParser#literal.
    def enterLiteral(self, ctx:LanguageParser.LiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#literal.
    def exitLiteral(self, ctx:LanguageParser.LiteralContext):
        pass



del LanguageParser