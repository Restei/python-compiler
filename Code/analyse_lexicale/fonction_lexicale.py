import re
from analyse_lexicale.token import *


def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu

def affichage_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
        print("La taille du contenu est:", len(contenu))
        for lettre in contenu:
            if lettre == "\n":
                print("\\n")  # Saut de ligne
            elif lettre == "\t":
                print("\\t")  # Tabulation
            else:
                print(lettre, end="")  
                
    return "Affichage terminé"

class Lexeur:
    def __init__(self, contenu):
        self.contenu = contenu + " "
        self.taille = len(self.contenu)
        self.column = -1
        self.position = -1
        self.ligne_position = 1
        self.curseur_position = 0
        self.charactere_actuelle = None
        self.token = None
        self.token_nombre = False
        self.fin_fichier = False
        self.string = False
        self.is_indent = False
        self.variable_error = False
        self.number_error = False
        self.count = 0
        self.pile_indent = [0]
        self.errors = []

    def lire(self):
        if self.curseur_position >= self.taille:
            self.fin_fichier = True
        else:
            self.position += 1
            self.column += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1
                self.column = 0

    def retour(self):
        if self.curseur_position >= 1:
            if self.charactere_actuelle == '\n':
                self.ligne_position -= 1
            self.position -= 1
            self.curseur_position -= 1
            self.charactere_actuelle = self.contenu[self.position]

    def peek(self):
        if self.curseur_position + 1 < len(self.contenu):
            return self.contenu[self.curseur_position + 1]
        return None

    def next_line(self):
        while self.charactere_actuelle != '\n':
            self.lire()

    def chiffre(self):
        return self.charactere_actuelle.isdigit()

    def charactere(self):
        return self.charactere_actuelle.isalpha() or self.charactere_actuelle == '_'
    
    def caractere_inconnu(self):
        caracteres_autorises = "!\"#%&'()*+,-./:<=>?[\\]^_`{|} "
        if self.charactere_actuelle.isalnum() or self.charactere_actuelle in caracteres_autorises:
            return False 
        return True 

    def fin_de_mot(self):
        fin = [',', '\n', ' ', '+', '-', ':', '(', ')', '[', ']', '/', '*', '=', '.']
        return self.charactere_actuelle in fin
    def unary_operator(self):
        operator_type = TokenType.is_unary_operator(self.charactere_actuelle)
        if operator_type:
            
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.column)
        return None  

    def binary(self):
      
        if self.curseur_position + 1 < self.taille:
            next_charactere = self.contenu[self.curseur_position]
            binary_token = self.charactere_actuelle + next_charactere

            operator_type = TokenType.is_binary_operator(binary_token)
            if operator_type:
                
                self.lire()  
                return OperatorBinaryToken(binary_token, self.ligne_position, self.column)
            else:
                return self.unary_operator()
        else:
            return self.unary_operator()


    def mot_cle(self):
        keywords = {
            'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
            'def': 'DEF', 'return': 'RETURN', 'import': 'IMPORT', 'from': 'FROM', 
            'and':'AND', 'True':'TRUE','False':'FALSE','in':'IN','not':'NOT','or':'OR',
            'print':'PRINT','None':'NONE'
        }
        if self.variable_error or self.number_error:
            return UnknownToken(self.token,self.ligne_position,self.column)
        
        if self.token in keywords:
            return KeywordToken(self.token, self.ligne_position, self.column)
        
        elif self.token_nombre:
            if self.token[0]=='0':
                if len(self.token)>1:
                    self.errors.append(ZeroException(self.ligne_position,self.token))
                    return UnknownToken(self.token,self.ligne_position,self.column)
            return LiteralToken(self.token, self.ligne_position, self.column)
        
        elif self.string:
            return StringToken(self.token,self.ligne_position,self.column)
        
        else:
            return IdentifierToken(self.token, self.ligne_position, self.column)

    def Identification(self,tokens):
        if self.is_indent==True and self.charactere_actuelle!='\n':
            if self.charactere_actuelle==' ' and not self.fin_fichier:
                self.count+=1
            else:
                if self.fin_fichier:
                    self.count-=1
                self.retour()
                self.is_indent=False
                if self.count==self.pile_indent[0]:
                    pass
                elif self.count>self.pile_indent[0]:
                    self.pile_indent = [self.count] + self.pile_indent
                    tokens.append(IndentToken(self.ligne_position,self.column ))
                    self.count = 0
                else:
                    if self.count in self.pile_indent:
                        while self.count!=self.pile_indent[0]:
                            tokens.append(DedentToken(self.ligne_position,self.position))
                            self.pile_indent = self.pile_indent[1:]
                            self.pile_indent[0] = self.pile_indent[0]
                    else:
                        self.errors.append(IndentException(self.ligne_position))


        elif self.charactere_actuelle == '#':
            self.next_line()
            self.retour()
        
        
        elif (self.charactere() or self.charactere_actuelle == '_') & (self.token is None) & (not self.string):
                self.token = self.charactere_actuelle
                

        elif (self.charactere_actuelle == '"') & (self.token is None) & (not self.string):
                self.token = self.charactere_actuelle
                self.string = True

        elif self.token and (self.string):
            if self.charactere_actuelle !='"':
                self.token += self.charactere_actuelle
            else:
                self.token += self.charactere_actuelle
                tokens.append(self.mot_cle())
                self.token = None
                self.string = False

        elif self.token and not self.string:
            if not self.fin_de_mot():
                if (not self.charactere()) and (not self.chiffre()) and (not self.token_nombre):
                    self.variable_error = True
                if self.token_nombre and not self.chiffre():
                    self.number_error = True
                self.token += self.charactere_actuelle
            else:
                if self.variable_error:
                    self.errors.append(UnknowCaractersInVariable((self.ligne_position),(self.token)))
                if self.number_error:
                    self.errors.append(AlphainNumberException(self.ligne_position,self.token))
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
                self.variable_error = False
                self.number_error = False
                self.Identification(tokens)
                 

        elif self.chiffre() & (not self.token) & (not self.string):
            self.token = self.charactere_actuelle
            self.token_nombre = True
  
        
        elif self.charactere_actuelle == '\n':
            tokens.append(NewlineToken(self.ligne_position,self.column))
            while self.peek()=='\n':
                self.lire()
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
            self.is_indent = True
            self.count = 0


        
        elif self.charactere_actuelle in '(){}[]:,' and not self.string:
            tokens.append(PunctuationToken(self.charactere_actuelle, self.ligne_position, self.column))
        
        
        else:
            operator_token = self.binary()  
            if operator_token:
                tokens.append(operator_token)
            elif self.caractere_inconnu():
                tokens.append(UnknownToken(self.charactere_actuelle,self.ligne_position,self.column))
                self.errors.append(UnknowCaracters((self.ligne_position),(self.charactere_actuelle)))
                
    def Tokenisation(self):
        tokens = []
        while not self.fin_fichier:
            self.lire()
            self.Identification(tokens)
        
        # Ajouter le token EOF à la fin
        tokens.append(BaseToken(TokenType.EOF, '', self.ligne_position, self.column))

        return tokens,self.errors
