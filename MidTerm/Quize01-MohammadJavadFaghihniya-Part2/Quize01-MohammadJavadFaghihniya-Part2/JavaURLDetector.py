"""
Main script for grammar Expr1

"""
import argparse
from copy import deepcopy
from enum import Enum
__version__ = '0.1.0'
__author__ = 'Mohammad Javad Faghihniya'

import unittest
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.Java9_v2Lexer import Java9_v2Lexer
from gen.Java9_v2Parser import Java9_v2Parser

# Step 1: Convert input to stream
stream = FileStream('A.java', encoding='utf8')
# Step 2: Create lexer object
lexer = Java9_v2Lexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
token_stream.fill()
# Step 4: Create a token stream rewriter
rewriter = TokenStreamRewriter(token_stream)
# Step 5: Create a parser object
parser = Java9_v2Parser(token_stream)
# Step 6: Create parse tree
parse_tree = parser.compilationUnit()
print(stream)
lexer.reset()
i = 0
tokens = lexer.getAllTokens()
lexer.reset()

# URL finder loop
print('There are following URLs in code: ')
for token in lexer.getAllTokens():
    if token.type == lexer.UrlLiteral:
        print(token.text)
    i = i + 1
print('-----------------------------------------')
#  string finder loop
lexer.reset()
j=0
print('There are following strings in code, Except URL: ')
for token in lexer.getAllTokens():
    if token.type == lexer.StringLiteral:
        print(token.text)
    j = j + 1
