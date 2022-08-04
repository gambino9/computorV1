# Entree bien formattees mais potentiellement mal gerees (coefficients nuls, negatifs, pas entiers...)
# Equation de degre 0 : 5 * X^ 0 = 5 * X^ 0 ---> Tout les nombres reels sont solutions
# 5 * X^ 0 = 5 * X^ 0
# 42 * X^0 = 42 * X^0

# Equation impossible : ex : 4 * x^0 = 8 * X^0 ---> Le programme doit dire qu'il n'y a pas de solution  --> OUI

# Equation de degre 1 : Le programme doit afficher la bonne solution 5 * X^0 = 4 * X^0 + 7 * X^1 --> OUI

# Equation second degre discriminant positif : ex : 5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1 ---> Doit afficher que le discriminant est strictement positif + afficher deux solutions, est-ce que c'est les bonnes ?  --> Normalement OUI
# Equation second degre discriminant nul : ex : 6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1 ---> Le programme doit afficher discriminant nul et afficher la bonne unique solution --> OUI
# Equation second degre discriminant negatif : ex : 5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1 ---> Discriminant negatif et deux bonnes solutions complexes  -> OUI
# Equation degre 3 ou plus : Ne resout pas et ne plante pas
# Bonus :
# Prouver les erreurs de syntaxes, entrees sous forme naturelle, fraction irreductible quand c'est cense, etapes intermediaires, etc...


import unittest
from exceptions import PolynomialError
from main import main


class PolynomialTest(unittest.TestCase):
    def test_expression_with_wrong_syntax(self):
        letter = "5 + 4 * X + X^2 = X^2 + abc"
        too_many_addition = "5 + 4 * X ++ X^2 = X^2 -- X^2"
        float_exponent = "5 + 4 * X + X^2.3 = X^2 - X^2"

        self.assertEqual(main(letter), "ERROR : There must be no alphabetical characters in the expression.")
        self.assertEqual(main(too_many_addition), "ERROR : The polynomial expression is syntactically incorrect")
        self.assertEqual(main(float_exponent), "ERROR : The polynomial expression is syntactically incorrect")

    def test_natural_form(self):
        natural = '9 + 4X + X^2 = +X^2'
        pass

    def test_mixed_natural_and_non_natural_form(self):
        mixed_expression = '9 - 8X^0 - 6X^1 + 0X^2 - 5.6 * X^3 = 3 * X^0'
        pass

    def test_equation_degree_zero(self):
        pass

    def test_impossible_equation(self):
        pass

    def test_equation_first_degree(self):
        pass

    def test_equation_second_degree_positive_discriminant(self):
        pass

    def test_equation_second_degree_null_discriminant(self):
        pass

    def test_equation_second_degree_negative_discriminant(self):
        pass

    def test_equation_third_or_more_degree(self):
        pass


if __name__ == "__main__":
    unittest.main()
