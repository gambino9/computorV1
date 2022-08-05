import unittest
from exceptions import PolynomialError
from polynomial import Polynomial
from parse import Parser


class PolynomialTest(unittest.TestCase):
    def test_expression_with_wrong_syntax(self):
        letter = "5 + 4 * X + X^2 = X^2 + abc"
        too_many_addition = "5 + 4 * X ++ X^2 = X^2 -- X^2"
        float_exponent = "5 + 4 * X + X^2.3 = X^2 - X^2"

        parser = Parser(letter)
        parser_1 = Parser(too_many_addition)
        parser_2 = Parser(float_exponent)
        with self.assertRaises(PolynomialError):
            parser.first_check()
        with self.assertRaises(PolynomialError):
            parser_1.retrieve_monomials()
        with self.assertRaises(PolynomialError):
            parser_2.retrieve_monomials()

    def test_natural_form(self):
        natural_expression = '9 + 4X + X^2 = +X^2'
        parser = Parser(natural_expression)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 9 + 4X = 0")
        self.assertEqual(solver.degree, '1')
        self.assertEqual(solver.solution, -2.25)

    def test_mixed_natural_and_non_natural_form(self):
        mixed_expression = '9 - 8 - 6X^1 + 0X^2 - 5.6 * X^2 = 3 * X^0'
        parser = Parser(mixed_expression)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : - 2 - 6X - 5.6X^2 = 0")
        self.assertEqual(solver.degree, '2')
        self.assertEqual(solver.solution, '(6 + i√-8.799999999999997) / -11.2')
        self.assertEqual(solver.solution_2, '(6 - i√-8.799999999999997) / -11.2')

    def test_equation_degree_zero(self):
        zero_expression = '5 * X^0 + 4.87 * X^1 = 4.87 * X^1'
        parser = Parser(zero_expression)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 5 = 0")
        self.assertEqual(solver.degree, '0')

    def test_impossible_equation(self):
        impossible_equation = '4 * x^0 = 8 * X^0'
        parser = Parser(impossible_equation)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : - 4 = 0")
        self.assertEqual(solver.degree, '0')
        self.assertEqual(solver.solution, 'No solution')

    def test_all_reel_numbers_are_solution(self):
        impossible_equation_2 = '42 * X^0 = 42 * X^0'
        parser = Parser(impossible_equation_2)

        with self.assertRaises(SystemExit):
            parser.remove_null_values()

    def test_equation_first_degree(self):
        first_degree_expression = '5 * X^0 = 4 * X^0 + 7 * X^1'
        parser = Parser(first_degree_expression)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 1 - 7X = 0")
        self.assertEqual(solver.degree, '1')
        self.assertAlmostEqual(solver.solution, 0.142, 2)

    def test_equation_second_degree_positive_discriminant(self):
        equation = '3 * X^0 + 9 * X^1 + 6 * X^2 = 1 * X^0 + 2 * X^1'
        parser = Parser(equation)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 2 + 7X + 6X^2 = 0")
        self.assertGreater(solver.discriminant, 0)
        self.assertEqual(solver.degree, '2')
        self.assertEqual(solver.solution, -0.5)
        self.assertAlmostEqual(solver.solution_2, -0.666, 2)

    def test_equation_second_degree_null_discriminant(self):
        equation = '6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1'
        parser = Parser(equation)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 5 + 10X + 5X^2 = 0")
        self.assertEqual(solver.discriminant, 0)
        self.assertEqual(solver.degree, '2')
        self.assertEqual(solver.solution, -1)

    def test_equation_second_degree_negative_discriminant(self):
        equation = '7 * X^0 + 4 * X^1 + 3 * X^2 = 3 * X^0 +  0 * X^1'
        parser = Parser(equation)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : 4 + 4X + 3X^2 = 0")
        self.assertEqual(solver.degree, '2')
        self.assertLess(solver.discriminant, 0)
        self.assertEqual(solver.solution, '(-4 + i√-32) / 6')
        self.assertEqual(solver.solution_2, '(-4 - i√-32) / 6')

    def test_equation_third_or_more_degree(self):
        equation = '9 - 8X^0 - 6X^1 + 0X^2 - 5.6 * X^3 = 3 * X^0'
        parser = Parser(equation)
        monomes = parser.remove_null_values()
        solver = Polynomial(monomes)

        self.assertEqual(parser.print_reduced_expression(), "Reduced form : - 2 - 6X - 5.6X^3 = 0")
        self.assertEqual(solver.degree, '3')
        self.assertEqual(solver.solution, 'unsolvable')


if __name__ == "__main__":
    unittest.main()
