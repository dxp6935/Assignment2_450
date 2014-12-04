from sys import *
nextToken = 1
nextChar = ""
lexeme = 0
lexeme = ['']*100
file = None
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = 9999
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
def main():
    global file, nextChar, nextToken,lexLen, charClass
    try:
        try:
            file = open("input.txt", "r")                  
        except Exception, e:
            print "ERROR: cannot open input.txt"
        finally:
            getChar()
            i = 0
        while nextToken != EOF:      
            lex() 
            i+=1
        file.close()
    except Exception, e:
        print e
def addChar():
    global file,nextToken,charClass,lexLen,lexeme,nextChar
    if lexLen <= 98:       
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error:lexeme is too long."  
def getChar():
    global file,nextToken,charClass,lexLen,nextChar
    try:
        t = file.read(1)
        if t != "-1":
            nextChar = t
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN            
        else:
            charClass = EOF
            nextChar = '\0'        
    except Exception, e:
        print e
    
def getNonBlank():
    global file,nextToken,charClass,lexLen,nextChar
    while nextChar.isspace():
        getChar()

def switch(ch):      
    global file,nextToken,charClass,lexLen,lexeme,nextChar
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
def lex():
    global file,nextToken,charClass,lexLen,lexeme,nextChar
    lexLen = 0
    lexeme = ['']*100
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()        
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        switch(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
    
    print "Next token is: " + str(nextToken) + " Next lexeme is " + str(lexeme[1])
    
main()

