#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hlavní skript pro zpracování zdrojového kódu
# Tento skript provádí syntaktickou analýzu a kontrolu typů.

import sys
import antlr4
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from src.parser.LanguageLexer import LanguageLexer
from src.parser.LanguageParser import LanguageParser

class SyntaxErrorListener(ErrorListener):
    # Třída pro zpracování syntaktických chyb
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.syntax_errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Funkce pro zpracování syntaktických chyb
        # Argumenty:
        #    recognizer: Rozpoznávač, kde došlo k chybě
        #    offendingSymbol: Token, který způsobil chybu
        #    line: Číslo řádku, kde došlo k chybě
        #    column: Číslo sloupce, kde došlo k chybě
        #    msg: Chybová zpráva
        #    e: Výjimka, která způsobila chybu (pokud existuje)

        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.syntax_errors.append(error_message)
        
    def has_errors(self):
        # Funkce pro kontrolu, zda byly nalezeny syntaktické chyby
        return len(self.syntax_errors) > 0
    
    def report_errors(self):
        # Funkce pro vypsání všech nalezených syntaktických chyb
        for error in self.syntax_errors:
            print(error)

def parse_file(file_path):
    # Funkce pro syntaktickou analýzu zdrojového souboru
    # Vrací parse tree, pokud nebyly nalezeny žádné syntaktické chyby, jinak None
    try:
        # Čtení vstupního souboru
        input_stream = InputStream(open(file_path, 'r').read())
        
        # Vytvoření lexikálního analyzátoru (lexer)
        lexer = LanguageLexer(input_stream)
        
        # Vytvoření tokenového proudu z lexeru
        token_stream = CommonTokenStream(lexer)
        
        # Vytvoření syntaktického analyzátoru (parser)
        parser = LanguageParser(token_stream)
        
        # Vytvoření a nastavení vlastního posluchače chyb
        error_listener = SyntaxErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        # Vytvoření parse tree
        parse_tree = parser.program()
        
        # Kontrola, zda byly nalezeny syntaktické chyby
        if error_listener.has_errors():
            error_listener.report_errors()
            return None
        
        # Vrátí parse tree, pokud nebyly nalezeny žádné chyby
        return parse_tree
    
    except Exception as e:
        print(f"Error parsing file '{file_path}': {str(e)}")
        return None

def main():
    # Hlavní funkce pro zpracování zdrojového kódu

    # Kontrola, zda byl zadán název souboru
    if len(sys.argv) < 2:
        print("Usage: python parser_main.py <source_file>")
        return 1
    
    file_path = sys.argv[1]
    parse_tree = parse_file(file_path)

    # Kontrola, zda byl parse tree úspěšně vytvořen    
    if parse_tree is None:
        print("Parsing failed due to syntax errors.")
        return 1
    
    print("Parsing successful!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
