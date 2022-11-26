// Generated from G:/PHD-IUST/Courses/Compiler/Assignment/Exercise_2\test.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class testLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Plus=3, MINUS=4, MUL=5, DIVIDE=6, ASSIGN=7, LINE_COMMENT=8, 
		BLOCK_COMMENT=9, Id=10, Number=11, Newline=12, Whitespace=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", "LINE_COMMENT", 
			"BLOCK_COMMENT", "Id", "Number", "IDENTIFIER", "NUMBER", "Newline", "Whitespace"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'='", null, null, null, 
			null, "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", "LINE_COMMENT", 
			"BLOCK_COMMENT", "Id", "Number", "Newline", "Whitespace"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public testLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "test.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\ra\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005"+
		"\u00072\b\u0007\n\u0007\f\u00075\t\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0005\b=\b\b\n\b\f\b@\t\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0005\u000bM\b\u000b\n\u000b\f\u000bP\t\u000b\u0001\f\u0004\fS\b\f\u000b"+
		"\f\f\fT\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0004\u000e\\\b\u000e"+
		"\u000b\u000e\f\u000e]\u0001\u000e\u0001\u000e\u0001>\u0000\u000f\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\u0000\u0019\u0000\u001b\f\u001d"+
		"\r\u0001\u0000\u0004\u0002\u0000\n\n\r\r\u0004\u0000**??AZaz\u0001\u0000"+
		"09\u0003\u0000\t\t\r\r  c\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0001\u001f\u0001\u0000"+
		"\u0000\u0000\u0003!\u0001\u0000\u0000\u0000\u0005#\u0001\u0000\u0000\u0000"+
		"\u0007%\u0001\u0000\u0000\u0000\t\'\u0001\u0000\u0000\u0000\u000b)\u0001"+
		"\u0000\u0000\u0000\r+\u0001\u0000\u0000\u0000\u000f-\u0001\u0000\u0000"+
		"\u0000\u00118\u0001\u0000\u0000\u0000\u0013F\u0001\u0000\u0000\u0000\u0015"+
		"H\u0001\u0000\u0000\u0000\u0017J\u0001\u0000\u0000\u0000\u0019R\u0001"+
		"\u0000\u0000\u0000\u001bV\u0001\u0000\u0000\u0000\u001d[\u0001\u0000\u0000"+
		"\u0000\u001f \u0005(\u0000\u0000 \u0002\u0001\u0000\u0000\u0000!\"\u0005"+
		")\u0000\u0000\"\u0004\u0001\u0000\u0000\u0000#$\u0005+\u0000\u0000$\u0006"+
		"\u0001\u0000\u0000\u0000%&\u0005-\u0000\u0000&\b\u0001\u0000\u0000\u0000"+
		"\'(\u0005*\u0000\u0000(\n\u0001\u0000\u0000\u0000)*\u0005/\u0000\u0000"+
		"*\f\u0001\u0000\u0000\u0000+,\u0005=\u0000\u0000,\u000e\u0001\u0000\u0000"+
		"\u0000-.\u0005/\u0000\u0000./\u0005/\u0000\u0000/3\u0001\u0000\u0000\u0000"+
		"02\b\u0000\u0000\u000010\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u0000"+
		"31\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u000046\u0001\u0000\u0000"+
		"\u000053\u0001\u0000\u0000\u000067\u0006\u0007\u0000\u00007\u0010\u0001"+
		"\u0000\u0000\u000089\u0005/\u0000\u00009:\u0005*\u0000\u0000:>\u0001\u0000"+
		"\u0000\u0000;=\t\u0000\u0000\u0000<;\u0001\u0000\u0000\u0000=@\u0001\u0000"+
		"\u0000\u0000>?\u0001\u0000\u0000\u0000><\u0001\u0000\u0000\u0000?A\u0001"+
		"\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AB\u0005*\u0000\u0000BC\u0005"+
		"/\u0000\u0000CD\u0001\u0000\u0000\u0000DE\u0006\b\u0000\u0000E\u0012\u0001"+
		"\u0000\u0000\u0000FG\u0003\u0017\u000b\u0000G\u0014\u0001\u0000\u0000"+
		"\u0000HI\u0003\u0019\f\u0000I\u0016\u0001\u0000\u0000\u0000JN\u0007\u0001"+
		"\u0000\u0000KM\u0007\u0001\u0000\u0000LK\u0001\u0000\u0000\u0000MP\u0001"+
		"\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000"+
		"O\u0018\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000QS\u0007\u0002"+
		"\u0000\u0000RQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TR\u0001"+
		"\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000U\u001a\u0001\u0000\u0000"+
		"\u0000VW\u0005\n\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0006\r\u0000"+
		"\u0000Y\u001c\u0001\u0000\u0000\u0000Z\\\u0007\u0003\u0000\u0000[Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0006\u000e\u0000"+
		"\u0000`\u001e\u0001\u0000\u0000\u0000\u0006\u00003>NT]\u0001\u0000\u0001"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}