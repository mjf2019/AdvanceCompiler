/*
grammar test
Grammar of simple mathematical expressions. Without any attribute and action.
Test grammar for demo and education porpuse.
- Example of input which accepts by the grammar:
-- x = a + b * c

Written by: Morteza Zakeri
*/

grammar test;
start:

    Id '=' expr EOF
    ;

expr:
    expr '+' term #rule_plus
    | expr '-' term  #rule_minus
    | term #rule3
    ;

term:
    term '*' fact
    | term '/' fact
    | fact
    ;

fact:
    Id
    | Number
    | '('expr')'
    ;
/* Lexical rules*/

Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';

LINE_COMMENT:'//'.*?'\r'?'\n' -> skip;
BLOCK_COMMENT : '/*'.*?'*/' -> skip;
Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: [a-zA-Z*?][a-zA-Z?*]*;
fragment NUMBER: [0-9]+;

Newline: '\n' -> skip;
Whitespace: [ \t\r]+ -> channel(HIDDEN);

