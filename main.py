from polynomial import Polynomial
from parse_2 import Parser
from parse import *
import sys


def main(polynomial_expression: str):
    try:
        parser = Parser(polynomial_expression)
        monomials = parser.remove_null_values()
        print(parser.print_reduced_expression())
        Polynomial(monomials)

    except PolynomialError as err:
        print(f"ERROR : {err}")


if __name__ == "__main__":
    inp = sys.argv[1:]
    if not isinstance(inp[0], str) or len(inp) > 1:
        sys.exit("ERROR : the argument is not correctly formatted")
    arg = inp[0]
    main(str(arg))
