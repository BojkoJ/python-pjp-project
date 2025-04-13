#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Interpreter:
    # Třída Interpreter pro provádění instrukcí na zásobníkové bázi

    def __init__(self):
        # Inicializuje stav interpretru
        self.stack = []
        self.memory = {}
        self.instructions = []
        self.labels = {}
        self.pc = 0 # Counter programu (program counter)

    def load_instructions(self, filepath):
        # Načítá instrukce ze souboru a zpracovává je
        self.instructions = []
        self.labels = {}

        try:
            with open(filepath, 'r') as f:
                for index, line in enumerate(f):
                    line = line.strip()
                    if not line: # Přeskočit prázdné řádky
                        continue
                    
                    parts = line.split(None, 2) # Rozdělit na opcode a argumenty, opcode je první slovo a argumenty zbytek
                    opcode = parts[0].lower() # Převeďte opcode na malá písmena pro konzistenci
                    args = parts[1:]
                    
                    # Uložit instrukci do seznamu instrukcí
                    parsed_instruction = [opcode] + args
                    self.instructions.append(parsed_instruction)
                    
                    # Pokud je opcode 'label', zpracovat jako label
                    if opcode == 'label':
                        # Zpracovat label, očekáváme formát 'label <number>'
                        if len(args) == 1 and args[0].isdigit():
                            label_num = int(args[0])

                            # Check jestli label_num je již v self.labels (duplikát)
                            if label_num in self.labels:
                                print(f"Warning: Duplicate label {label_num} found at line {index + 1}", file=sys.stderr)

                            self.labels[label_num] = index
                        else:
                            print(f"Warning: Invalid label format at line {index + 1}: {line}", file=sys.stderr)
                            
        except FileNotFoundError:
            print(f"Error: Instruction file not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading instruction file {filepath}: {e}", file=sys.stderr)
            sys.exit(1)

    def run(self):
        # Spustí vykonávání instrukcí
        self.pc = 0

        while 0 <= self.pc < len(self.instructions): # Cyklus se bude provádět, dokud je pc v rozsahu instrukcí
            instruction = self.instructions[self.pc]

            # Aktuální pc je uložen před potenciálním skokem
            current_pc = self.pc 
            
            # Zpracování instrukce
            self.pc += 1 
            try:
                self.execute_instruction(instruction)
            except IndexError: # Stack underflow
                print(f"Runtime Error: Stack underflow at instruction {current_pc}: {instruction}", file=sys.stderr)
                sys.exit(1)
            except KeyError as e: # Undefined variable/label
                print(f"Runtime Error: Unknown variable or label {e} at instruction {current_pc}: {instruction}", file=sys.stderr)
                sys.exit(1)
            except Exception as e: # Jiné chyby
                print(f"Runtime Error at instruction {current_pc} ({instruction}): {e}", file=sys.stderr)
                sys.exit(1)

    def execute_instruction(self, instruction):
        # Zpracovává jednotlivé instrukce
        opcode = instruction[0] # opcode je první prvek instrukce
        args = instruction[1:] # zbytek jsou argumenty

        # Instrukce push:
        if opcode == 'push':
            # Očekáváme formát 'PUSH <type_code> <value>'
            if len(args) != 2:
                raise ValueError(f"Invalid PUSH format: {instruction}")
            
            # args[0] je type_code, args[1] je hodnota
            type_code = args[0]
            value_str = args[1]

            value = None
            
            if type_code == 'I': # Integer
                value = int(value_str)
            elif type_code == 'F': # Float
                value = float(value_str)
            elif type_code == 'B': # Boolean
                if value_str.lower() == 'true': 
                    value = True
                elif value_str.lower() == 'false':
                    value = False
                else:
                    raise ValueError(f"Invalid boolean literal for PUSH B: {value_str}")
            elif type_code == 'S': # String
                # Pokud jsou uvozovky, odstraníme je
                if len(value_str) >= 2 and value_str.startswith('"') and value_str.endswith('"'):
                    value = value_str[1:-1]
                else:
                    value = value_str # Ponecháme jako je, bez uvozovek
            else:
                raise ValueError(f"Unknown type code for PUSH: {type_code}")
            self.stack.append(value)
        
        # Instrukce pop:
        elif opcode == 'pop':
            if not self.stack:
                raise IndexError("POP on empty stack")
            self.stack.pop()

        # Instrukce load:
        elif opcode == 'load':
            # Očekáváme formát 'LOAD <var_name>'
            if len(args) != 1:
                raise ValueError(f"Invalid LOAD format: {instruction}")
            
            var_name = args[0]
            
            # Zkontrolujeme, zda je proměnná v paměti
            if var_name not in self.memory:
                 raise KeyError(var_name)
        
            # Pokud je v paměti, tak ji načteme na zásobník
            self.stack.append(self.memory[var_name])
        
        # Instrukce save:
        elif opcode == 'save':
            # Očekáváme formát 'SAVE <var_name>'
            if len(args) != 1:
                raise ValueError(f"Invalid SAVE format: {instruction}")
            
            # Zkontrolujeme, zda je zásobník prázdný
            if not self.stack:
                raise IndexError("SAVE on empty stack")
            
            # Pokud není prázdný, tak uložíme hodnotu z vrcholu zásobníku do paměti
            var_name = args[0]
            value = self.stack.pop()
            self.memory[var_name] = value

        # add, sub, mul, div - aritmetické operace
        elif opcode in ('add', 'sub', 'mul', 'div'):
            # Očekává se formát s jedným argumentem: 'ADD <type_code>'
            if len(args) != 1:
                 raise ValueError(f"Invalid format for {opcode.upper()}: {instruction}")
            
            type_code = args[0]
            
            # Pokud type_code není I nebo F, raise ValueError - jen FLOAT a INT
            if type_code not in ('I', 'F'):
                 raise ValueError(f"Invalid type code for {opcode.upper()}: {type_code}")
            
            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError(f"{opcode.upper()} requires two operands on the stack")
            
            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            # Základní kontrola typů (Python zvládá propagaci int/float)
            if type_code == 'I' and not (isinstance(op1, int) and isinstance(op2, int)): # INT
                 raise TypeError(f"{opcode.upper()} I requires integer operands, got {type(op1)}, {type(op2)}")
            if type_code == 'F' and not (isinstance(op1, (int, float)) and isinstance(op2, (int, float))): # FLOAT
                 raise TypeError(f"{opcode.upper()} F requires numeric operands, got {type(op1)}, {type(op2)}")

            # Provádíme operaci podle opcode
            result = None
            if opcode == 'add':
                result = op1 + op2
            elif opcode == 'sub':
                result = op1 - op2
            elif opcode == 'mul':
                result = op1 * op2
            elif opcode == 'div':
                if op2 == 0: # Dělení nulou
                    raise ZeroDivisionError("Division by zero")
                # Pokud je typ FLOAT, použijeme dělení s plovoucí desetinnou čárkou, jinak celočíselné dělení 
                result = op1 / op2 if type_code == 'F' else op1 // op2 

            # Výsledek vložíme zpět na zásobník
            self.stack.append(result)

        # Instrukce mod
        elif opcode == 'mod':
            if len(args) != 0: # MOD nebere žádné argumenty
                 raise ValueError(f"Invalid format for MOD: {instruction}")
            
            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError("MOD requires two operands on the stack")

            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            # Kontrola typů, jestli obě hodnoty jsou celé čísla
            if not (isinstance(op1, int) and isinstance(op2, int)):
                 raise TypeError(f"MOD requires integer operands, got {type(op1)}, {type(op2)}")
            
            if op2 == 0:
                raise ZeroDivisionError("Modulo by zero")
            
            # Vytvoříme výsledek modulu a vložíme ho zpět na zásobník
            result = op1 % op2
            self.stack.append(result)
        
        # Instrukce uminus
        elif opcode == 'uminus':
            # Očekáváme formát s jedním argumentem: 'UMINUS <type_code>'
            if len(args) != 1:
                 raise ValueError(f"Invalid format for UMINUS: {instruction}")
            
            # type_code je první argument, (typ operandu - float/int)
            type_code = args[0]
            # Kontrola jestance, zda je type_code platný (I nebo F)
            if type_code not in ('I', 'F'):
                 raise ValueError(f"Invalid type code for UMINUS: {type_code}")

            if not self.stack:
                raise IndexError("UMINUS requires one operand on the stack")
            
            # Popneme hodnotu ze zásobníku
            op1 = self.stack.pop()

            if type_code == 'I' and not isinstance(op1, int): # INT
                 raise TypeError(f"UMINUS I requires an integer operand, got {type(op1)}")
            if type_code == 'F' and not isinstance(op1, (int, float)): # FLOAT
                 raise TypeError(f"UMINUS F requires a numeric operand, got {type(op1)}")

            # Odčítáme hodnotu od nuly (negace)
            self.stack.append(-op1)

        # Instrukce concat - spojení dvou řetězců
        elif opcode == 'concat':
            if len(args) != 0: # CONCAT nebere žádné argumenty
                 raise ValueError(f"Invalid format for CONCAT: {instruction}")
            
            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError("CONCAT requires two operands on the stack")
            
            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            # Kontrola, že obě hodnoty jsou řetězce
            if not (isinstance(op1, str) and isinstance(op2, str)):
                 raise TypeError(f"CONCAT requires string operands, got {type(op1)}, {type(op2)}")
            
            # Spojíme řetězce a vložíme výsledek zpět na zásobník
            self.stack.append(op1 + op2)

        # Instrukce Itof - konverze int na float
        elif opcode == 'itof':
            
            if not self.stack:
                raise IndexError("ITOF requires one operand on the stack")
            
            # Popneme hodnotu ze zásobníku
            op1 = self.stack.pop()
            
            # Kontrola, že hodnota je celé číslo
            if not isinstance(op1, int):
                raise TypeError(f"ITOF requires an integer operand, got {type(op1)}")
            
            # Provedeme konverzi na float a vložíme výsledek zpět na zásobník
            self.stack.append(float(op1))

        # Instrukce eq, lt, gt - porovnání
        elif opcode in ('eq', 'lt', 'gt'):
            ## Očekáváme formát s jedním argumentem: 'EQ <type_code>'
            if len(args) != 1:
                 raise ValueError(f"Invalid format for {opcode.upper()}: {instruction}")
            
            # Získáme type_code z argumentů
            type_code = args[0]
            
            if type_code not in ('I', 'F', 'S'): # Kontrola platnosti type_code
                 raise ValueError(f"Invalid type code for {opcode.upper()}: {type_code}")
            
            # STRING může dělat jen EQ
            if opcode != 'eq' and type_code == 'S':
                 raise ValueError(f"{opcode.upper()} S is not supported, only EQ S")

            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError(f"{opcode.upper()} requires two operands on the stack")
            
            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            result = None
            try:
                # INT:
                if type_code == 'I':
                    # Pokud operandy nejsou int, raise TypeError
                    if not (isinstance(op1, int) and isinstance(op2, int)):
                        raise TypeError(f"{opcode.upper()} I requires integer operands, got {type(op1)}, {type(op2)}")
                    
                    # Provádíme operaci podle opcode
                    if opcode == 'eq': result = op1 == op2
                    elif opcode == 'lt': result = op1 < op2
                    elif opcode == 'gt': result = op1 > op2
                # FLOAT:
                elif type_code == 'F':
                    # Provedeme převod na float, pokud je operand int
                    op1_f = float(op1) if isinstance(op1, int) else op1
                    op2_f = float(op2) if isinstance(op2, int) else op2

                    # Kontrola, že oba operandy jsou float
                    if not (isinstance(op1_f, float) and isinstance(op2_f, float)):
                         raise TypeError(f"{opcode.upper()} F requires numeric operands, got {type(op1)}, {type(op2)}")
                    
                    # Provádíme operaci podle opcode
                    if opcode == 'eq': result = op1_f == op2_f
                    elif opcode == 'lt': result = op1_f < op2_f
                    elif opcode == 'gt': result = op1_f > op2_f
                # STRING:
                elif type_code == 'S': 
                    # Kontrola, že oba operandy jsou řetězce
                    if not (isinstance(op1, str) and isinstance(op2, str)):
                         raise TypeError(f"EQ S requires string operands, got {type(op1)}, {type(op2)}")
                    
                    # Provádíme operaci EQ
                    result = op1 == op2
            except Exception as e:
                 raise TypeError(f"Error during {opcode.upper()} {type_code} comparison: {e}")

            # Vložení výsledku zpět na zásobník
            self.stack.append(result)

        # Instrukce not - negace
        elif opcode == 'not':
            # Očekáváme formát s jedním argumentem: 'NOT <type_code>'
            if len(args) != 0:
                 raise ValueError(f"Invalid format for NOT: {instruction}")
            
            if not self.stack:
                raise IndexError("NOT requires one operand on the stack")

            # Popneme hodnotu ze zásobníku            
            op1 = self.stack.pop()
            
            # Kontrola, že hodnota je boolean
            if not isinstance(op1, bool):
                raise TypeError(f"NOT requires a boolean operand, got {type(op1)}")
            
            # výpočet negace a vložíme výsledek zpět na zásobník
            self.stack.append(not op1)

        # Instrukce AND
        elif opcode == 'and':
            if len(args) != 0:
                 raise ValueError(f"Invalid format for AND: {instruction}")

            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError("AND requires two operands on the stack")

            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            # Kontrola, že obě hodnoty jsou boolean
            if not (isinstance(op1, bool) and isinstance(op2, bool)):
                 raise TypeError(f"AND requires boolean operands, got {type(op1)}, {type(op2)}")

            # Provedeme logickou operaci AND a vložíme výsledek zpět na zásobník
            self.stack.append(op1 and op2)

        # Instrukce OR
        elif opcode == 'or':
            if len(args) != 0:
                 raise ValueError(f"Invalid format for OR: {instruction}")
            
            # Zkontrolujeme, zda máme na zásobníku alespoň 2 hodnoty
            if len(self.stack) < 2:
                raise IndexError("OR requires two operands on the stack")
            
            # Popneme dvě hodnoty ze zásobníku
            op2 = self.stack.pop()
            op1 = self.stack.pop()

            # Kontrola, že obě hodnoty jsou boolean
            if not (isinstance(op1, bool) and isinstance(op2, bool)):
                 raise TypeError(f"OR requires boolean operands, got {type(op1)}, {type(op2)}")
            
            # Provedeme logickou operaci OR a vložíme výsledek zpět na zásobník
            self.stack.append(op1 or op2)

        # Instrukce label
        elif opcode == 'label':
            # Labely jsou již zpracovány při načítání instrukcí, takže nic neděláme
            pass 
            
        # Instrukce jmp (jump)
        elif opcode == 'jmp':
            # Očekáváme formát 'JMP <label_num>'
            # args[0] je label_num, který je číslo
            # Kontrola, že args[0] je číslo
            if len(args) != 1 or not args[0].isdigit():
                raise ValueError(f"Invalid JMP format: {instruction}")
            
            label_num = int(args[0])
            
            # Kontrola, že label_num je v self.labels (existuje)
            if label_num not in self.labels:
                raise KeyError(f"Undefined label for JMP: {label_num}")
            
            # Pokud je label_num v self.labels, nastavíme pc na index labelu
            self.pc = self.labels[label_num] 

        # Instrukce fjmp (false jump)
        elif opcode == 'fjmp':
            if len(args) != 1 or not args[0].isdigit():
                raise ValueError(f"Invalid FJMP format: {instruction}")
            
            if not self.stack:
                raise IndexError("FJMP requires one boolean operand on the stack")
            
            condition = self.stack.pop()
            
            if not isinstance(condition, bool):
                raise TypeError(f"FJMP requires a boolean operand, got {type(condition)}")
                
            if not condition: # If condition is False
                label_num = int(args[0])
                
                if label_num not in self.labels:
                    raise KeyError(f"Undefined label for FJMP: {label_num}")
                # Pokud je label_num v self.labels, nastavíme pc na index labelu
                self.pc = self.labels[label_num]

        # Instrukce print
        elif opcode == 'print':
            # Očekáváme formát 'PRINT <num_values>'
            # args[0] je počet hodnot k vytištění, který je číslo
            if len(args) != 1 or not args[0].isdigit():
                raise ValueError(f"Invalid PRINT format: {instruction}")
            
            num_values = int(args[0])
            
            # Kontrola, že num_values je kladné číslo
            if num_values < 0:
                 raise ValueError("Cannot PRINT negative number of values")
            
            # Kontrola, že máme na zásobníku alespoň num_values hodnot
            if len(self.stack) < num_values:
                raise IndexError(f"PRINT {num_values} requires {num_values} operands on the stack, found {len(self.stack)}")
            
            # Vytvoříme seznam pro hodnoty k vytištění
            values_to_print = []
            
            # Popneme num_values hodnot ze zásobníku
            for _ in range(num_values):
                values_to_print.append(self.stack.pop())
            
            # Vypíšeme hodnoty v opačném pořadí, aby odpovídaly pořadí na zásobníku
            output = []
            for val in reversed(values_to_print):
                # Pokud je hodnota boolean, převedeme ji na lowercase string
                if isinstance(val, bool):
                    output.append(str(val).lower())
                else:
                    output.append(str(val))
            
            print("".join(output))

        # Instrukce read
        elif opcode == 'read':
            # Očekáváme formát 'READ <type_code>'
            if len(args) != 1:
                raise ValueError(f"Invalid READ format: {instruction}")
            
            # Typový kód je první argument
            type_code = args[0]
            
            try:
                line = input() # Načteme řádek z konzole

                value = None
                
                # Zpracování podle type_code
                if type_code == 'I': # Integer
                    value = int(line)
                elif type_code == 'F': # Float
                    value = float(line)
                elif type_code == 'B': # Boolean
                    if line.lower() == 'true':
                        value = True
                    elif line.lower() == 'false':
                        value = False
                    else:
                        raise ValueError(f"Invalid boolean input: {line}")
                elif type_code == 'S': # String
                    value = line
                else:
                    raise ValueError(f"Unknown type code for READ: {type_code}")
                self.stack.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid input for READ {type_code}: {e}")
            except EOFError:
                raise EOFError("End of input reached during READ")
        else:
            print(f"Warning: Unknown opcode '{opcode}' encountered.", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <instruction_file>")
        sys.exit(1)

    instruction_file = sys.argv[1]
    interpreter = Interpreter()
    interpreter.load_instructions(instruction_file)
    interpreter.run()
