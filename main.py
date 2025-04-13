#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
from antlr4 import *
from src.parser.LanguageLexer import LanguageLexer
from src.parser.LanguageParser import LanguageParser
from src.type_checker.type_checker import TypeChecker
from src.code_generator.code_generator import CodeGenerator
from src.interpreter.interpreter import Interpreter

def compile_file(input_path, output_path=None):
    try:
        print(f"Compiling {input_path}...")
        
        input_stream = FileStream(input_path, encoding='utf-8')
        
        lexer = LanguageLexer(input_stream)
        
        token_stream = CommonTokenStream(lexer)
        
        parser = LanguageParser(token_stream)
        
        parse_tree = parser.program()
        
        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"Syntax errors found in {input_path}")
            return False
        
        type_checker = TypeChecker()
        type_checker.visit(parse_tree)
        
        if type_checker.has_errors():
            print(f"Type errors found in {input_path}:")
            type_checker.report_errors()
            return False
        
        code_generator = CodeGenerator()
        try:
            code_generator.visit(parse_tree)
        except Exception as e:
            print(f"Error during code generation: {e}")
            print("Partial generated code:")
            code_generator.print_generated_code()
            return False
        
        generated_code = code_generator.get_generated_code()
        
        if output_path is None:
            input_dir = os.path.dirname(input_path)
            input_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(input_dir, f"generated_{input_name}.txt")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        
        print(f"Successfully compiled {input_path} to {output_path}")
        return True
    
    except Exception as e:
        print(f"Error compiling {input_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file> [<output_file>]")
        return
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    success = compile_file(input_path, output_path)
    
    if success:
        print(f"--- Running Interpreter on {output_path} ---")
        interpreter = Interpreter()
        interpreter.load_instructions(output_path)
        interpreter.run()
        print("--- Interpreter finished ---")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
