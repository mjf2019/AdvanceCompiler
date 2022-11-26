# Generated from G:/PHD-IUST/Courses/Compiler/Assignment/Exercise_2\test.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,29,8,1,10,1,12,1,32,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,54,8,3,1,
        3,0,2,2,4,4,0,2,4,6,0,0,59,0,11,1,0,0,0,2,16,1,0,0,0,4,33,1,0,0,
        0,6,53,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,1,
        0,0,0,16,17,6,1,-1,0,17,18,3,4,2,0,18,30,1,0,0,0,19,20,10,4,0,0,
        20,21,5,7,0,0,21,29,3,2,1,5,22,23,10,3,0,0,23,24,5,3,0,0,24,29,3,
        4,2,0,25,26,10,2,0,0,26,27,5,4,0,0,27,29,3,4,2,0,28,19,1,0,0,0,28,
        22,1,0,0,0,28,25,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,
        0,31,3,1,0,0,0,32,30,1,0,0,0,33,34,6,2,-1,0,34,35,3,6,3,0,35,44,
        1,0,0,0,36,37,10,3,0,0,37,38,5,5,0,0,38,43,3,6,3,0,39,40,10,2,0,
        0,40,41,5,6,0,0,41,43,3,6,3,0,42,36,1,0,0,0,42,39,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,
        54,5,10,0,0,48,54,5,11,0,0,49,50,5,1,0,0,50,51,3,2,1,0,51,52,5,2,
        0,0,52,54,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,7,
        1,0,0,0,6,11,28,30,42,44,53
    ]

class testParser ( Parser ):

    grammarFileName = "test.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "MINUS", 
                      "MUL", "DIVIDE", "ASSIGN", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "Id", "Number", "Newline", "Whitespace" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    MINUS=4
    MUL=5
    DIVIDE=6
    ASSIGN=7
    LINE_COMMENT=8
    BLOCK_COMMENT=9
    Id=10
    Number=11
    Newline=12
    Whitespace=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(testParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.ExprContext)
            else:
                return self.getTypedRuleContext(testParser.ExprContext,i)


        def getRuleIndex(self):
            return testParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = testParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << testParser.T__0) | (1 << testParser.Id) | (1 << testParser.Number))) != 0):
                self.state = 8
                self.expr(0)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(testParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Rule_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(testParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_minus" ):
                listener.enterRule_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_minus" ):
                listener.exitRule_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_minus" ):
                return visitor.visitRule_minus(self)
            else:
                return visitor.visitChildren(self)


    class Rule_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)

        def Plus(self):
            return self.getToken(testParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_plus" ):
                listener.enterRule_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_plus" ):
                listener.exitRule_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_plus" ):
                return visitor.visitRule_plus(self)
            else:
                return visitor.visitChildren(self)


    class Rule3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule3" ):
                listener.enterRule3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule3" ):
                listener.exitRule3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule3" ):
                return visitor.visitRule3(self)
            else:
                return visitor.visitChildren(self)


    class Rule_assignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.ExprContext)
            else:
                return self.getTypedRuleContext(testParser.ExprContext,i)

        def ASSIGN(self):
            return self.getToken(testParser.ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_assign" ):
                listener.enterRule_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_assign" ):
                listener.exitRule_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_assign" ):
                return visitor.visitRule_assign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = testParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = testParser.Rule3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 17
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = testParser.Rule_assignContext(self, testParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 20
                        self.match(testParser.ASSIGN)
                        self.state = 21
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = testParser.Rule_plusContext(self, testParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 23
                        self.match(testParser.Plus)
                        self.state = 24
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = testParser.Rule_minusContext(self, testParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 26
                        self.match(testParser.MINUS)
                        self.state = 27
                        self.term(0)
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(testParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def MUL(self):
            return self.getToken(testParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(testParser.DIVIDE, 0)

        def getRuleIndex(self):
            return testParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = testParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = testParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(testParser.MUL)
                        self.state = 38
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = testParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(testParser.DIVIDE)
                        self.state = 41
                        self.fact()
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(testParser.Id, 0)

        def Number(self):
            return self.getToken(testParser.Number, 0)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)


        def getRuleIndex(self):
            return testParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = testParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [testParser.Id]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(testParser.Id)
                pass
            elif token in [testParser.Number]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(testParser.Number)
                pass
            elif token in [testParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(testParser.T__0)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(testParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




