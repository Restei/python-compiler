from analyse_lexicale.fonction_lexicale import Lexeur, lire_fichier
from analyse_lexicale.token import TokenType, BaseToken
import unittest


class TestLexeur(unittest.TestCase):

    def setUp(self):
        """
        Préparer la configuration nécessaire avant chaque test.
        """
        pass  # Aucune initialisation spéciale pour le lexeur

    def test_invalid_character_in_variable(self):
        """
        Tester un cas où un caractère inconnu est utilisé dans une variable.
        """
        path = "mini_python/err_lex/"
        file = path + "erreur_inconnue.py"
        
        Lex1 = Lexeur(lire_fichier(file))
        Tokens, errors = Lex1.Tokenisation()

        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        # Vérifier qu'il y a bien une erreur
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un caractère inconnu.")
        
        # Vérifier qu'il y a des tokens
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le fichier avec un caractère inconnu.")

    def test_invalid_number_with_letters(self):
        """
        Tester un cas où un nombre contient des lettres.
        """
        path = "mini_python/err_lex/"
        file = path + "erreur_nombre_avec_lettres.py"
        
        Lex1 = Lexeur(lire_fichier(file))
        Tokens, errors = Lex1.Tokenisation()

        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre avec des lettres.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le fichier avec un nombre contenant des lettres.")

    def test_invalid_number_starting_with_zero(self):
        """
        Tester un cas où un nombre commence par zéro.
        """
        path = "mini_python/err_lex/"
        file = path + "erreur_nombre_zero.py"
        
        Lex1 = Lexeur(lire_fichier(file))
        Tokens, errors = Lex1.Tokenisation()

        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre débutant par zéro.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le fichier avec un nombre commençant par zéro.")

    def test_invalid_indentation(self):
        """
        Tester un cas où l'indentation est incorrecte.
        """
        path = "mini_python/err_lex/"
        file = path + "erreur_indentation.py"
        
        Lex1 = Lexeur(lire_fichier(file))
        Tokens, errors = Lex1.Tokenisation()

        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour une indentation incorrecte.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le fichier avec une mauvaise indentation.")

    def test_too_long_number(self):
        """
        Tester un cas où le nombre est trop long.
        """
        path = "mini_python/err_lex/"
        file = path + "erreur_nombre_trop_long.py"
        
        Lex1 = Lexeur(lire_fichier(file))
        Tokens, errors = Lex1.Tokenisation()

        if errors:
            print(f"Erreurs de tokenisation dans {file} : {errors}")
        
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre trop long.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le fichier avec un nombre trop long.")

    
if __name__ == "__main__":
    unittest.main()
