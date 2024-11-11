import re
from analyse_lexicale.token import TokenType, BaseToken, KeywordToken, OperatorToken, LiteralToken, IdentifierToken, PunctuationToken, OperatorUnaryToken, OperatorBinaryToken,IndentToken,DedentToken,StringToken


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
        self.position = -1
        self.ligne_position = 1
        self.curseur_position = 0
        self.charactere_actuelle = None
        self.token = None
        self.token_nombre = False
        self.fin_fichier = False
        self.string = False
        self.is_indent = False
        self.count = 0
        self.pile_indent = [0]

    def lire(self):
        if self.curseur_position >= self.taille:
            self.fin_fichier = True
        else:
            self.position += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1

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

    def fin_de_mot(self):
        fin = [',', '\n', ' ', '+', '-', ':', '(', ')', '[', ']', '/', '*', '=', '.']
        return self.charactere_actuelle in fin
    def unary_operator(self):
        operator_type = TokenType.is_unary_operator(self.charactere_actuelle)
        if operator_type:
            
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.position)
        return None  

    def binary(self):
      
        if self.curseur_position + 1 < self.taille:
            next_charactere = self.contenu[self.curseur_position]
            binary_token = self.charactere_actuelle + next_charactere

            operator_type = TokenType.is_binary_operator(binary_token)
            if operator_type:
                
                self.lire()  
                return OperatorBinaryToken(binary_token, self.ligne_position, self.position)
            else:
                return self.unary_operator()
        else:
            return self.unary_operator()


    def mot_cle(self):
        keywords = {
            'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
            'def': 'DEF', 'return': 'RETURN', 'import': 'IMPORT', 'from': 'FROM'
        }

        if self.token in keywords:
            return KeywordToken(self.token, self.ligne_position, self.position)
        elif self.token_nombre:
            return LiteralToken(self.token, self.ligne_position, self.position)
        elif self.string:
            return StringToken(self.token,self.ligne_position,self.position)
        else:
            return IdentifierToken(self.token, self.ligne_position, self.position)

    def Identification(self,tokens):
        if self.is_indent==True and self.charactere_actuelle!='\n':
            if self.charactere_actuelle==' ' and not self.fin_fichier:
                self.count+=1
            else:
                if self.fin_fichier:
                    self.count-=1
                self.retour()
                print(f"\nself pile ={self.pile_indent}; count_indent = {self.count};ligne = {self.ligne_position}")
                self.is_indent=False
                if self.count==self.pile_indent[0]:
                    pass
                elif self.count>self.pile_indent[0]:
                    print("BEGIN")
                    self.pile_indent = [self.count] + self.pile_indent
                    tokens.append(IndentToken(self.ligne_position,self.position))
                    self.count = 0
                else:
                    if self.count in self.pile_indent:
                        while self.count!=self.pile_indent[0]:
                            print(f"END:{self.pile_indent} ; Count = {self.count}")
                            tokens.append(DedentToken(self.ligne_position,self.position))
                            self.pile_indent = self.pile_indent[1:]
                            self.pile_indent[0] = self.pile_indent[0]


        elif self.charactere_actuelle == '#':
            self.next_line()
        
        
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
                self.token += self.charactere_actuelle
            else:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
                self.retour() #reconnaisait les ponctuation que quand il n'y avait pas de token
        
        
        elif self.chiffre() & (not self.token) & (not self.string):
            self.token = self.charactere_actuelle
            self.token_nombre = True
            if(self.charactere_actuelle == '0'):
                tokens.append(LiteralToken(self.token, self.ligne_position, self.position))
                self.token = None
                self.token_nombre = False
            else:
                self.token = self.charactere_actuelle
                self.token_nombre = True   
        
        
        elif self.charactere_actuelle == '\n':
            while self.peek()=='\n':
                self.lire()
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
            self.is_indent = True
            self.count = 0


        
        elif self.charactere_actuelle in '(){}[]' and not self.string:
            tokens.append(PunctuationToken(self.charactere_actuelle, self.ligne_position, self.position))
        
        
        else:
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
        
            
            operator_token = self.binary()  
            if operator_token:
                tokens.append(operator_token)
                
    def Tokenisation(self):
        tokens = []

        while self.position<1285:
            self.lire()
            self.Identification(tokens)

        while not self.fin_fichier:
            self.lire()
            self.Identification(tokens)
        
        # Ajouter le token EOF à la fin
        tokens.append(BaseToken(TokenType.EOF, '', self.ligne_position, self.position))
        return tokens
