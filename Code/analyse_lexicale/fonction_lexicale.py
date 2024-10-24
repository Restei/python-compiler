
def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu

class Lexeur:
    def __init__(self,contenu):
        self.contenu = contenu
        self.position = -1
        self.curseur_position = 0
        self.ligne_position = 1
        self.charactere_actuelle = None
        self.token = None
        self.token_nombre =False
        self.fin_fichier = False
        self.pile = [0]
    
    def lire(self):
        if(self.curseur_position >= len(self.contenu)):
            self.fin_fichier = True
        else:
            self.position +=1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if(self.charactere_actuelle == '\n'):
                self.ligne_position +=1

    def retour(self):
            if (self.curseur_position==0):
                pass
            else: 
                self.position -=1
                self.curseur_position -=1
                self.charactere_actuelle = self.contenu[self.position]
                if (self.charactere_actuelle == '\n'):
                    self.ligne_position = 1

    def chiffre(self):
        if self.charactere_actuelle.isdigit():  
            return True
        else:
            return False
    
    def charactere(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if(self.charactere_actuelle in alphabet):
            return True
        else:
            return False
    
    def fin_de_mot(self):
        fin =[',','\n',' ','+','-',':','(',')','[',']','/','*','=','.']
        if self.charactere_actuelle in fin:
            return True
        else:
            return False
        
    def binary(self):
        next_charactere = self.contenu[self.position + 1]
        binary_token = self.charactere_actuelle + next_charactere
        match binary_token:
            case '&&':
                print("Opérateur logique ET", binary_token)
                self.lire()
            case '||':
                print("Opérateur logique OU", binary_token)
                self.lire()
            case '==':
                print("Opérateur de comparaison égalité", binary_token)
                self.lire()
            case '!=':
                print("Opérateur de comparaison différence", binary_token)
                self.lire()
            case '<=':
                print("Opérateur inférieur ou égal", binary_token)
                self.lire()
            case '>=':
                print("Opérateur supérieur ou égal", binary_token)
                self.lire()
            case '++':
                print("Opérateur d'incrémentation", binary_token)
                self.lire()
            case '--':
                print("Opérateur de décrémentation", binary_token)
                self.lire()
            case '//':
                print("Division entière", binary_token)
                self.lire()
            case '<<':
                print("Décalage à gauche", binary_token)
                self.lire()
            case '>>':
                print("Décalage à droite", binary_token)
                self.lire()
            case '**':
                print("Opérateur de puissance", binary_token)
                self.lire()
            case _:
                match self.charactere_actuelle:
                    case '-':
                        print("soustraction",self.charactere_actuelle)
                    case '*':
                        print("multiplication",self.charactere_actuelle)
                    case '+':
                        print("plus",self.charactere_actuelle)
                    case '/':
                        print("divise à", self.charactere_actuelle)
                    case '=':
                        print("égale",self.charactere_actuelle)
                    case '<':
                        print("inférieur à", self.charactere_actuelle)
                    case '>':
                        print("supérieur à", self.charactere_actuelle)
                    case '!':
                        print(" l'opposé", self.charactere_actuelle)
                    case '&':
                        print(" ET", self.charactere_actuelle)
                    case '|':
                        print(" OU", self.charactere_actuelle)
                    case '"':
                        print('"', self.charactere_actuelle)


    def mot_cle(self):
        match self.token:
            case 'if':
                print("condition if")
            case 'elif':
                print("condition elif")
            case 'else':
                print("condition else")
            case 'and':
                print("condition ET")
            case 'or':
                print("condition OU")
            case 'for':
                print("boucle for")
            case 'while':
                print("boucle while")
            case 'def':
                print("définition de fonction")
            case 'class':
                print("définition de classe")
            case 'import':
                print("importation de module")
            case 'from':
                print("importation de parties de module")
            case 'try':
                print("blocs try-except")
            case 'except':
                print("gestion d'exception")
            case 'finally':
                print("bloc finally")
            case 'with':
                print("utilisation du gestionnaire de contexte")
            case 'return':
                print("retourner une valeur")
            case 'break':
                print("sortir de la boucle")
            case 'continue':
                print("continuer à l'itération suivante")
            case 'pass':
                print("ne rien faire")
            case 'True':
                print("la condidtion est vrai")
            case 'False':
                print("la condidtion est fause")
            case 'print':
                print("on affiche")
            case _:
                if(self.token_nombre == False):
                    print("variable",self.token)
                else:
                    print("nombre",self.token)

    def Tokenisation(self):
        
        if((self.charactere() or  (self.charactere_actuelle == '_') ) &  (self.token == None)):
            self.token = self.charactere_actuelle    
        elif(self.token != None):
            if(self.fin_de_mot()):
                self.mot_cle()
                self.token = None
                self.token_nombre = False 
                self.Tokenisation()
            else:
                self.token += self.charactere_actuelle               
        elif((self.chiffre()) & (self.token == None)):
            if(self.charactere_actuelle == '0'):
                print("nombre",self.charactere_actuelle)
            else:
                self.token = self.charactere_actuelle
                self.token_nombre = True        
        else:
            match self.charactere_actuelle:
                case '#':
                    while self.charactere_actuelle!='\n':
                        self.lire()
                case ',':
                    print("virgule",self.charactere_actuelle)
                case ':':
                    print("fin de la definion d'une boucle",self.charactere_actuelle)
                case '%':
                    print("reste de la division euclidienne",self.charactere_actuelle)
                case '\n':
                    print("saut de ligne",'\\n')
                    indent=0
                    self.lire()
                    while self.charactere_actuelle == ' ':
                        indent+=1
                        self.lire()
                    self.retour()
                    head = self.pile[0]
                    if head==indent:
                        pass
                    elif head<indent:
                        self.pile = [indent]+self.pile
                        head=self.pile[0]
                        print("BEGIN")
                    else:
                        while head>indent:
                            print("END")
                            self.pile = self.pile[1:]
                            head = self.pile[0]
                            if (head<indent):
                                return "indentation error"         
                case '(':
                    print("parenthèse ouvrante ",self.charactere_actuelle)
                case ')':
                    print("parenthèse fermante ",self.charactere_actuelle)
                case ' ':
                    pass
                case '-':
                    self.binary()
                case '*':
                    self.binary()
                case '+':
                    self.binary()
                case '/':
                    self.binary()
                case '=':
                    self.binary()
                case '<':
                    self.binary()
                case '>':
                    self.binary()
                case '!':
                    self.binary()
                case '&':
                    self.binary()
                case '|':
                    self.binary()
                case _:
                  print("illégale",self.charactere_actuelle)
    

