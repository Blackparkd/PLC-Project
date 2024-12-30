import ply.lex as lex


tokens = (
    'TYPE',
    'ID',
    'EQ', 
    'NEQ',
    'ÑOT', 
    'MORE', 
    'MOREEQ', 
    'LESS', 
    'LESSEQ', 
    'NUM', 
    'PLUS',
    'MINUS',
    'DIV',
    'MULT', 
    'AND',
    'OR',
    'PRINT', 
    'INPUT', 
    'STRING',
    'OTHERWISE', 
    'WHILE', 
    'DO',
    'MOD',
    'LPAR',
    'RPAR',
    'REPEAT',
    'UNTIL'
)

literals = [':',',','=','{','}','|','"','']

#Regras
t_PLUS = r'\+' #soma
t_MINUS = r'\-' #subtração
t_DIV = r'\/' #divisão
t_MULT = r'\*' #multiplicação
t_MORE = r'\>' #maior
t_LESS = r'\<'  #menor
t_EQ = r'\=\=' #igual
t_NEQ = r'\!\=' #diferente
t_NOT = r'\~' #não
t_MOREEQ = r'\>\=' #maior ou igual
t_LESSEQ  = r'\<\=' # menor ou igual
t_MOD = r'\%' #resto
t_LPAR = r'\(' #parenteses esquerdo
t_RPAR = r'\)' #parenteses direito
t_AND = r'\&' # e/and
t_OR = r'\|\|' # ou/or


def t_ID(t):
    r'[a-zA-Z0-9]+'
    return t

def t_NUM(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

def t_PRINT(t):
    r'print'
    return t

def t_INPUT(t):
    r'input'
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_TYPE(t):
    r'NUM|STRING'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_OTHERWISE(t):
    r'otherwise'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) ## returns the number of the line within the report page that is currently being printed

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \r\t'

lexer = lex.lex()