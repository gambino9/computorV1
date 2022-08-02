class Polynomial:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.degree = None

    def ft_power(self, x, y, z=None):
        power = 1

        for i in range(1, y + 1):
            power = power * x
        return power

    def ft_square_root(self, x):
        return self.ft_power(x, 0.5)

    # Evaluate degree of equation and
    def which_degree(self, degree):
        print(f"Polynomial degree : {degree}")
        if degree == 0:
            pass
        elif degree == 1:  # forme ax + b = 0
            self.solve_first_degree_equation()
        elif degree == 2:
            discriminant = self.calculate_discriminant(self.a, self.b, self.c)
            self.solve_second_degree_equation(discriminant)
        elif degree > 2:
            print("The polynomial degree is strictly greater than 2, i can't solve.")
            # exit(0)

    def calculate_discriminant(self, a, b, c):
        discriminant = self.ft_power(b, 2) - (4 * a * c)
        return discriminant

    def solve_second_degree_equation(self, discriminant):
        if discriminant > 0:
            x1 = (-self.b + self.ft_square_root(discriminant)) / 2 * self.a
            x2 = (-self.b - self.ft_square_root(discriminant)) / 2 * self.a
            print(f"The discriminant is strictly positive, the two solutions are :\n{x1}\n{x2}")
        elif discriminant == 0:
            x1 = ((-self.b) / (2*self.a))
            print(f"The solution is : {x1}")
        elif discriminant < 0:
            x1 = f"({-self.b} + i√{discriminant}) / 2*{self.a}"
            x2 = f"({-self.b} - i√{discriminant}) / 2*{self.a}"
            print(f"The discriminant is strictly negative, the two complex solutions are :\n{x1}\n{x2}")

    def solve_first_degree_equation(self):
        if self.a == 0:  # P(x) = b
            print("The solution is :\n")
        # Add here elif for special case when all reel number can be a solution (ax^0 = zx^0)
        else:
            solution = (-self.b) / self.a
            print(f"The solution is :\n{solution}")

    # For a polynomial expression as follows : AX^2 + BX + C
    def identify_a_b_c(self, reduced_expression: dict) -> None:
        self.a = reduced_expression.get('2', 0)
        self.b = reduced_expression.get('1', 0)
        self.c = reduced_expression.get('0', 0)
