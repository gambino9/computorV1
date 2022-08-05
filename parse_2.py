# regex for a monomial : "^\s*[+-]?\s*(\d+(?:\.\d+)?)?\s*(([\*]?)\s*(([X]\s*)(?(4)(\^)(\s*(\d+(?!\.)))|)?))?\s*"
# split whitespaces
# https://regex101.com/r/pC4Aud/1

# Without spaces : "^([+-])?(\d+(?:\.\d+)?)?([\*]?)(([X])(?(5)(\^)(\d+(?!\.))|)?)?"

# 1st capturing group : ([+-])?
# 1st character may be a "-" or "+", but it is optional

# 2nd capturing group : (\d+(?:\.\d+)?)?
# May be an int (\d+) or a float, or nothing. (\.\d+)
# (?:...) matches everything enclosed

# 3rd capturing group : ([\*]?)
# A single "*" can be match, but is also optional

# 4th capturing group : (([X])(?(5)(\^)((\d+(?!\.)))|)?)?
# 5th capturing group : ([X])
# 6th capturing group : (\^)
# 7th capturing group : (\d+(?!\.))

# 4th capturing group : a conditional statement enclosing 5th, 6th, 7th
# groups. If 5th group returns a match, the pattern before the "|" is matched
# otherwise, the pattern after the "|" is matched. Here, it allows us to check
# that an "X" character is matched before we try to match 6th capturing
# group "^" char and what comes after. In other words, "^\d" is dependant on
# a "X" char presence to be matched.

# 7th capturing group : Only accepts an int after the "^" char. Float are
# explicitly forbidden with the negative lookahead(?!...), that ensures that
# the float pattern will not match

from collections import Counter
from exceptions import PolynomialError
import re
import ast
import sys

# monomial_pattern = re.compile(r"([+-])?(\d+(?:\.\d+)?)?([*]?)((X)(?(5)(\^)(\d+(?!\.))|)?)?")
# testtttt_pattern = re.compile(r"((([+-])?((\d+(?:\.\d+)?)(?(5)[*]?|))?)((X)(?(7)(\^)(\d+(?!\.))|)?)?){1,1}")
testtttt_pattern = re.compile(
    r"([+-])?(\d+(?:\.\d+)?)(?(2)[*]?|)((X)(?(4)(\^)(\d+(?!\.))|)?)|([+-])?(\d+(?:\.\d+)?)|([+-])?((X)(?(11)(\^)(\d+(?!\.))|)?){1,1}")

monomial_regex = r"([+-])?(\d+(?:\.\d+)?)(?(2)[*]?|)((X)(?(4)(\^)(\d+(?!\.))|)?)|([+-])?(\d+(?:\.\d+)?)|([+-])?((X)(?(11)(\^)(\d+(?!\.))|)?){1,1}"


class Parser:
    def __init__(self, polynomial_expression: str) -> None:
        self.polynomial_expression = polynomial_expression

    def first_check(self) -> str:
        """
        Checks if expression contains letters, is empty, doesn't have '='
        """
        polynomial_string = self.polynomial_expression.upper()
        polynomial_string = polynomial_string.replace(" ", "")
        if any(letter.isalpha() and letter != 'X' for letter in polynomial_string):
            raise PolynomialError("There must be no alphabetical characters in the expression.")
        if polynomial_string == "":
            raise PolynomialError("The expression must not be empty.")
        if Counter(polynomial_string)['='] != 1:
            raise PolynomialError("The expression must contains the equal sign")
        if polynomial_string.split('=')[0] == "" or polynomial_string.split('=')[1] == "":
            raise PolynomialError("The expression is wrongly formatted.")
        return polynomial_string

    def check_len_string(self, retrieved_poly: str, poly: str) -> None:
        """
        Check for syntactical errors by checking len of polynomial expression
        """
        poly_len = sum(not char.isspace() for char in poly)
        if len(retrieved_poly) != poly_len:
            raise PolynomialError("The polynomial expression is syntactically incorrect")

    def shift_right_side_expression(self) -> str:
        """
        Inverts mathematical signs of right expression and concatenate
         with left expression. Returns concatenation
        """
        polynomial_string = self.first_check()
        left_side, right_side = polynomial_string.split('=')
        if right_side[0] != '+' and right_side[0] != '-':
            right_side = "".join(["+", right_side])
        res = right_side.replace('+', 'tmp').replace('-', '+').replace('tmp', '-')
        merged_expression = "".join([left_side, res])
        return merged_expression

    def retrieve_monomials(self) -> dict:
        """
        Retrieves monomials from string using regex and stores them in dictionary
        """
        polynomial = self.shift_right_side_expression()
        monomial_pattern = re.compile(monomial_regex)
        iter_pattern = monomial_pattern.finditer(polynomial)
        monomials_dict = {}
        len_string = ''
        for index, monomial in enumerate(iter_pattern):
            monomials_dict[index] = monomial.group()
            len_string += monomial.group()
        self.check_len_string(len_string, polynomial)
        return monomials_dict

    def reduce_monomials(self) -> dict:
        """
        Takes dictionary of monomials and computes the constants
        Returns the reduced form as a dictionary
        """
        monomials = self.retrieve_monomials()
        degree_dict = {}
        for monomial in monomials.values():
            if 'X' in monomial:
                if '^' not in monomial:
                    exponent = '1'
                else:
                    exponent = monomial.split('^')[1]
                if exponent not in degree_dict:
                    degree_dict[exponent] = 0
                if '*' in monomial:
                    constant = monomial.split('*')[0]
                else:
                    constant = monomial.split('X')[0]
                    try:
                        isinstance(ast.literal_eval(constant), int) or isinstance(ast.literal_eval(constant), float)
                    except SyntaxError:
                        if constant == '+' or constant == '':
                            constant = '1'
                        elif constant == '-':
                            constant = '-1'
                degree_dict[exponent] += ast.literal_eval(constant)
            else:
                constant = monomial
                exponent = '0'
                if exponent not in degree_dict:
                    degree_dict[exponent] = 0
                degree_dict[exponent] += ast.literal_eval(constant)

        return degree_dict

    def remove_null_values(self) -> dict:
        """
        Remove the monomials which constants are equal to zero
        After, checks if dict is empty, if so, all reel numbers are solution
        """
        monomials_dict = self.reduce_monomials()
        null_values = [key for key in monomials_dict if monomials_dict[key] == 0]
        for null_key in null_values:
            del monomials_dict[null_key]
        if not monomials_dict:
            print("All reel numbers are solutions")
            sys.exit()
        else:
            return monomials_dict

    def print_reduced_expression(self) -> str:
        """
        Iterate through the monomials dictionary to print
        the expression under a natural and reduced form
        """
        reduced_dict = self.remove_null_values()
        reduced_string = ""
        sorted_reduced_dict = dict(sorted(reduced_dict.items(), key=lambda x: x[0]))
        for k, v in sorted_reduced_dict.items():
            if k == '0':
                reduced_string += f"{['', '+ '][v >= 0] or ['', '- '][v < 0]}{str(abs(v))} "
            elif k == '1':
                reduced_string += f"{['', '+ '][v >= 0] or ['', '- '][v < 0]}{str(abs(v))}X "
            else:
                reduced_string += f"{['', '+ '][v >= 0] or ['', '- '][v < 0]}{str(abs(v))}X^{k} "
        if reduced_string[0] == '+':
            reduced_string = reduced_string[2:]
        reduced_string += "= 0"
        return "Reduced form : " + reduced_string

