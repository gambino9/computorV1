from polynomial import Polynomial
from parse_2 import Parser
from parse import *
import sys


# if __name__ == "__main__":
def main(polynomial_expression: str):
    polynomial = '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'  # classique
    polynomial_2 = '5 * X^0 + 4.87 * X^1 = 4 * X^0'  # avec un coefficient float
    polynomial_3 = '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^2 = 3 * X^0'
    polynomial_4 = '9 + 4 * X + X^2= -X^2'  # avec un int seul
    polynomial_5 = '42 * X^0 = 42 * X^0'
    polynomial_6 = '5 * X^0 = -5 * X^0'
    polynomial_7 = '9 - 8X^0 - 6X^1 + 0X^2 - 5.6 * X^3 = 3 * X^0'  # forme naturelle et non naturelle melangees

    poly_subj = '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'
    poly_subj_1 = '5 * X^0 + 4 * X^1 = 4 * X^0'
    poly_subj_2 = '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0'
    poly_subj_3 = '5 + 4 * X + X^2 = X^2'

    poly_slack = 'X^1 + X^5 = X^5'

    natural = '5 * X^0 + 4.87 * X^1 = 4.87 * X^1'

    try:
        pol = natural
        # print(pol)

        # poly = first_check(pol)
        # left_side_expression, right_side_expression = poly.split('=')
        # concat = shift_right_side_expression(right_side_expression, left_side_expression)
        # retrieved = retrieve_monomials(concat)
        # reduced_dict = reduce_monomials(retrieved)

        # non_null_dict = remove_null_values(reduced_dict)

        # reduced_string = print_reduced_expression(non_null_dict)
        # print(f"{reduced_string=}")

        # if not check_expression_solvability(non_null_dict):  # TODO : Maybe put somewhere else so it can print the degree at the right time
        #     print("The polynomial degree is strictly greater than 2, I can't solve this equation")

        parser = Parser(pol)
        monomes = parser.remove_null_values()
        # print(monomes)
        print(parser.print_reduced_expression())
        Polynomial(monomes)

    except PolynomialError as err:
        print(f"ERROR : {err}")
        # return f"ERROR : {err}"
    # except ValueError as err:
    #     print(f"ERROR : There must be no alphabetical characters in the expression.")
    # finally:
    #     sys.exit()


if __name__ == "__main__":
    arg = sys.argv[1:]
    # if not isinstance(arg, str) or len(arg) > 1 or arg == "":  # TODO : This is not handled correctly
    #     print("ERROR : the argument is not correctly formatted")
    main(str(arg))
