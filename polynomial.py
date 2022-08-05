from typing import Union


class Polynomial:
    def __init__(self, reduced_expression: dict) -> None:
        self.a = None
        self.b = None
        self.c = None
        self.discriminant = None
        self.solution = None
        self.solution_2 = None
        self.degree = max(reduced_expression.keys())
        self.reduced_expression = reduced_expression

        self.identify_a_b_c()
        self.discriminant = self.calculate_discriminant()
        self.identify_equation_degree()

    def ft_square_root(self, x: Union[int, float]) -> Union[int, float]:
        sqrt = x ** 0.5
        return sqrt

    def identify_a_b_c(self) -> None:
        self.a = self.reduced_expression.get('2', 0)
        self.b = self.reduced_expression.get('1', 0)
        self.c = self.reduced_expression.get('0', 0)

    def calculate_discriminant(self):
        discriminant = self.b**2 - (4 * self.a * self.c)
        return discriminant

    def identify_equation_degree(self) -> None:
        print(f'Polynomial degree : {self.degree}')
        if self.degree == '0':
            self.solution = 'No solution'
            print(f'This equation has no solution.')
        elif self.degree == '1':  # forme ax + b = 0
            self.solve_first_degree_equation()
        elif self.degree == '2':
            self.solve_second_degree_equation()
        elif int(self.degree) > 2:
            self.solution = 'unsolvable'
            print("The polynomial degree is strictly greater than 2, I can't solve it.")

    # aX^2 + bX + c form
    def solve_second_degree_equation(self):
        if self.discriminant > 0:
            self.solution = (-self.b + self.ft_square_root(self.discriminant)) / (2 * self.a)
            self.solution_2 = (-self.b - self.ft_square_root(self.discriminant)) / (2 * self.a)
            print(f"The discriminant is strictly positive, the two solutions are :\n{self.solution}\n{self.solution_2}")
        elif self.discriminant == 0:
            self.solution = ((-self.b) / (2 * self.a))
            print(f"The discriminant is equal to 0. The solution is : \n{self.solution}")
        elif self.discriminant < 0:
            self.solution = f"({-self.b} + i√{self.discriminant}) / {2 * self.a}"
            self.solution_2 = f"({-self.b} - i√{self.discriminant}) / {2 * self.a}"
            print(f"The discriminant is strictly negative, the two complex solutions are :\n{self.solution}\n{self.solution_2}")

    # bX + c form
    def solve_first_degree_equation(self):
        self.solution = (-self.c / self.b)
        print(f"The solution is :\n{self.solution}")
