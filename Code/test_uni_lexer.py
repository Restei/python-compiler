from analyse_lexicale.fonction_lexicale import Lexeur
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
        input_code = "var@iable = 42"  # '@' est un caractère invalide
        Lex1 = Lexeur(input_code)
        Tokens, errors = Lex1.Tokenisation()

        # Vérifier qu'il y a bien une erreur
        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un caractère inconnu.")
        
        # Vérifier qu'il y a des tokens
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le code avec un caractère inconnu.")

    def test_invalid_number_with_letters(self):
        """
        Tester un cas où un nombre contient des lettres.
        """
        input_code = "123abc"  # Nombre contenant des lettres
        Lex1 = Lexeur(input_code)
        Tokens, errors = Lex1.Tokenisation()

        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre avec des lettres.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le code avec un nombre contenant des lettres.")

    def test_invalid_number_starting_with_zero(self):
        """
        Tester un cas où un nombre commence par zéro.
        """
        input_code = "007"  # Nombre commençant par zéro
        Lex1 = Lexeur(input_code)
        Tokens, errors = Lex1.Tokenisation()

        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre débutant par zéro.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le code avec un nombre commençant par zéro.")

    def test_invalid_indentation(self):
        """
        Tester un cas où l'indentation est incorrecte.
        """
        input_code = "def foo():\n  print('Hello')\n    print('World')"  # Mauvaise indentation
        Lex1 = Lexeur(input_code)
        Tokens, errors = Lex1.Tokenisation()

        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour une indentation incorrecte.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le code avec une mauvaise indentation.")

    def test_too_long_number(self):
        """
        Tester un cas où le nombre est trop long.
        """
        input_code = "123456789012345678901234567890123456789012345678901234567890"  # Nombre > 50 chiffres
        Lex1 = Lexeur(input_code)
        Tokens, errors = Lex1.Tokenisation()

        self.assertGreater(len(errors), 0, "Aucune erreur lexicale n'a été détectée pour un nombre trop long.")
        self.assertGreater(len(Tokens), 0, "Aucun token n'a été généré pour le code avec un nombre trop long.")


if __name__ == "__main__":
    unittest.main()
