# Language Compiler and Interpreter

A complete compiler and interpreter implementation for a custom programming language built with ANTLR4. This project demonstrates the full compilation pipeline from source code to execution, including lexical analysis, parsing, semantic analysis (type checking), code generation, and interpretation.

## 🎯 Overview

This project implements a compiler and interpreter for a statically-typed programming language that supports:

-   **Data Types**: `int`, `float`, `bool`, `string`
-   **Variables**: Declaration and assignment with type checking
-   **Expressions**: Arithmetic, logical, relational, and ternary operations
-   **Control Flow**: `if-else`, `while`, `for` loops
-   **I/O Operations**: `read` and `write` statements
-   **Type Safety**: Comprehensive type checking with automatic type promotion (int → float)

The compilation process produces stack-based bytecode instructions that are executed by a custom virtual machine interpreter.

## ✨ Features

### Language Features

-   ✅ **Static Type System** with type inference and checking
-   ✅ **Automatic Type Promotion** (int to float)
-   ✅ **String Concatenation** using the `.` operator
-   ✅ **Boolean Logic** with short-circuit evaluation
-   ✅ **Ternary Operator** (`condition ? true_expr : false_expr`)
-   ✅ **Multiple Assignment** (`a = b = c = 5`)
-   ✅ **Comments** (line comments with `//`)

### Compiler Pipeline

-   ✅ **Lexical Analysis** (ANTLR4 generated lexer)
-   ✅ **Syntax Analysis** (ANTLR4 generated parser)
-   ✅ **Semantic Analysis** (comprehensive type checker)
-   ✅ **Code Generation** (stack-based bytecode)
-   ✅ **Interpretation** (virtual machine execution)

## 📝 Language Syntax

### Data Types

```javascript
int number;      // Integer numbers
float decimal;   // Floating-point numbers
bool flag;       // Boolean values (true/false)
string text;     // String literals
```

### Variable Declaration and Assignment

```javascript
int x, y, z;           // Multiple variable declaration
x = 10;                // Simple assignment
y = x + 5;             // Expression assignment
a = b = c = 42;        // Multiple assignment
```

### Expressions

```javascript
// Arithmetic
result = 2 + 3 * 5;    // Operator precedence
value = 17 / 3;        // Integer division
remainder = 17 % 3;    // Modulo operation

// String concatenation
greeting = "Hello" . " World";

// Logical operations
isValid = (x > 0) && (y < 100);
canProceed = isReady || hasPermission;

// Relational operations
isEqual = (a == b);
isGreater = (x > y);

// Ternary operator
max = (a > b) ? a : b;
```

### Control Flow

```javascript
// If-else statement
if (condition) {
    write "True branch";
} else {
    write "False branch";
}

// While loop
while (counter < 10) {
    counter = counter + 1;
}

// For loop
for (i = 0; i < 5; i = i + 1) {
    write i;
}
```

### I/O Operations

```javascript
// Output
write "Hello, World!";
write "Value: ", variable;

// Input
read variable1, variable2;
```

## 📁 Project Structure

```
python-pjp-project/
├── main.py                    # Main compiler driver
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── grammar/
│   └── Language.g4           # ANTLR4 grammar definition
├── src/
│   ├── parser/               # Generated ANTLR4 parser
│   │   ├── LanguageLexer.py
│   │   ├── LanguageParser.py
│   │   ├── LanguageVisitor.py
│   │   └── parser_main.py    # Parser testing utilities
│   ├── type_checker/         # Semantic analysis
│   │   └── type_checker.py   # Type checking implementation
│   ├── code_generator/       # Code generation
│   │   └── code_generator.py # Bytecode generation
│   └── interpreter/          # Virtual machine
│       └── interpreter.py    # Stack-based interpreter
└── sample_inputs/            # Example programs
    ├── sample1/
    ├── sample2/
    ├── sample3/
    ├── sample4/
    ├── sample5/
    └── sample_err/           # Error test cases
```

## 🚀 Usage

### Basic Compilation and Execution

```bash
python main.py <input_file> [output_file]
```

**Example:**

```bash
python main.py sample_inputs/sample1/sample1.txt
```

This will:

1. Parse and type-check the source file
2. Generate bytecode instructions
3. Execute the program using the interpreter

### Individual Components

#### Parse Only

```bash
python src/parser/parser_main.py <source_file>
```

#### Run Interpreter on Bytecode

```bash
python src/interpreter/interpreter.py <bytecode_file>
```

## 💡 Examples

### Example 1: Basic Operations

**Input (`sample1.txt`):**

```javascript
write "<Constants>";
write "10: ",10;
write " 1.25: ", 1.25;

string s;
s = "Hello";
write "s: ", s;

int n;
n = -500;
write "n: ", n;

bool flag;
flag = true;
write "flag: ", flag;
```

**Generated Bytecode:**

```
push S "<Constants>"
print 1
push S "10: "
push I 10
print 2
push S " 1.25: "
push F 1.25
print 2
push S ""
save s
push S "Hello"
save s
push S "s: "
load s
print 2
```

**Output:**

```
<Constants>
10: 10
 1.25: 1.25
s: Hello
n: -500
flag: true
```

### Example 2: Control Flow

```javascript
int i;
for (i = 1; i <= 3; i = i + 1) {
    if (i % 2 == 0) {
        write i, " is even";
    } else {
        write i, " is odd";
    }
}
```

### Example 3: Type Promotion

```javascript
float result;
int x;
x = 10;
result = x + 3.14;  // Automatic int to float conversion
write "Result: ", result;
```

## 🏗️ Architecture

### Compilation Pipeline

1. **Lexical Analysis** (`LanguageLexer`)

    - Tokenizes source code
    - Handles keywords, operators, literals, identifiers

2. **Syntax Analysis** (`LanguageParser`)

    - Builds Abstract Syntax Tree (AST)
    - Grammar-driven parsing with ANTLR4

3. **Semantic Analysis** (`TypeChecker`)

    - Type checking and inference
    - Variable declaration validation
    - Expression type compatibility

4. **Code Generation** (`CodeGenerator`)

    - Converts AST to stack-based bytecode
    - Handles type conversions and control flow

5. **Interpretation** (`Interpreter`)
    - Stack-based virtual machine
    - Executes bytecode instructions
    - Runtime I/O and memory management

### Stack-Based Virtual Machine

The interpreter uses a stack-based architecture with these instruction types:

-   **Stack Operations**: `push`, `pop`, `load`, `save`
-   **Arithmetic**: `add`, `sub`, `mul`, `div`, `mod`, `uminus`
-   **Logical**: `and`, `or`, `not`
-   **Comparison**: `eq`, `lt`, `gt`
-   **Control Flow**: `jmp`, `fjmp`, `label`
-   **I/O**: `print`, `read`
-   **Type Conversion**: `itof` (int to float)
-   **String**: `concat`

## 📚 Sample Programs

The `sample_inputs/` directory contains various example programs:

-   **sample1/**: Basic language features and I/O
-   **sample2/**: Expression evaluation and operators
-   **sample3/**: Control flow statements
-   **sample4/**: Advanced features and type conversion
-   **sample5/**: Complex program demonstrating all features
-   **sample_err/**: Error cases for testing type checker

Each sample includes:

-   `.txt` - Source code
-   `generated_code*.txt` - Generated bytecode
-   `output.txt` - Expected execution output

## 🔧 Error Handling

The compiler provides comprehensive error reporting:

### Syntax Errors

```
Syntax error at line 5, column 12: mismatched input ';' expecting ')'
```

### Type Errors

```
Type error at line 8, column 5: Cannot assign string to int
Type error at line 12, column 10: Variable 'x' is not declared
```

### Runtime Errors

```
Runtime Error: Stack underflow at instruction 15
Runtime Error: Division by zero at instruction 23
```

---

This project is developed for educational purposes as part of a PLC - Programming Languages and Compilers course at VŠB-TUO.

_Built with ANTLR4 and Python • Demonstrates complete compiler construction pipeline_
