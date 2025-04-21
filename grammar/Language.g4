grammar Language;

// Parser Rules
program: statement+ EOF;

statement
    : emptyStatement
    | declarationStatement
    | expressionStatement
    | readStatement
    | writeStatement
    | blockStatement
    | ifStatement
    | whileStatement
    | forStatement
    ;

emptyStatement: ';';

declarationStatement: type variableList ';';

variableList: ID (',' ID)*;

expressionStatement: expression ';';

readStatement: 'read' variableList ';';

writeStatement: 'write' expressionList ';';

expressionList: expression (',' expression)*;

blockStatement: '{' statement* '}';

ifStatement: 'if' '(' expression ')' statement ('else' statement)?;

whileStatement: 'while' '(' expression ')' statement;

forStatement: 'for' '(' init=expression? ';' cond=expression? ';' step=expression? ')' statement;

expression
    : literal                                             # literalExpr
    | ID                                                  # variableExpr
    | '(' expression ')'                                  # parenExpr
    | '!' expression                                      # notExpr
    | '-' expression                                      # unaryMinusExpr
    | <assoc=left> expression ('*' | '/' | '%') expression# multiplicativeExpr
    | <assoc=left> expression ('+' | '-' | '.') expression# additiveExpr
    | <assoc=left> expression ('<' | '>') expression      # relationalExpr
    | <assoc=left> expression ('==' | '!=') expression    # equalityExpr
    | <assoc=left> expression '&&' expression             # andExpr
    | <assoc=left> expression '||' expression             # orExpr
    | cond=expression '?' th=expression ':' el=expression  # TernaryExpr
    | <assoc=right> ID '=' expression                     # assignmentExpr
    ;

type
    : 'int'
    | 'float'
    | 'bool'
    | 'string'
    ;

literal
    : IntegerLiteral
    | FloatLiteral
    | BooleanLiteral
    | StringLiteral
    ;

// Lexer Rules
BooleanLiteral: 'true' | 'false';
StringLiteral: '"' (~["\r\n] | '\\' .)* '"';
IntegerLiteral: [0-9]+;
FloatLiteral: [0-9]+ '.' [0-9]+;

ID: [a-zA-Z] [a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
