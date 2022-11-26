"""
Main script for grammar Expr1

"""
import argparse
from copy import deepcopy
from enum import Enum
__version__ = '0.1.0'
__author__ = 'Morteza'

import unittest
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.CPP14_v2Lexer import CPP14_v2Lexer
from gen.CPP14_v2Parser import CPP14_v2Parser

# Step 1: Convert input to stream
stream = FileStream('input_file.cpp', encoding='utf8')
# Step 2: Create lexer object
lexer = CPP14_v2Lexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
token_stream.fill()
# Step 4: Create a token stream rewriter
rewriter = TokenStreamRewriter(token_stream)
# Step 5: Create a parser object
parser = CPP14_v2Parser(token_stream)
# Step 6: Parse from start rule
parse_tree = parser.translationunit()
lexer.reset()
print("input string is (before):\n   ", stream)
i = 0
tokens = lexer.getAllTokens()
lexer.reset()
for token in lexer.getAllTokens():

    if token.type == lexer.LineComment:
        txt = token.text[2:]
        new_comment = "/* " + txt + " - Author: mohammad javad faghihniya */"
        rewriter.replaceIndex(i, new_comment)
    i = i + 1
print('-----------------------------------')
print('input string is (after):\n', rewriter.getDefaultText())
