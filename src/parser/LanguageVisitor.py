# Generated from c:/Users/roryb/Desktop/PJP/project-py-base/grammar/Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete generic visitor for a parse tree produced by LanguageParser.

class LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LanguageParser#program.
    def visitProgram(self, ctx:LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statement.
    def visitStatement(self, ctx:LanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#emptyStatement.
    def visitEmptyStatement(self, ctx:LanguageParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:LanguageParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#variableList.
    def visitVariableList(self, ctx:LanguageParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionStatement.
    def visitExpressionStatement(self, ctx:LanguageParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#readStatement.
    def visitReadStatement(self, ctx:LanguageParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#writeStatement.
    def visitWriteStatement(self, ctx:LanguageParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionList.
    def visitExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#blockStatement.
    def visitBlockStatement(self, ctx:LanguageParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#ifStatement.
    def visitIfStatement(self, ctx:LanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:LanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#forStatement.
    def visitForStatement(self, ctx:LanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#assignmentExpr.
    def visitAssignmentExpr(self, ctx:LanguageParser.AssignmentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#orExpr.
    def visitOrExpr(self, ctx:LanguageParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:LanguageParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#relationalExpr.
    def visitRelationalExpr(self, ctx:LanguageParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#parenExpr.
    def visitParenExpr(self, ctx:LanguageParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#variableExpr.
    def visitVariableExpr(self, ctx:LanguageParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#notExpr.
    def visitNotExpr(self, ctx:LanguageParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:LanguageParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#literalExpr.
    def visitLiteralExpr(self, ctx:LanguageParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:LanguageParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#equalityExpr.
    def visitEqualityExpr(self, ctx:LanguageParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#TernaryExpr.
    def visitTernaryExpr(self, ctx:LanguageParser.TernaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#andExpr.
    def visitAndExpr(self, ctx:LanguageParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#type.
    def visitType(self, ctx:LanguageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#literal.
    def visitLiteral(self, ctx:LanguageParser.LiteralContext):
        return self.visitChildren(ctx)



del LanguageParser