# Generated from c:/Users/roryb/Desktop/PJP/project-py-base/grammar/Language.g4 by ANTLR 4.13.1
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
        4,1,39,173,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,79,8,8,10,8,12,8,82,9,8,1,9,1,
        9,5,9,86,8,9,10,9,12,9,89,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,3,10,100,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,3,12,111,8,12,1,12,1,12,3,12,115,8,12,1,12,1,12,3,12,119,8,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,138,8,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,5,13,164,8,13,10,13,12,13,167,9,13,1,14,
        1,14,1,15,1,15,1,15,0,1,26,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,6,1,0,15,17,2,0,14,14,18,19,1,0,20,21,1,0,22,23,1,0,29,
        32,1,0,33,36,184,0,33,1,0,0,0,2,48,1,0,0,0,4,50,1,0,0,0,6,52,1,0,
        0,0,8,56,1,0,0,0,10,64,1,0,0,0,12,67,1,0,0,0,14,71,1,0,0,0,16,75,
        1,0,0,0,18,83,1,0,0,0,20,92,1,0,0,0,22,101,1,0,0,0,24,107,1,0,0,
        0,26,137,1,0,0,0,28,168,1,0,0,0,30,170,1,0,0,0,32,34,3,2,1,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,
        0,37,38,5,0,0,1,38,1,1,0,0,0,39,49,3,4,2,0,40,49,3,6,3,0,41,49,3,
        10,5,0,42,49,3,12,6,0,43,49,3,14,7,0,44,49,3,18,9,0,45,49,3,20,10,
        0,46,49,3,22,11,0,47,49,3,24,12,0,48,39,1,0,0,0,48,40,1,0,0,0,48,
        41,1,0,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,1,0,0,0,48,45,1,0,0,
        0,48,46,1,0,0,0,48,47,1,0,0,0,49,3,1,0,0,0,50,51,5,1,0,0,51,5,1,
        0,0,0,52,53,3,28,14,0,53,54,3,8,4,0,54,55,5,1,0,0,55,7,1,0,0,0,56,
        61,5,37,0,0,57,58,5,2,0,0,58,60,5,37,0,0,59,57,1,0,0,0,60,63,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,9,1,0,0,0,63,61,1,0,0,0,64,65,
        3,26,13,0,65,66,5,1,0,0,66,11,1,0,0,0,67,68,5,3,0,0,68,69,3,8,4,
        0,69,70,5,1,0,0,70,13,1,0,0,0,71,72,5,4,0,0,72,73,3,16,8,0,73,74,
        5,1,0,0,74,15,1,0,0,0,75,80,3,26,13,0,76,77,5,2,0,0,77,79,3,26,13,
        0,78,76,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,17,
        1,0,0,0,82,80,1,0,0,0,83,87,5,5,0,0,84,86,3,2,1,0,85,84,1,0,0,0,
        86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,
        0,0,0,90,91,5,6,0,0,91,19,1,0,0,0,92,93,5,7,0,0,93,94,5,8,0,0,94,
        95,3,26,13,0,95,96,5,9,0,0,96,99,3,2,1,0,97,98,5,10,0,0,98,100,3,
        2,1,0,99,97,1,0,0,0,99,100,1,0,0,0,100,21,1,0,0,0,101,102,5,11,0,
        0,102,103,5,8,0,0,103,104,3,26,13,0,104,105,5,9,0,0,105,106,3,2,
        1,0,106,23,1,0,0,0,107,108,5,12,0,0,108,110,5,8,0,0,109,111,3,26,
        13,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,114,5,1,
        0,0,113,115,3,26,13,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,
        0,0,0,116,118,5,1,0,0,117,119,3,26,13,0,118,117,1,0,0,0,118,119,
        1,0,0,0,119,120,1,0,0,0,120,121,5,9,0,0,121,122,3,2,1,0,122,25,1,
        0,0,0,123,124,6,13,-1,0,124,138,3,30,15,0,125,138,5,37,0,0,126,127,
        5,8,0,0,127,128,3,26,13,0,128,129,5,9,0,0,129,138,1,0,0,0,130,131,
        5,13,0,0,131,138,3,26,13,10,132,133,5,14,0,0,133,138,3,26,13,9,134,
        135,5,37,0,0,135,136,5,28,0,0,136,138,3,26,13,1,137,123,1,0,0,0,
        137,125,1,0,0,0,137,126,1,0,0,0,137,130,1,0,0,0,137,132,1,0,0,0,
        137,134,1,0,0,0,138,165,1,0,0,0,139,140,10,8,0,0,140,141,7,0,0,0,
        141,164,3,26,13,9,142,143,10,7,0,0,143,144,7,1,0,0,144,164,3,26,
        13,8,145,146,10,6,0,0,146,147,7,2,0,0,147,164,3,26,13,7,148,149,
        10,5,0,0,149,150,7,3,0,0,150,164,3,26,13,6,151,152,10,4,0,0,152,
        153,5,24,0,0,153,164,3,26,13,5,154,155,10,3,0,0,155,156,5,25,0,0,
        156,164,3,26,13,4,157,158,10,2,0,0,158,159,5,26,0,0,159,160,3,26,
        13,0,160,161,5,27,0,0,161,162,3,26,13,3,162,164,1,0,0,0,163,139,
        1,0,0,0,163,142,1,0,0,0,163,145,1,0,0,0,163,148,1,0,0,0,163,151,
        1,0,0,0,163,154,1,0,0,0,163,157,1,0,0,0,164,167,1,0,0,0,165,163,
        1,0,0,0,165,166,1,0,0,0,166,27,1,0,0,0,167,165,1,0,0,0,168,169,7,
        4,0,0,169,29,1,0,0,0,170,171,7,5,0,0,171,31,1,0,0,0,12,35,48,61,
        80,87,99,110,114,118,137,163,165
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'for'", 
                     "'!'", "'-'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", 
                     "'>'", "'=='", "'!='", "'&&'", "'||'", "'?'", "':'", 
                     "'='", "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BooleanLiteral", "StringLiteral", "IntegerLiteral", 
                      "FloatLiteral", "ID", "COMMENT", "WS" ]

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
    RULE_forStatement = 12
    RULE_expression = 13
    RULE_type = 14
    RULE_literal = 15

    ruleNames =  [ "program", "statement", "emptyStatement", "declarationStatement", 
                   "variableList", "expressionStatement", "readStatement", 
                   "writeStatement", "expressionList", "blockStatement", 
                   "ifStatement", "whileStatement", "forStatement", "expression", 
                   "type", "literal" ]

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
    T__29=30
    T__30=31
    T__31=32
    BooleanLiteral=33
    StringLiteral=34
    IntegerLiteral=35
    FloatLiteral=36
    ID=37
    COMMENT=38
    WS=39

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274341067194) != 0)):
                    break

            self.state = 37
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


        def forStatement(self):
            return self.getTypedRuleContext(LanguageParser.ForStatementContext,0)


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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.emptyStatement()
                pass
            elif token in [29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.declarationStatement()
                pass
            elif token in [8, 13, 14, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.expressionStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.readStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.writeStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.blockStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.whileStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 9)
                self.state = 47
                self.forStatement()
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
            self.state = 50
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
            self.state = 52
            self.type_()
            self.state = 53
            self.variableList()
            self.state = 54
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
            self.state = 56
            self.match(LanguageParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 57
                self.match(LanguageParser.T__1)
                self.state = 58
                self.match(LanguageParser.ID)
                self.state = 63
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
            self.state = 64
            self.expression(0)
            self.state = 65
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
            self.state = 67
            self.match(LanguageParser.T__2)
            self.state = 68
            self.variableList()
            self.state = 69
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
            self.state = 71
            self.match(LanguageParser.T__3)
            self.state = 72
            self.expressionList()
            self.state = 73
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
            self.state = 75
            self.expression(0)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 76
                self.match(LanguageParser.T__1)
                self.state = 77
                self.expression(0)
                self.state = 82
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
            self.state = 83
            self.match(LanguageParser.T__4)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274341067194) != 0):
                self.state = 84
                self.statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
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
            self.state = 92
            self.match(LanguageParser.T__6)
            self.state = 93
            self.match(LanguageParser.T__7)
            self.state = 94
            self.expression(0)
            self.state = 95
            self.match(LanguageParser.T__8)
            self.state = 96
            self.statement()
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(LanguageParser.T__9)
                self.state = 98
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
            self.state = 101
            self.match(LanguageParser.T__10)
            self.state = 102
            self.match(LanguageParser.T__7)
            self.state = 103
            self.expression(0)
            self.state = 104
            self.match(LanguageParser.T__8)
            self.state = 105
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init = None # ExpressionContext
            self.cond = None # ExpressionContext
            self.step = None # ExpressionContext

        def statement(self):
            return self.getTypedRuleContext(LanguageParser.StatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = LanguageParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LanguageParser.T__11)
            self.state = 108
            self.match(LanguageParser.T__7)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266287997184) != 0):
                self.state = 109
                localctx.init = self.expression(0)


            self.state = 112
            self.match(LanguageParser.T__0)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266287997184) != 0):
                self.state = 113
                localctx.cond = self.expression(0)


            self.state = 116
            self.match(LanguageParser.T__0)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266287997184) != 0):
                self.state = 117
                localctx.step = self.expression(0)


            self.state = 120
            self.match(LanguageParser.T__8)
            self.state = 121
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


    class TernaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LanguageParser.ExpressionContext
            super().__init__(parser)
            self.cond = None # ExpressionContext
            self.th = None # ExpressionContext
            self.el = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpr" ):
                listener.enterTernaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpr" ):
                listener.exitTernaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpr" ):
                return visitor.visitTernaryExpr(self)
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LanguageParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 124
                self.literal()
                pass

            elif la_ == 2:
                localctx = LanguageParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(LanguageParser.ID)
                pass

            elif la_ == 3:
                localctx = LanguageParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(LanguageParser.T__7)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(LanguageParser.T__8)
                pass

            elif la_ == 4:
                localctx = LanguageParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(LanguageParser.T__12)
                self.state = 131
                self.expression(10)
                pass

            elif la_ == 5:
                localctx = LanguageParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(LanguageParser.T__13)
                self.state = 133
                self.expression(9)
                pass

            elif la_ == 6:
                localctx = LanguageParser.AssignmentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(LanguageParser.ID)
                self.state = 135
                self.match(LanguageParser.T__27)
                self.state = 136
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 163
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.MultiplicativeExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 140
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 141
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.AdditiveExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 143
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 802816) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.RelationalExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 146
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.EqualityExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 149
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.AndExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 152
                        self.match(LanguageParser.T__23)
                        self.state = 153
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.OrExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 155
                        self.match(LanguageParser.T__24)
                        self.state = 156
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = LanguageParser.TernaryExprContext(self, LanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.cond = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 158
                        self.match(LanguageParser.T__25)
                        self.state = 159
                        localctx.th = self.expression(0)
                        self.state = 160
                        self.match(LanguageParser.T__26)
                        self.state = 161
                        localctx.el = self.expression(3)
                        pass

             
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
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
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




