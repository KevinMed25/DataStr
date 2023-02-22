#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
/* Global declarations */
/* Variables */
int charClass;
char lexeme [100];
char nextChar;
int lexLen;
int token;
int nextToken;
FILE *in_fp, *fopen();	
/*Lista de lexemas y tokens*/
char lexemas[100][100];
int tokens[100];
int i=0;
int k=0;
/* Function declarations */
void addChar();
void getChar();
void getNonBlank();
int lex();
int verificaReservada();
void expr();
void term();
void factor();
/*Palabras reservadas **** DO 2, WHILE 3, FOR   4, IF    5, ELSE  6 */
char reservadas[5][10]  = {"DO","WHILE","FOR","IF","ELSE"};
/* Character classes */
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99
/* Token codes */
#define INT_LIT 10
#define IDENT 11
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26
#define PYC 27
/* main driver */
int main(int argc, char *argv[]) {
	/* Open the input data file and process its contents */
	if ((in_fp = fopen("front2.in", "r")) == NULL)
		printf("ERROR - cannot open front2.in \n");
	else {
		getChar();
		do {
			lex();
		} while (nextToken != EOF);
	}
	for(int j=0;j<i;j++){
		printf("Token: %2i ,Lexema: %s\n",tokens[j],lexemas[j]);
	}
	expr();
	k++;
	if(tokens[k]!=PYC)
		printf("\nExpresion incorrecta",PYC,tokens[k], lexemas[k]);//%i %i %s
	else
		printf("%s",lexemas[k]);
	return 0;
}
/* lookup - a function to lookup operators and parentheses
and return the token */
int lookup(char ch) {
	switch (ch) {
	case '(':
		addChar();
		nextToken = LEFT_PAREN;
		break;
	case ')':
		addChar();
		nextToken = RIGHT_PAREN;
		break;
	case '+':
		addChar();
		nextToken = ADD_OP;
		break;
	case '-':
		addChar();
		nextToken = SUB_OP;
		break;
	case '*':
		addChar();
		nextToken = MULT_OP;
		break;
	case '/':
		addChar();
		nextToken = DIV_OP;
		break;
    case '=':
		addChar();
		nextToken = ASSIGN_OP;
		break;
	case ';':
		addChar();
		nextToken = PYC;
		break;
	default:
		addChar();
		nextToken = EOF;
		break;
	}
	return nextToken;
}
/* addChar - a function to add nextChar to lexeme */
void addChar() {
	if (lexLen <= 98) {
		lexeme[lexLen++] = nextChar;
		lexeme[lexLen] = 0;
	}
	else
		printf("Error - lexeme is too long \n");
}
/* getChar - a function to get the next character of
input and determine its character class */
void getChar() {
	if ((nextChar = getc(in_fp)) != EOF) {
		if (isalpha(nextChar))
			charClass = LETTER;
		else if (isdigit(nextChar))
			charClass = DIGIT;
			else charClass = UNKNOWN;
	}
	else
		charClass = EOF;
}
void getNonBlank() {
	while (isspace(nextChar))
		getChar();
}
	/* lex - a simple lexical analyzer for arithmetic expressions */
int lex() {
	lexLen = 0;
	getNonBlank();
	switch (charClass) {
	case LETTER:
		addChar();
		getChar();
		while (charClass == LETTER || charClass == DIGIT) {
			addChar();
			getChar();
		}
		if(verificaReservada()!=-2)
			nextToken = verificaReservada();
		else
			nextToken = IDENT;
		break;
		/* Parse integer literals */
	case DIGIT:
		addChar();
		getChar();
		while (charClass == DIGIT) {
			addChar();
			getChar();
		}
		nextToken = INT_LIT;
		break;
		/* Parentheses and operators */
	case UNKNOWN:
		lookup(nextChar);
		getChar();
		break;
		/* EOF */
	case EOF:
		nextToken = EOF;
		lexeme[0] = 'E';
		lexeme[1] = 'O';
		lexeme[2] = 'F';
		lexeme[3] = 0;
		break;
	} /* End of switch */
	tokens[i]=nextToken;
	strcpy(lexemas[i],lexeme);
	i++;
	//printf("Token: %2d, Lexeme %s\n", nextToken, lexeme);
	return nextToken;
} /* End of function lex */
int verificaReservada(){
	int esReservada = -2;
	/*Valores de las  palabras reservadas
	******** DO 2, WHILE 3, FOR   4, IF    5, ELSE  6 ********/
	for(int i = 0;i<5;i++){
		if(strcmp(lexeme,reservadas[i])==0)
			esReservada = i+2;
	}
	return esReservada;
}
	/* expr
	Parses strings in the language generated by the rule:
	<expr> -> <term> {(+ | -) <term>}
	*/
	void expr() {
		//printf("Enter <expr>\n");
		/* Parse the first term */
		term();
		//k++;
		/* As long as the next token is + or -, get
		the next token and parse the next term */
		while (tokens[k] == ADD_OP || tokens[k] == SUB_OP) {
			printf("%s",lexemas[k]);//lex();
			k++;
			term();
		}
		//printf("Exit <expr>\n");
	} /* End of function expr */
	/* term
	Parses strings in the language generated by the rule:
	<term> -> <factor> {(* | /) <factor>) 
	*/
	void term() {
		//printf("Enter <term>\n");
		/* Parse the first factor */
		factor();
		k++;
		/* As long as the next token is * or /, get the
		next token and parse the next factor */
		while (tokens[k] == MULT_OP || tokens[k] == DIV_OP) {
			printf("%s",lexemas[k]);//lex();
			k++;
			factor();
		}
		//printf("Exit <term>\n");
	} /* End of function term */
	/* factor
	Parses strings in the language generated by the rule:
	<factor> -> id | int_constant | ( <expr )
	*/
	void factor() {
		//printf("Enter <factor>\n");
		/* Determine which RHS */
		if (tokens[k] == IDENT || tokens[k] == INT_LIT)
			printf("%s",lexemas[k]);
			/* Get the next token */
			//lex();
		/* If the RHS is ( <expr>), call lex to pass over the 
		left parenthesis, call expr, and check for the right
		parenthesis */
		else {
			if (tokens[k] == LEFT_PAREN){
				printf("%s",lexemas[k]);
				k++;
				expr();
				if (tokens[k] == RIGHT_PAREN){
					printf("%s",lexemas[k]);
				}
				else
					printf("Error");//error();
			} /* End of if (nextToken == ... */
			/* It was not an id, an integer literal, or a left
			parenthesis */
			else
				printf("Error");//error();
		} /* End of else */
		//printf("Exit <factor>\n");;
	} /* End of function factor */
