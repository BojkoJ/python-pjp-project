#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Inicializace a utility funkce pro kontrolu typů

from antlr4 import *
from src.parser.LanguageLexer import LanguageLexer
from src.parser.LanguageParser import LanguageParser
from src.type_checker.type_checker import TypeChecker

def check_types(parse_tree):
    # Funkce pro provádění kontroly typů na parse tree
    # Vrací instance TypeChecker s výsledky
    type_checker = TypeChecker()
    type_checker.visit(parse_tree)
    return type_checker

def check_types_file(file_path, parse_tree):
    # Funkce pro provádění kontroly typů na parse tree
    # Vrací True, pokud nebyly nalezeny žádné chyby typu, jinak False

    if parse_tree is None:
        print(f"Error: No parse tree provided for file {file_path}")
        return False
    
    print(f"Type checking file: {file_path}")
    type_checker = TypeChecker()
    type_checker.visit(parse_tree)
    
    if type_checker.has_errors():
        print(f"Type checking failed for file {file_path}")
        type_checker.report_errors()
        return False
    
    print(f"Type checking passed for file {file_path}")
    return True
