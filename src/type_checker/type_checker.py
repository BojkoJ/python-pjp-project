#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Type checker modul
# Tento modul provádí kontrolu typů na syntaktickém stromě a hlásí chyby typu.

from antlr4 import *
from src.parser.LanguageParser import LanguageParser
from src.parser.LanguageVisitor import LanguageVisitor

# Třída Type definuje typy, které jsou podporovány v našem jazyce.
class Type:
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    ERROR = "error"  # Typ pro chyby
    
    @staticmethod
    def to_string(type_value):
        # Převod typů na řetězec pro lepší čitelnost chybových hlášení
        if type_value == Type.INT:
            return "int"
        elif type_value == Type.FLOAT:
            return "float"
        elif type_value == Type.BOOL:
            return "bool"
        elif type_value == Type.STRING:
            return "string"
        else:
            return "error"

# Třída TypeCheckError reprezentuje chybu typu, která byla nalezena během kontroly typů.
# Obsahuje informace o řádku, sloupci a zprávě chyby.
class TypeCheckError:
    # Třída pro reprezentaci chyby typu, která byla nalezena během kontroly typů.
    def __init__(self, line, column, message):
        self.line = line # Řádek, kde došlo k chybě
        self.column = column # Sloupec, kde došlo k chybě
        self.message = message # Zpráva chyby
    
    def __str__(self):
        # Sestavení chybové zprávy
        return f"Type error at line {self.line}, column {self.column}: {self.message}"

class TypeChecker(LanguageVisitor):
    # Implementace Visitoru pro kontrolu typů v syntaktickém stromě. (parser tree)
    # Tato třída dědí z LanguageVisitor, což je generovaný visitor pro náš jazyk.
    def __init__(self):
        # Initializace type checkeru

        # Tady budeme ukládat typy proměnných (název -> typ)
        self.variables = {}
        
        # Tady budeme ukládat chyby, které byly nalezeny během kontroly typů
        self.errors = []
    
    def is_boolean_literal(self, expr_text):
        return expr_text == "true" or expr_text == "false"

    def has_errors(self):
        # Funkce pro kontrolu, zda byly nalezeny nějaké chyby. Pokud ano, vrátí True.
        return len(self.errors) > 0
    
    def report_errors(self):
        for error in self.errors:
            print(error)
    
    def add_error(self, ctx, message):
        if hasattr(ctx, 'start'):
            line = ctx.start.line
            column = ctx.start.column
        elif hasattr(ctx, 'symbol'):
            line = ctx.symbol.line
            column = ctx.symbol.column
        else:
            line = 0
            column = 0
        
        error = TypeCheckError(line, column, message)
        self.errors.append(error)
        
        return Type.ERROR
    
    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return None
    
    def visitEmptyStatement(self, ctx):
        return None
    
    def visitDeclarationStatement(self, ctx):
        # Funkce pro visit statementu pro deklaraci proměnné.

        # Získáme typ proměnné z kontextu
        type_name = ctx.type_().getText()
        
        # Získáme seznam proměnných z kontextu
        variables = ctx.variableList().ID()
        
        # Přidáme každou proměnnou do objektu (slovníku) proměnných
        for var in variables:
            var_name = var.getText()
            
            # Pokud je proměnná již deklarována, přidáme chybu do seznamu chyb
            if var_name in self.variables:
                self.add_error(var, f"Variable '{var_name}' is already declared")
            else: # Pokud ne, přidáme do objektu proměnných (slovníku)
                self.variables[var_name] = type_name
        
        return None
    
    def visitExpressionStatement(self, ctx):
        # Funkce pro visit statementu pro výraz.
        self.visit(ctx.expression())
        return None
    
    def visitReadStatement(self, ctx):
        # Funkce pro visit statementu pro čtení proměnné. (read)

        # Získáme seznam proměnných z kontextu
        variables = ctx.variableList().ID()
        
        # Kontrolujeme, zda je každá proměnná deklarována
        for var in variables:
            var_name = var.getText()
            
            # Pokud proměnná není deklarována, přidáme chybu do seznamu chyb
            if var_name not in self.variables:
                self.add_error(var, f"Variable '{var_name}' is not declared")
        
        return None
    
    def visitWriteStatement(self, ctx):
        # Funkce pro visit statementu pro zápis proměnné. (write)

        # Navštívíme všechny výrazy ve write statementu
        expressions = ctx.expressionList().expression()
        for expr in expressions:
            self.visit(expr)
        
        return None
    
    def visitBlockStatement(self, ctx):
        # Funkce pro visit bloku

        # Zavoláme visit na všechny statementy v bloku, blok jsou složené závorky
        for statement in ctx.statement():
            self.visit(statement)
        
        return None
    
    def visitIfStatement(self, ctx):
        # Funkce pro visit if statementu.

        # Navštívíme podmínku if statementu
        condition_type = self.visit(ctx.expression())
        
        # Kontrolujeme, zda je podmínka boolean, pokud ne, přidáme chybu do seznamu chyb
        if condition_type != Type.BOOL and condition_type != Type.ERROR:
            self.add_error(ctx.expression(), f"Condition must be of type bool, but got {Type.to_string(condition_type)}")
        
        # Navštívíme 'then' statement
        self.visit(ctx.statement(0))
        
        # Pokud je else statement, navštívíme ho
        if len(ctx.statement()) > 1:
            self.visit(ctx.statement(1))
        
        return None
    def visitWhileStatement(self, ctx):
        # Funkce pro visit while statementu.

        # Navštívíme podmínku while statementu
        condition_type = self.visit(ctx.expression())
        
        # Kontrolujeme, zda je podmínka boolean, pokud ne, přidáme chybu do seznamu chyb
        if condition_type != Type.BOOL and condition_type != Type.ERROR:
            self.add_error(ctx.expression(), f"Condition must be of type bool, but got {Type.to_string(condition_type)}")
        
        # Navštívíme tělo while statementu
        self.visit(ctx.statement())
        
        return None
    
    def visitForStatement(self, ctx:LanguageParser.ForStatementContext):
        # Funkce pro visit for statementu.

        # Navštívíme inicializační výraz (pokud existuje)
        if ctx.init:
            self.visit(ctx.init)

        # Navštívíme podmínkový výraz (pokud existuje) a zkontrolujeme typ
        condition_type = Type.BOOL
        
        if ctx.cond:
            condition_type = self.visit(ctx.cond)
            
            # Kontrolujeme, zda je podmínka boolean
            if condition_type != Type.BOOL and condition_type != Type.ERROR:
                self.add_error(ctx.cond, f"For loop condition must be of type bool, but got {Type.to_string(condition_type)}")

        # Navštívíme krokovací výraz (pokud existuje)
        if ctx.step:
            self.visit(ctx.step)

        # Navštívíme tělo cyklu
        self.visit(ctx.statement())

        return None
    
    # -------------------------------------------------------------------------------
    # Visitory pro jednotlivé výrazy, které se používají v našem jazyce:
    
    def visitVariableExpr(self, ctx):
        # Funkce pro visit proměnné v kontextu výrazu

        # Získáme název proměnné z kontextu
        var_name = ctx.ID().getText()
        
        # Kontrolujeme, zda je proměnná deklarována, pokud ne, přidáme chybu do seznamu chyb
        if var_name not in self.variables:
            return self.add_error(ctx, f"Variable '{var_name}' is not declared")
        
        # Pokud je proměnná deklarována, vrátíme její typ
        return self.variables[var_name]
    def visitLiteralExpr(self, ctx):
        # Funkce pro visit literalu (např. číslo, řetězec, boolean).
        # Např. takovýto výraz: 10, "Hello", true
        # V našem jazyce máme několik typů literálů: int, float, bool, string

        literal = ctx.literal()
        
        # Zkontrolujeme co to je za literal a vrátíme jeho typ
        if literal.IntegerLiteral() is not None:
            return Type.INT
        elif literal.FloatLiteral() is not None:
            return Type.FLOAT
        elif literal.BooleanLiteral() is not None:
            # Handle boolean literals explicitly, including "true" and "false"
            bool_text = literal.BooleanLiteral().getText()
            if bool_text == "true" or bool_text == "false":
                return Type.BOOL
            return Type.BOOL
        elif literal.StringLiteral() is not None:
            return Type.STRING
        
        # Sem by se nemělo dostat, pokud ano, přidáme chybu do seznamu chyb
        return self.add_error(ctx, "Unknown literal type")
    
    def visitParenExpr(self, ctx):
        # Funkce pro visit výrazu v závorkách (např. (x + y)).
        return self.visit(ctx.expression())
    
    def visitUnaryMinusExpr(self, ctx):
        # Funkce pro visit unární minus výrazu (např. -x).

        # Získáme typ operandu (výrazu) z kontextu
        operand_type = self.visit(ctx.expression())
        
        # Zjistíme, jestli je operand číslo (int nebo float)
        if operand_type == Type.INT:
            return Type.INT
        elif operand_type == Type.FLOAT:
            return Type.FLOAT
        elif operand_type == Type.ERROR:
            return Type.ERROR
        
        # Pokud to dojede sem, znamená to, že operand není číslo (int nebo float), přidáme chybu do seznamu chyb
        return self.add_error(ctx, f"Unary minus can only be applied to numeric types, but got {Type.to_string(operand_type)}")
    
    def visitNotExpr(self, ctx):
        # Funkce pro visit logického NOT výrazu (např. !x).

        operand_type = self.visit(ctx.expression())
        
        # Zjistíme, jestli je operand boolean
        if operand_type == Type.BOOL:
            return Type.BOOL
        elif operand_type == Type.ERROR:
            return Type.ERROR
        
        return self.add_error(ctx, f"Logical NOT can only be applied to boolean type, but got {Type.to_string(operand_type)}")
    
    def visitMultiplicativeExpr(self, ctx):
        # Funkce pro visit výrazu pro násobení, dělení a modulo

        # Získáme typy levého a pravého operandu (výrazu)
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        # Získáme operátor
        operator = ctx.getChild(1).getText()
        
        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        # Oba operandy musí být int
        if operator == '%':
            if left_type == Type.INT and right_type == Type.INT:
                return Type.INT
            else:
                return self.add_error(ctx, f"Modulo operator requires int operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
        
        # Oba operandy musí být číslo (int nebo float)
        if (left_type == Type.INT or left_type == Type.FLOAT) and (right_type == Type.INT or right_type == Type.FLOAT):
            # Pokud je alespoň jeden operand float, výsledek bude float
            if left_type == Type.FLOAT or right_type == Type.FLOAT:
                return Type.FLOAT
            else:
                return Type.INT
        
        return self.add_error(ctx, f"Multiplicative operators require numeric operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitAdditiveExpr(self, ctx):
        # Funkce pro visit výrazu pro sčítání, odčítání a spojení řetězců

        # Získáme typy levého a pravého operandu (výrazu)
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        # Získáme operátor
        operator = ctx.getChild(1).getText()
        
        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        # Pro spojení řetězců musí být oba operandy typu string
        if operator == '.':
            if left_type == Type.STRING and right_type == Type.STRING:
                return Type.STRING
            else:
                return self.add_error(ctx, f"String concatenation operator requires string operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
        
        # Pro sčítání, odčítání: oba operandy musí být číslo (int nebo float)
        if (left_type == Type.INT or left_type == Type.FLOAT) and (right_type == Type.INT or right_type == Type.FLOAT):
            # Pokud je alespoň jeden operand float, výsledek bude float
            if left_type == Type.FLOAT or right_type == Type.FLOAT:
                return Type.FLOAT
            else:
                return Type.INT
        
        return self.add_error(ctx, f"Additive operators require numeric operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitRelationalExpr(self, ctx):
        # Funkce pro visit porovnávacích výrazů (< > <= >=).

        # Získáme typy levého a pravého operandu (výrazu)
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))

        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        # Oba operandy musí být číslo (int nebo float)
        if (left_type == Type.INT or left_type == Type.FLOAT) and (right_type == Type.INT or right_type == Type.FLOAT):
            return Type.BOOL
        
        return self.add_error(ctx, f"Relational operators require numeric operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitEqualityExpr(self, ctx):
        # Funkce pro visit porovnávacích výrazů (rovnost a nerovnost)

        # Získáme typy levého a pravého operandu (výrazu)
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        # Pro oba porovnávací operátory musí být oba operandy stejného typu
        # A typ musí být jeden z: int, float, string
        if left_type == right_type and left_type in [Type.INT, Type.FLOAT, Type.STRING]:
            return Type.BOOL
        
        # Pokud se typy operand nerovají, checkneme jestli to není float a int - to je povolené
        # Např. 10 == 10.0 nebo 10.0 == 10
        if (left_type == Type.INT and right_type == Type.FLOAT) or (left_type == Type.FLOAT and right_type == Type.INT):
            return Type.BOOL
        
        return self.add_error(ctx, f"Equality operators cannot compare {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitAndExpr(self, ctx):
        # Funkce pro visit logického AND výrazu (&&).

        # Získáme text levého a pravého operandu (výrazu)
        left_text = ctx.expression(0).getText()
        right_text = ctx.expression(1).getText()
        
        # Kontrola, jestli jsou oba operandy boolean literály
        # Např. true && false nebo false && true
        if self.is_boolean_literal(left_text) and self.is_boolean_literal(right_text):
            return Type.BOOL
        
        # Jestli je levý operand boolean literal:
        if self.is_boolean_literal(left_text):
            # Navštívíme pravý operand a zkontrolujeme jeho typ
            right_type = self.visit(ctx.expression(1))
            if right_type == Type.BOOL:
                return Type.BOOL
            elif right_type == Type.ERROR:
                return Type.ERROR
            else:
                return self.add_error(ctx, f"Logical AND operator requires boolean operands, but got bool and {Type.to_string(right_type)}")
        
        # To stejné, ale opak pro pravý operand
        if self.is_boolean_literal(right_text):
            left_type = self.visit(ctx.expression(0))
            if left_type == Type.BOOL:
                return Type.BOOL
            elif left_type == Type.ERROR:
                return Type.ERROR
            else:
                return self.add_error(ctx, f"Logical AND operator requires boolean operands, but got {Type.to_string(left_type)} and bool")
        
        # Získáme typy levého a pravého operandu (výrazu)
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        # Obě operandy musí být boolean
        if left_type == Type.BOOL and right_type == Type.BOOL:
            return Type.BOOL
        
        return self.add_error(ctx, f"Logical AND operator requires boolean operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitOrExpr(self, ctx):
        # Funkce pro visit logického OR výrazu (||).

        left_text = ctx.expression(0).getText()
        right_text = ctx.expression(1).getText()
        
        if self.is_boolean_literal(left_text) and self.is_boolean_literal(right_text):
            return Type.BOOL
        
        if self.is_boolean_literal(left_text):
            right_type = self.visit(ctx.expression(1))
            if right_type == Type.BOOL:
                return Type.BOOL
            elif right_type == Type.ERROR:
                return Type.ERROR
            else:
                return self.add_error(ctx, f"Logical OR operator requires boolean operands, but got bool and {Type.to_string(right_type)}")
        
        if self.is_boolean_literal(right_text):
            left_type = self.visit(ctx.expression(0))
            if left_type == Type.BOOL:
                return Type.BOOL
            elif left_type == Type.ERROR:
                return Type.ERROR
            else:
                return self.add_error(ctx, f"Logical OR operator requires boolean operands, but got {Type.to_string(left_type)} and bool")
        
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type == Type.ERROR or right_type == Type.ERROR:
            return Type.ERROR
        
        if left_type == Type.BOOL and right_type == Type.BOOL:
            return Type.BOOL
        
        return self.add_error(ctx, f"Logical OR operator requires boolean operands, but got {Type.to_string(left_type)} and {Type.to_string(right_type)}")
    
    def visitAssignmentExpr(self, ctx):
        # Funkce pro visit přiřazení výrazu (=).

        # Získáme název proměnné
        var_name = ctx.ID().getText()

        # Kontrolujeme, zda je proměnná deklarována, pokud ne, přidáme chybu do seznamu chyb
        if var_name not in self.variables:
            return self.add_error(ctx, f"Variable '{var_name}' is not declared")

        # Získáme typ proměnné
        var_type = self.variables[var_name]
        
        # Speciální case pro boolean literály v přímém přiřazení
        
        expr_text = ctx.expression().getText()
        if var_type == Type.BOOL and (expr_text == "true" or expr_text == "false"):
            return Type.BOOL
        
        # Získáme typ výrazu na pravé straně přiřazení
        expr_type = self.visit(ctx.expression())
        
        if expr_type == Type.ERROR:
            return Type.ERROR
        
        # Kontrola, jestli se typ výrazu shoduje s typem proměnné
        # Speciální případ: int může být přiřazen float (automatická konverze typu)
        if expr_type == var_type:
            return var_type
        elif var_type == Type.FLOAT and expr_type == Type.INT: #  Jestli je proměnná float a výraz je int, tak vrátíme float
            return Type.FLOAT
        
        return self.add_error(ctx, f"Cannot assign {Type.to_string(expr_type)} to {Type.to_string(var_type)}")
