// MiniC.g4 - VERSÃO CORRIGIDA (entende void)
grammar MiniC;

// --- REGRAS DO PARSER ---

compilationUnit
    : (Directive | externalDeclaration)* EOF
    ;

preprocessorDirective
    : Directive
    ;

externalDeclaration
    : functionDefinition
    | declaration
    ;

functionDefinition
    : typeSpecifier declarator compoundStatement
    ;

declaration
    : typeSpecifier initDeclaratorList? ';'
    ;

initDeclaratorList
    : initDeclarator (',' initDeclarator)*
    ;

initDeclarator
    : declarator ('=' initializer)?
    ;

initializer
    : assignmentExpression
    | '{' initializerList ','? '}'
    ;

initializerList
    : initializer (',' initializer)*
    ;

typeSpecifier
    : Void
    | Char
    | Int
    | Float
    | structOrUnionSpecifier
    | typedefName
    ;

structOrUnionSpecifier
    : structOrUnion Identifier? '{' structDeclarationList '}'
    | structOrUnion Identifier
    ;

structOrUnion
    : Struct
    | Union
    ;

structDeclarationList
    : structDeclaration+
    ;

structDeclaration
    : typeSpecifier structDeclaratorList ';'
    ;

structDeclaratorList
    : structDeclarator (',' structDeclarator)*
    ;

structDeclarator
    : declarator
    ;

declarator
    : pointer? directDeclarator
    ;

directDeclarator
    : Identifier
    | '(' declarator ')'
    | directDeclarator '[' constantExpression? ']'
    // --- CORREÇÃO AQUI ---
    // Permite (void) ou (parameterList) ou ()
    | directDeclarator '(' ( parameterTypeList | Void )? ')'
    ;

// Lista de parâmetros
parameterTypeList
    : parameterList
    ;

parameterList
    : parameterDeclaration (',' parameterDeclaration)*
    ;

parameterDeclaration
    : typeSpecifier declarator
    ;

pointer
    : Star+
    ;

typeName
    : typeSpecifier abstractDeclarator?
    ;

abstractDeclarator
    : pointer
    | pointer? directAbstractDeclarator
    ;

directAbstractDeclarator
    : '(' abstractDeclarator ')'
    | '[' constantExpression? ']'
    | '(' parameterTypeList? ')'
    | directAbstractDeclarator '[' constantExpression? ']'
    | directAbstractDeclarator '(' parameterTypeList? ')'
    ;

typedefName
    : Identifier
    ;

// --- Expressões (Sem alterações) ---
expression
    : assignmentExpression (',' assignmentExpression)*
    ;
constantExpression
    : conditionalExpression
    ;
assignmentExpression
    : conditionalExpression
    | unaryExpression assignmentOperator assignmentExpression
    ;
assignmentOperator
    : Assign | StarAssign | DivAssign | ModAssign | PlusAssign | MinusAssign
    ;
conditionalExpression
    : logicalOrExpression
    ;
logicalOrExpression
    : logicalAndExpression (OrOr logicalAndExpression)*
    ;
logicalAndExpression
    : inclusiveOrExpression (AndAnd inclusiveOrExpression)*
    ;
inclusiveOrExpression
    : exclusiveOrExpression (Or exclusiveOrExpression)*
    ;
exclusiveOrExpression
    : andExpression (Caret andExpression)*
    ;
andExpression
    : equalityExpression (And equalityExpression)*
    ;
equalityExpression
    : relationalExpression ( (Equal | NotEqual) relationalExpression )*
    ;
relationalExpression
    : additiveExpression ( (Less | Greater | LessEqual | GreaterEqual) additiveExpression )*
    ;
additiveExpression
    : multiplicativeExpression ( (Plus | Minus) multiplicativeExpression )*
    ;
multiplicativeExpression
    : castExpression ( (Star | Div | Mod) castExpression )*
    ;
castExpression
    : '(' typeName ')' castExpression
    | unaryExpression
    ;
unaryExpression
    : postfixExpression
    | PlusPlus unaryExpression
    | MinusMinus unaryExpression
    | unaryOperator castExpression
    | Sizeof '(' typeName ')'
    ;
unaryOperator
    : And | Star | Plus | Minus | Not
    ;
postfixExpression
    : primaryExpression (
        '[' expression ']'
        | '(' argumentExpressionList? ')'
        | (Dot | Arrow) Identifier
        | PlusPlus
        | MinusMinus
    )*
    ;
argumentExpressionList
    : assignmentExpression (',' assignmentExpression)*
    ;
primaryExpression
    : Identifier
    | Constant
    | StringLiteral+
    | '(' expression ')'
    ;

// --- Declarações (Sem alterações) ---
statement
    : labeledStatement
    | compoundStatement
    | expressionStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    ;
labeledStatement
    : Case constantExpression ':' statement
    | Default ':' statement
    ;
compoundStatement
    : LeftBrace blockItemList? RightBrace
    ;
blockItemList
    : blockItem+
    ;
blockItem
    : statement
    | declaration
    ;
expressionStatement
    : expression? Semi
    ;
selectionStatement
    : If '(' expression ')' statement (Else statement)?
    | Switch '(' expression ')' statement
    ;
iterationStatement
    : While '(' expression ')' statement
    | Do statement While '(' expression ')' Semi
    | For '(' forCondition ')' statement
    ;
forCondition
    : (forDeclaration | expression?) Semi expression? Semi expression?
    ;
forDeclaration
    : typeSpecifier initDeclaratorList
    ;
jumpStatement
    : Continue Semi
    | Break Semi
    | Return expression? Semi
    ;

// --- LEXER (Sem alterações) ---
Break: 'break';
Case: 'case';
Char: 'char';
Continue: 'continue';
Default: 'default';
Do: 'do';
Else: 'else';
Float: 'float';
For: 'for';
If: 'if';
Int: 'int';
Return: 'return';
Sizeof: 'sizeof';
Struct: 'struct';
Switch: 'switch';
Union: 'union';
Void: 'void';
While: 'while';
Typedef: 'typedef';
Static: 'static';
Extern: 'extern';
LeftParen: '(';
RightParen: ')';
LeftBracket: '[';
RightBracket: ']';
LeftBrace: '{';
RightBrace: '}';
Less: '<';
LessEqual: '<=';
Greater: '>';
GreaterEqual: '>=';
Plus: '+';
PlusPlus: '++';
Minus: '-';
MinusMinus: '--';
Star: '*';
Div: '/';
Mod: '%';
And: '&';
Or: '|';
AndAnd: '&&';
OrOr: '||';
Caret: '^';
Not: '!';
Question: '?';
Colon: ':';
Semi: ';';
Comma: ',';
Assign: '=';
StarAssign: '*=';
DivAssign: '/=';
ModAssign: '%=';
PlusAssign: '+=';
MinusAssign: '-=';
Equal: '==';
NotEqual: '!=';
Arrow: '->';
Dot: '.';
Identifier: [a-zA-Z_] [a-zA-Z0-9_]*;
Constant: IntegerConstant | FloatingConstant | CharacterConstant;
fragment IntegerConstant: [0-9]+;
fragment FloatingConstant: [0-9]+ '.' [0-9]* | '.' [0-9]+;
fragment CharacterConstant: '\'' ( ~['\\\r\n] | '\\' . ) '\'';
StringLiteral: '"' ( ~["\\\r\n] | '\\' . )* '"';
Directive: '#' [ \t]* 'include' [ \t]* ( '<' ~[\r\n>]+ '>' | '"' ~[\r\n"]+ '"' ) | '#' [ \t]* 'define' [ \t]+ Identifier ( ~[\r\n] )*;
Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: ('\r' '\n'? | '\n') -> channel(HIDDEN);
BlockComment: '/*' .*? '*/' -> channel(HIDDEN);
LineComment: '//' ~[\r\n]* -> channel(HIDDEN);