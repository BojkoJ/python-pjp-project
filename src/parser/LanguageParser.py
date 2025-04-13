# Generated from c:/Users/roryb/Desktop/PJP/project-py/grammar/Language.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        57,8,4,10,4,12,4,60,9,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,9,1,9,5,9,83,8,9,10,
        9,12,9,86,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,97,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,119,8,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,139,8,12,10,12,12,12,142,9,12,1,13,1,13,1,14,
        1,14,1,14,0,1,24,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,6,
        1,0,14,16,2,0,13,13,17,18,1,0,19,20,1,0,21,22,1,0,26,29,1,0,30,33,
        155,0,31,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,53,1,0,
        0,0,10,61,1,0,0,0,12,64,1,0,0,0,14,68,1,0,0,0,16,72,1,0,0,0,18,80,
        1,0,0,0,20,89,1,0,0,0,22,98,1,0,0,0,24,118,1,0,0,0,26,143,1,0,0,
        0,28,145,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,
        1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,
        46,3,4,2,0,38,46,3,6,3,0,39,46,3,10,5,0,40,46,3,12,6,0,41,46,3,14,
        7,0,42,46,3,18,9,0,43,46,3,20,10,0,44,46,3,22,11,0,45,37,1,0,0,0,
        45,38,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,
        0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,5,1,0,0,48,
        5,1,0,0,0,49,50,3,26,13,0,50,51,3,8,4,0,51,52,5,1,0,0,52,7,1,0,0,
        0,53,58,5,34,0,0,54,55,5,2,0,0,55,57,5,34,0,0,56,54,1,0,0,0,57,60,
        1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,9,1,0,0,0,60,58,1,0,0,0,61,
        62,3,24,12,0,62,63,5,1,0,0,63,11,1,0,0,0,64,65,5,3,0,0,65,66,3,8,
        4,0,66,67,5,1,0,0,67,13,1,0,0,0,68,69,5,4,0,0,69,70,3,16,8,0,70,
        71,5,1,0,0,71,15,1,0,0,0,72,77,3,24,12,0,73,74,5,2,0,0,74,76,3,24,
        12,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,
        17,1,0,0,0,79,77,1,0,0,0,80,84,5,5,0,0,81,83,3,2,1,0,82,81,1,0,0,
        0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,
        1,0,0,0,87,88,5,6,0,0,88,19,1,0,0,0,89,90,5,7,0,0,90,91,5,8,0,0,
        91,92,3,24,12,0,92,93,5,9,0,0,93,96,3,2,1,0,94,95,5,10,0,0,95,97,
        3,2,1,0,96,94,1,0,0,0,96,97,1,0,0,0,97,21,1,0,0,0,98,99,5,11,0,0,
        99,100,5,8,0,0,100,101,3,24,12,0,101,102,5,9,0,0,102,103,3,2,1,0,
        103,23,1,0,0,0,104,105,6,12,-1,0,105,119,3,28,14,0,106,119,5,34,
        0,0,107,108,5,8,0,0,108,109,3,24,12,0,109,110,5,9,0,0,110,119,1,
        0,0,0,111,112,5,12,0,0,112,119,3,24,12,9,113,114,5,13,0,0,114,119,
        3,24,12,8,115,116,5,34,0,0,116,117,5,25,0,0,117,119,3,24,12,1,118,
        104,1,0,0,0,118,106,1,0,0,0,118,107,1,0,0,0,118,111,1,0,0,0,118,
        113,1,0,0,0,118,115,1,0,0,0,119,140,1,0,0,0,120,121,10,7,0,0,121,
        122,7,0,0,0,122,139,3,24,12,8,123,124,10,6,0,0,124,125,7,1,0,0,125,
        139,3,24,12,7,126,127,10,5,0,0,127,128,7,2,0,0,128,139,3,24,12,6,
        129,130,10,4,0,0,130,131,7,3,0,0,131,139,3,24,12,5,132,133,10,3,
        0,0,133,134,5,23,0,0,134,139,3,24,12,4,135,136,10,2,0,0,136,137,
        5,24,0,0,137,139,3,24,12,3,138,120,1,0,0,0,138,123,1,0,0,0,138,126,
        1,0,0,0,138,129,1,0,0,0,138,132,1,0,0,0,138,135,1,0,0,0,139,142,
        1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,25,1,0,0,0,142,140,1,
        0,0,0,143,144,7,4,0,0,144,27,1,0,0,0,145,146,7,5,0,0,146,29,1,0,
        0,0,9,33,45,58,77,84,96,118,138,140
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'!'", 
                     "'-'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", "'>'", 
                     "'=='", "'!='", "'&&'", "'||'", "'='", "'int'", "'float'", 
                     "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BooleanLiteral", "StringLiteral", 
                      "IntegerLiteral", "FloatLiteral", "ID", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_emptyStatement = 2
    RULE_declarationStatement = 3
    RULE_variableList = 4
    RULE_expressionStatement = 5
    RULE_readStatement = 6
    RULE_writeStatement = 7
    RULE_expressionList = 8
    RULE_blockStatement = 9
    RULE_ifStatement = 10
    RULE_whileStatement = 11
    RULE_expression = 12
    RULE_type = 13
    RULE_literal = 14

    ruleNames =  [ "program", "statement", "emptyStatement", "declarationStatement", 
                   "variableList", "expressionStatement", "readStatement", 
                   "writeStatement", "expressionList", "blockStatement", 
                   "ifStatement", "whileStatement", "expression", "type", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    BooleanLiteral=30
    StringLiteral=31
    IntegerLiteral=32
    FloatLiteral=33
    ID=34
    COMMENT=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34292644282) != 0)):
                    break

            self.state = 35
            self.match(LanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def emptyStatement(self):
            return self.getTypedRuleContext(LanguageParser.EmptyStatementContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(LanguageParser.DeclarationStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(LanguageParser.ReadStatementContext,0)


        def writeStatement(self):
            return self.getTypedRuleContext(LanguageParser.WriteStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(LanguageParser.BlockStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(LanguageParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(LanguageParser.WhileStatementContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.emptyStatement()
                pass
            elif token in [26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.declarationStatement()
                pass
            elif token in [8, 12, 13, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.expressionStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.readStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.writeStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.blockStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 43
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 44
                self.whileStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LanguageParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement(self):

        localctx = LanguageParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(LanguageParser.TypeContext,0)


        def variableList(self):
            return self.getTypedRuleContext(LanguageParser.VariableListContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = LanguageParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.type_()
            self.state = 50
            self.variableList()
            self.state = 51
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.ID)
            else:
                return self.getToken(LanguageParser.ID, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_variableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableList" ):
                listener.enterVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableList" ):
                listener.exitVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableList" ):
                return visitor.visitVariableList(self)
            else:
                return visitor.visitChildren(self)




    def variableList(self):

        localctx = LanguageParser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(LanguageParser.ID)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 54
                self.match(LanguageParser.T__1)
                self.state = 55
                self.match(LanguageParser.ID)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = LanguageParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.expression(0)
            self.state = 62
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableList(self):
            return self.getTypedRuleContext(LanguageParser.VariableListContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_readStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)




    def readStatement(self):

        localctx = LanguageParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_readStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LanguageParser.T__2)
            self.state = 65
            self.variableList()
            self.state = 66
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_writeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)




    def writeStatement(self):

        localctx = LanguageParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_writeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LanguageParser.T__3)
            self.state = 69
            self.expressionList()
            self.state = 70
            self.match(LanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = LanguageParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.expression(0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 73
                self.match(LanguageParser.T__1)
                self.state = 74
                self.expression(0)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = LanguageParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LanguageParser.T__4)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34292644282) != 0):
                self.state = 81
                self.statement()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(LanguageParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = LanguageParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(LanguageParser.T__6)
            self.state = 90
            self.match(LanguageParser.T__7)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(LanguageParser.T__8)
            self.state = 93
            self.statement()
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 94
                self.match(LanguageParser.T__9)
                self.state = 95
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(LanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = LanguageParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(LanguageParser.T__10)
            self.state = 99
            self.match(LanguageParser.T__7)
            self.state = 100
            self.expression(0)
            self.state = 101
            self.match(LanguageParser.T__8)
            self.state = 102
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LanguageParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AssignmentExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpr" ):
                listener.enterAssignmentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpr" ):
                listener.exitAssignmentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpr" ):
                return visitor.visitAssignmentExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(LanguageParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = LanguageParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 105
                self.literal()
                pass

            elif la_ == 2:
                localctx = LanguageParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(LanguageParser.ID)
                pass

            elif la_ == 3:
                localctx = LanguageParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(LanguageParser.T__7)
                self.state = 108
                self.expression(0)
                self.state = 109
                self.match(LanguageParser.T__8)
                pass

            elif la_ == 4:
                localctx = LanguageParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(LanguageParser.T__11)
                self.state = 112
                self.expression(9)
                pass

            elif la_ == 5:
                localctx = LanguageParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(LanguageParser.T__12)
                self.state = 114
                self.expression(8)
                pass

            elif la_ == 6:
                localctx = LanguageParser.AssignmentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(LanguageParser.ID)
                self.state = 116
                self.match(LanguageParser.T__24)
                self.state = 117
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 138
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.MultiplicativeExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 121
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 122
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.AdditiveExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 124
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 401408) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.RelationalExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 127
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.EqualityExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 130
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.AndExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 133
                        self.match(LanguageParser.T__22)
                        self.state = 134
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.OrExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 136
                        self.match(LanguageParser.T__23)
                        self.state = 137
                        self.expression(3)
                        pass

             
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LanguageParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = LanguageParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(LanguageParser.IntegerLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(LanguageParser.FloatLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(LanguageParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(LanguageParser.StringLiteral, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LanguageParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




