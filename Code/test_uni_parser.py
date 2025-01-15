from analyse_lexicale.fonction_lexicale import Lexeur, lire_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.fonction_syntaxique import *
import unittest


class TestParser(unittest.TestCase):

    def setUp(self):
        """
        Préparer la configuration nécessaire avant chaque test.
        """
        
        self.ll1_table = tableau_des_symboles_directeur_ll1_ultime

    

    def test_invalid_case(self):
        """
        Tester un cas où la chaîne ne peut pas être analysée correctement.
        """
        path = "mini_python/err_synt/"
        file = path + "invalid_syntax.py"
        
        
        Lex1 = Lexeur(lire_fichier(file))
        
        
        Tokens, errors = Lex1.Tokenisation()

        
        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
       
        result = parse_with_tokens(self.ll1_table, Tokens, file)
        
        
        self.assertFalse(result, "Le parsing a réussi alors qu'il aurait échoué.")

    def test_unexpected_token(self):
        """
        Tester un cas avec un token inattendu.
        """
        path = "mini_python/err_synt/"
        file = path + "unexpected_token.py"
        
        
        Lex1 = Lexeur(lire_fichier(file))
        
        
        Tokens, errors = Lex1.Tokenisation()

        
        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        
        result = parse_with_tokens(self.ll1_table, Tokens, file)
        
        
        self.assertFalse(result, "Le parsing a échoué alors qu'un token inattendu était présent.")

  
        

        


if __name__ == "__main__":
    unittest.main()
