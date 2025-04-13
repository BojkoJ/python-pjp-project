#!/usr/bin/env python
# -*- coding: utf-8 -*-

from antlr4 import *
from src.parser.LanguageParser import LanguageParser
from src.parser.LanguageVisitor import LanguageVisitor
from src.type_checker.type_checker import Type

class CodeGenerator(LanguageVisitor):
    # Třída pro generování kódu z parse tree
    def __init__(self):
        self.code = []
        self.variables = {}
        self.label_counter = 0
    
    def get_new_label(self):
        # Funkce pro generování nového unikátního čísla pro label
        label = self.label_counter
        self.label_counter += 1
        return label
    
    def add_instruction(self, instruction):
        # Funkce pro přidání instrukce do generovaného kódu
        self.code.append(instruction)
    
    def get_generated_code(self):
        # Funkce pro získání generovaného kódu jako řetězec
        return '\n'.join(self.code)
    
    def type_to_code(self, type_value):
        # Funkce pro převod typu na kód I, S, B, F
        if type_value == 'int' or type_value == Type.INT:
            return 'I'
        elif type_value == 'float' or type_value == Type.FLOAT:
            return 'F'
        elif type_value == 'bool' or type_value == Type.BOOL:
            return 'B'
        elif type_value == 'string' or type_value == Type.STRING:
            return 'S'
        else:
            return 'ERROR'
    
    def visitProgram(self, ctx):
        # Funkce pro zpracování celého programu
        for statement in ctx.statement():
            self.visit(statement)
        
        return None
    
    def visitEmptyStatement(self, ctx):
        # Funkce pro zpracování prázdného příkazu
        return None
    
    def _string_to_type(self, type_name):
        # Pomocná funkce pro převod názvu typu na enum
        if type_name == 'int':
            return Type.INT
        elif type_name == 'float':
            return Type.FLOAT
        elif type_name == 'bool':
            return Type.BOOL
        elif type_name == 'string':
            return Type.STRING
        else:
            raise ValueError(f"Unknown type name: {type_name}")

    def visitDeclarationStatement(self, ctx):
        """
        Visit a variable declaration statement.

        Args:
            ctx: The declaration statement context

        Returns:
            None
        """
        # Funkce pro zpracování příkazu pro deklaraci proměnné

        # Získáme typ proměnné
        type_name = ctx.type_().getText()
        var_type_enum = self._string_to_type(type_name) # Převod na enum pomocí _string_to_type pomocníka

        # Získáme jména proměnných
        variables = ctx.variableList().ID()

        for var in variables:
            var_name = var.getText()
            self.variables[var_name] = var_type_enum 

            if var_type_enum == Type.INT:
                self.add_instruction(f"push I 0")
            elif var_type_enum == Type.FLOAT:
                self.add_instruction(f"push F 0.0")
            elif var_type_enum == Type.BOOL:
                self.add_instruction(f"push B false")
            elif var_type_enum == Type.STRING:
                self.add_instruction('push S ""')

            self.add_instruction(f"save {var_name}")

        return None
    
    def visitExpressionStatement(self, ctx):
        # Funkce pro zpracování příkazu pro výraz

        # Zpracujeme výraz (což způsobí, že se hodnota vloží na zásobník)
        self.visit(ctx.expression())
        
        # Popnutí hodnoty ze zásobníku
        self.add_instruction("pop")
        return None
    
    def visitReadStatement(self, ctx):
        # Funkce pro zpracování příkazu pro čtení hodnoty do proměnné

        # Získání všech jmen proměnných
        variables = ctx.variableList().ID()

        for var in variables:
            var_name = var.getText()
            var_type_enum = self.variables[var_name] 

            self.add_instruction(f"read {self.type_to_code(var_type_enum)}")
            self.add_instruction(f"save {var_name}")

        return None    
    def visitWriteStatement(self, ctx):
        # Funkce pro visit statementu pro zápis proměnné. (write)

        # Získáme všechny výrazy k zápisu
        expressions = ctx.expressionList().expression()
        num_expressions = len(expressions)

        # zpracujeme každý výraz, abychom jeho hodnotu vložili na zásobník
        for expr in expressions:
            self.visit(expr)

        # Vytiskneme všechny hodnoty ze zásobníku
        if num_expressions > 0:
            self.add_instruction(f"print {num_expressions}")

        return None

    def visitBlockStatement(self, ctx):
        # Funkce pro visit bloku.

        # zpracujeme všechny příkazy v bloku
        for statement in ctx.statement():
            self.visit(statement)

        return None

    def visitIfStatement(self, ctx):
        # Funkce pro visit if statementu.

        # Získáme nové návěští pro else blok a konec if statementu
        else_label = self.get_new_label()
        end_label = self.get_new_label()

        # zpracujeme podmínku
        self.visit(ctx.expression())

        # Pokud je podmínka false, skočíme na else návěští
        self.add_instruction(f"fjmp {else_label}")

        # zpracujeme 'then' příkaz
        self.visit(ctx.statement(0))

        # Skočíme na konec if statementu
        self.add_instruction(f"jmp {end_label}")

        # Přidáme else návěští
        self.add_instruction(f"label {else_label}")

        # Pokud existuje 'else' příkaz, zpracujeme ho
        if len(ctx.statement()) > 1:
            self.visit(ctx.statement(1))

        # Přidáme koncové návěští
        self.add_instruction(f"label {end_label}")

        return None

    def visitWhileStatement(self, ctx):
        # Funkce pro visit while statementu.

        # Získáme nové návěští pro začátek a konec cyklu
        start_label = self.get_new_label()
        end_label = self.get_new_label()

        # Přidáme počáteční návěští
        self.add_instruction(f"label {start_label}")

        # zpracujeme podmínku
        self.visit(ctx.expression())

        # Pokud je podmínka false, skočíme na koncové návěští
        self.add_instruction(f"fjmp {end_label}")

        # zpracujeme tělo příkazu
        self.visit(ctx.statement())

        # Skočíme zpět na počáteční návěští
        self.add_instruction(f"jmp {start_label}")

        # Přidáme koncové návěští
        self.add_instruction(f"label {end_label}")

        return None

    def visitVariableExpr(self, ctx):
        # Funkce pro visit výrazu proměnné.

        # Získáme název proměnné
        var_name = ctx.ID().getText()

        # Načteme hodnotu proměnné na zásobník
        # Zkontrolujeme, zda proměnná existuje (mělo by být zachyceno type checkerem, ale je to dobrá praxe)
        if var_name not in self.variables:
             raise NameError(f"Chyba generování kódu: Proměnná '{var_name}' použita, ale nedeklarována.")
        self.add_instruction(f"load {var_name}")

        # Vrátíme typ proměnné
        return self.variables[var_name]

    def visitLiteralExpr(self, ctx):
        # Funkce pro visit literálového výrazu.

        # Získáme literál
        literal = ctx.literal()

        # Zkontrolujeme, o jaký literál se jedná
        if literal.IntegerLiteral() is not None:
            value = literal.IntegerLiteral().getText()
            self.add_instruction(f"push I {value}")
            return Type.INT
        elif literal.FloatLiteral() is not None: 
            value = literal.FloatLiteral().getText()
            self.add_instruction(f"push F {value}")
            return Type.FLOAT
        elif literal.BooleanLiteral() is not None:
            value_text = literal.BooleanLiteral().getText()
            instruction_value = value_text.lower()
            if instruction_value not in ['true', 'false']:
                 raise ValueError(f"Interní chyba: Neočekávaný text boolean literálu '{value_text}'")
            self.add_instruction(f"push B {instruction_value}")
            return Type.BOOL
        elif literal.StringLiteral() is not None:
            value = literal.StringLiteral().getText()
            # Odstraníme okolní uvozovky z ANTLR tokenu
            if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
                processed_value = value[1:-1]
            else:
                # Nemělo by nastat s danou gramatikou, ale ošetříme defenzivně
                processed_value = value
            self.add_instruction(f'push S "{processed_value}"') # Použijeme processed_value
            return Type.STRING

        raise TypeError("Neznámý typ literálu nalezen v visitLiteralExpr")

    def visitParenExpr(self, ctx):
        # Funkce pro visit výrazu v závorkách.

        # Jen zpracujeme výraz uvnitř závorek
        return self.visit(ctx.expression())
    
    def visitUnaryMinusExpr(self, ctx):
        # Funkce pro visit unárního mínus výrazu.

        # zpracujeme operand
        operand_type = self.visit(ctx.expression())
        
        # Aplikujeme unární mínus
        if operand_type == Type.INT:
            self.add_instruction("uminus I")
            return Type.INT
        elif operand_type == Type.FLOAT:
            self.add_instruction("uminus F")
            return Type.FLOAT
        
        # Sem by se nikdy nemělo dostat, pokud byla provedena kontrola typů
        return Type.ERROR
    
    def visitNotExpr(self, ctx):
        # Funkce pro visit logického NOT výrazu.

        # zpracujeme operand
        self.visit(ctx.expression())
        
        # Aplikujeme logické NOT
        self.add_instruction("not")
        
        return Type.BOOL
    
    def visitMultiplicativeExpr(self, ctx):
        # Funkce pro visit multiplikativního výrazu (* / %).
        
        # zpracujeme levý a pravý operand
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()
        result_type = Type.ERROR

        # Ošetříme itof konverzi: konvertujeme pouze pokud je zásobník [F, I]
        if left_type == Type.FLOAT and right_type == Type.INT:
            self.add_instruction("itof")
            right_type = Type.FLOAT # Aktualizujeme efektivní typ
        # Předpokládáme, že op F implicitně zvládne případ [I, F]

        # Určíme operaci a výsledný typ
        if left_type == Type.FLOAT or right_type == Type.FLOAT:
            # Float operace
            result_type = Type.FLOAT
            if operator == '*': self.add_instruction("mul F")
            elif operator == '/': self.add_instruction("div F")
            elif operator == '%': 
                raise TypeError("Modulo operátor '%' není podporován pro floaty")
        elif left_type == Type.INT and right_type == Type.INT:
            # Integer operace
            result_type = Type.INT
            if operator == '*': self.add_instruction("mul I")
            elif operator == '/': self.add_instruction("div I")
            elif operator == '%': self.add_instruction("mod") # Modulo je jen 'mod' pro inty
        else:
            # Chyba typu (např. zapojen řetězec) - mělo by být zachyceno type checkerem
            pass # Necháme to na type checkeru

        return result_type
    
    def visitAdditiveExpr(self, ctx):
        # Funkce pro visit aditivního výrazu (+ - .).
        
        # zpracujeme levý a pravý operand
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()
        result_type = Type.ERROR

        if operator == '.': # Spojení řetězců
            if left_type == Type.STRING and right_type == Type.STRING:
                self.add_instruction("concat")
                result_type = Type.STRING
            else:
                # Chyba typu - mělo by být zachyceno type checkerem
                pass # Necháme to na type checkeru
        else: # '+' nebo '-'
            # Ošetříme itof konverzi: konvertujeme pouze pokud je zásobník [F, I]
            if left_type == Type.FLOAT and right_type == Type.INT:
                self.add_instruction("itof")
                right_type = Type.FLOAT # Aktualizujeme efektivní typ
            # Předpokládáme, že op F implicitně zvládne případ [I, F]

            # Určíme operaci a výsledný typ
            if left_type == Type.FLOAT or right_type == Type.FLOAT:
                # Float operace
                result_type = Type.FLOAT
                if operator == '+': self.add_instruction("add F")
                elif operator == '-': self.add_instruction("sub F")
            elif left_type == Type.INT and right_type == Type.INT:
                # Integer operace
                result_type = Type.INT
                if operator == '+': self.add_instruction("add I")
                elif operator == '-': self.add_instruction("sub I")
            else:
                # Chyba typu - mělo by být zachyceno type checkerem
                pass # Necháme to na type checkeru

        return result_type
    
    # Pomocná metoda pro určení typu výrazu bez generování kódu
    def _determine_expression_type(self, ctx):
        if isinstance(ctx, LanguageParser.LiteralExprContext):
            lit = ctx.literal()
            if lit.IntegerLiteral(): return Type.INT
            if lit.FloatLiteral(): return Type.FLOAT
            if lit.BooleanLiteral(): return Type.BOOL
            if lit.StringLiteral(): return Type.STRING
        elif isinstance(ctx, LanguageParser.VariableExprContext):
            var_name = ctx.ID().getText()
            # Použijeme uložené typy proměnných, pokud jsou k dispozici
            return self.variables.get(var_name, Type.ERROR)
        elif isinstance(ctx, LanguageParser.ParenExprContext):
            # Podíváme se dovnitř závorek
            return self._determine_expression_type(ctx.expression())
        elif isinstance(ctx, LanguageParser.UnaryMinusExprContext):
            # Typ závisí na typu operandu
            operand_type = self._determine_expression_type(ctx.expression())
            if operand_type in [Type.INT, Type.FLOAT]:
                return operand_type
        elif isinstance(ctx, LanguageParser.NotExprContext):
             return Type.BOOL # Výsledek 'not' je vždy bool

        print(f"Varování: Nelze určit typ pro uzel {ctx.getText()} bez plné návštěvy.")
        return Type.ERROR # Indikuje neznámý typ

    def visitRelationalExpr(self, ctx):
        # Funkce pro visit relačního výrazu (< >). Upraveno pro správné zpracování int/float povýšení.
        left_expr_ctx = ctx.expression(0)
        right_expr_ctx = ctx.expression(1)
        operator = ctx.getChild(1).getText()

        # zpracujeme levý operand jako první
        left_type = self.visit(left_expr_ctx)

        # Určíme typ pravého operandu *před* jeho návštěvou
        determined_right_type = self._determine_expression_type(right_expr_ctx)

        # --- Zpracování INT < FLOAT nebo INT > FLOAT ---
        itof_added_early = False
        if left_type == Type.INT and determined_right_type == Type.FLOAT:
            self.add_instruction("itof") # Přidáme itof *po* návštěvě levého, *před* návštěvou pravého
            left_type = Type.FLOAT # Aktualizujeme efektivní levý typ pro konečný výběr instrukce
            itof_added_early = True

        # zpracujeme pravý operand
        right_type = self.visit(right_expr_ctx)

        # --- Zpracování FLOAT < INT nebo FLOAT > INT ---
        # Pokud itof nebyl přidán dříve, zkontrolujeme, zda je potřeba nyní (zásobník: [F, I])
        if not itof_added_early and left_type == Type.FLOAT and right_type == Type.INT:
            self.add_instruction("itof") # Přidáme itof *po* návštěvě pravého (konvertuje int na vrcholu)
            right_type = Type.FLOAT # Aktualizujeme efektivní pravý typ

        # Určíme kód typu pro konečnou porovnávací instrukci
        comparison_type_code = 'ERROR'
        if left_type == Type.INT and right_type == Type.INT:
            comparison_type_code = 'I'
        elif left_type == Type.FLOAT and right_type == Type.FLOAT:
             # Toto pokrývá INT/FLOAT, FLOAT/INT (po itof) a FLOAT/FLOAT
            comparison_type_code = 'F'

        # Aplikujeme příslušný operátor
        if comparison_type_code == 'I':
            if operator == '<': self.add_instruction("lt I")
            elif operator == '>': self.add_instruction("gt I")
        elif comparison_type_code == 'F':
            if operator == '<': self.add_instruction("lt F")
            elif operator == '>': self.add_instruction("gt F")
        # else: Chyba typu nebo nepodporované porovnání, neděláme nic

        return Type.BOOL
    
    def visitEqualityExpr(self, ctx):
        # Funkce pro visit výrazu rovnosti (== !=).

        # zpracujeme levý a pravý operand
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))

        # Získáme operátor
        operator = ctx.getChild(1).getText()

        # Určíme typ pro porovnání a zpracujeme int/float povýšení
        comparison_type = Type.ERROR
        promoted_to_float = False

        # Zpracujeme povýšení typu pro porovnání
        if left_type == Type.FLOAT and right_type == Type.INT:
            # Zásobník: [F_val, I_val]. Konvertujeme I_val (vrchol) na F_val.
            self.add_instruction("itof")
            right_type = Type.FLOAT # Aktualizujeme typ po konverzi
            comparison_type = Type.FLOAT
            promoted_to_float = True
        elif left_type == Type.INT and right_type == Type.FLOAT:
            comparison_type = Type.FLOAT
            promoted_to_float = True # Indikuje potřebu float porovnání
            # Zde nepřidáváme žádnou instrukci, spoléháme na to, že eq F zvládne [I, F]
        elif left_type == Type.FLOAT and right_type == Type.FLOAT:
            comparison_type = Type.FLOAT
        elif left_type == Type.INT and right_type == Type.INT:
            comparison_type = Type.INT
        elif left_type == Type.STRING and right_type == Type.STRING:
            comparison_type = Type.STRING
        elif left_type == Type.BOOL and right_type == Type.BOOL:
            # Porovnání boolů je podporováno, ale není jasné, zda je to smysluplné.
            pass
        else:
            pass # comparison_type zůstává ERROR

        # Aplikujeme příslušný operátor na základě určeného typu porovnání
        instruction_added = False
        if comparison_type in [Type.INT, Type.FLOAT, Type.STRING]: # Přidáváme eq pouze pro I, F, S
            type_code = self.type_to_code(comparison_type)

            # Pokud jsme implicitně povýšili INT na FLOAT pro případ [I, F],
            # stále používáme 'eq F'.
            if promoted_to_float and comparison_type == Type.FLOAT:
                 type_code = 'F' # Zajistíme float porovnání

            self.add_instruction(f"eq {type_code}")
            instruction_added = True
        # else: comparison_type je ERROR nebo BOOL, žádná 'eq' instrukce není generována.

        # Zpracujeme != přidáním 'not' po 'eq'
        if operator == '!=':
            if comparison_type == Type.BOOL:
                 raise NotImplementedError("Boolean nerovnost '!=' nelze generovat, protože 'eq B' není definováno ve specifikaci sady instrukcí.")
            elif instruction_added:
                 # Pokud bylo přidáno eq I/F/S, negujeme výsledek.
                 self.add_instruction("not")

        # Výsledek porovnání je vždy bool
        return Type.BOOL

    def visitAndExpr(self, ctx):
        # Funkce pro visit logického AND výrazu.

        # zpracujeme levý a pravý operand
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        
        # Aplikujeme logické AND
        self.add_instruction("and")
        
        return Type.BOOL
    
    def visitOrExpr(self, ctx):
        # Funkce pro visit logického OR výrazu.

        # zpracujeme levý a pravý operand
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        
        # Aplikujeme logické OR
        self.add_instruction("or")
        
        return Type.BOOL
    
    def visitAssignmentExpr(self, ctx):
        # Funkce pro visit výrazu přiřazení.

        # Získáme název proměnné
        var_name = ctx.ID().getText()

        if not var_name or not isinstance(var_name, str):
             raise TypeError(f"Interní chyba: Neplatný název proměnné '{var_name}' v přiřazení")
        if var_name not in self.variables:
            raise NameError(f"Interní chyba: Proměnná '{var_name}' není deklarována před přiřazením")

        var_type = self.variables[var_name]

        # zpracujeme výraz na pravé straně JAKO PRVNÍ
        rhs_expr_ctx = ctx.expression()

        expr_type = None # Inicializujeme expr_type
        try:
            expr_type = self.visit(rhs_expr_ctx)
        except Exception as e:
            # Vytiskneme detailní informace o výjimce
            import traceback
            traceback.print_exc() # Vytiskneme celý traceback
            raise # Znovu vyvoláme výjimku
            
        # Zkontrolujeme kompatibilitu typů a provedeme konverze, pokud je potřeba
        if var_type == Type.FLOAT and expr_type == Type.INT:
            self.add_instruction("itof")
            expr_type = Type.FLOAT # Aktualizujeme efektivní typ po konverzi
        elif var_type != expr_type:
             if not (var_type == Type.FLOAT and expr_type == Type.INT): # Zkontrolujeme, zda již nebyl zpracován int->float
                pass

        # Uložíme hodnotu (která je na vrcholu zásobníku) do proměnné
        self.add_instruction(f"save {var_name}")

        # Načteme novou hodnotu proměnné zpět na zásobník (hodnota výrazu přiřazení)
        if not isinstance(var_name, str) or not var_name:
             raise TypeError(f"Interní chyba: var_name neplatný ('{var_name}') před instrukcí load v přiřazení")
        if var_name not in self.variables:
             raise NameError(f"Interní chyba: Proměnná '{var_name}' náhle nedeklarována před load v přiřazení?")
        self.add_instruction(f"load {var_name}")

        # Vrátíme typ proměnné (což je také typ výrazu)
        return var_type
    
    def print_generated_code(self):
        # Vytiskne generovaný kód do konzole pro účely ladění.
        print("Generovaný kód:")
        print(self.get_generated_code())
