"""
Main script for grammar Expr1

"""
from copy import deepcopy
from enum import Enum
__version__ = '0.1.0'
__author__ = 'Morteza'

import unittest
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.testLexer import testLexer
from gen.testParser import testParser


# Step 0: Input program
x = '?'
f = open("input_file.txt", "r")
input_string = f.read()
# Step 1: Convert input to stream
stream = InputStream(input_string)
# Step 2: Create lexer object
lexer = testLexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
token_stream.fill()
# Step 4: Create a token stream rewriter
rewriter = TokenStreamRewriter(token_stream)
# Step 4: Create a parser object
parser = testParser(token_stream)
# Step 5: Parse from start rule
parse_tree = parser.start()
lexer.reset()
print("input string is (before):\n   ", input_string)
i = 0
tokens = lexer.getAllTokens()
lexer.reset()
for token in lexer.getAllTokens():
    # if token.channel == 1:  # comment remove
    # continue
    # Methode 1
    if lexer.symbolicNames[token.type - 2] == 'LINE_COMMENT':
        txt = token.text[2:]
        new_comment = "/* " + txt + " - Author: mohammad javad faghihniya */"
        rewriter.replaceIndex(i, new_comment)
    #Methode 2
#    if token.channel == 1:
#        txt = token.text[2:]
#        new_comment = "/* " + txt + " */\n"
#        rewriter.replaceIndex(i, new_comment)
    i = i + 1
    # break
# rewriter.replace(rewriter.DEFAULT_PROGRAM_NAME,  token.start, token.stop, 'parsa')
print('input string is (after):\n', rewriter.getDefaultText())
