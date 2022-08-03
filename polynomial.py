class Polynomial:
    def __init__(self, reduced_expression: dict) -> None:
        self.a = None
        self.b = None
        self.c = None
        self.discriminant = None
        # self.degree = None
        self.degree = max(reduced_expression.keys())
        self.reduced_expression = reduced_expression

        self.identify_a_b_c()
        self.calculate_discriminant()
        self.identify_equation_degree(self.reduced_expression)

    def ft_power(self, x, y, z=None):
        power = 1
        # print(f'{x=}, {y=}')

        for i in range(1, y + 1):
            power = power * x
        return power

    def ft_square_root(self, x):
        # sqrt = self.ft_power(x, 0.5)
        sqrt = x ** 0.5  # TODO : May be forbidden in subject
        return sqrt

    def identify_a_b_c(self) -> None:
        self.a = self.reduced_expression.get('2', 0)
        self.b = self.reduced_expression.get('1', 0)
        self.c = self.reduced_expression.get('0', 0)

    def calculate_discriminant(self):
        discriminant = self.ft_power(self.b, 2) - (4 * self.a * self.c)
        return discriminant

    def identify_equation_degree(self, reduced_expression: dict) -> None:
        print(f'Polynomial degree : {self.degree}')  # TODO : Find place where to print it properly

        if self.degree == '0':
            pass
        elif self.degree == '1':  # forme ax + b = 0
            self.solve_first_degree_equation()
        elif self.degree == '2':
            discriminant = self.calculate_discriminant()
            self.solve_second_degree_equation(discriminant)

    def solve_second_degree_equation(self, discriminant):
        if discriminant > 0:
            x1 = (-self.b + self.ft_square_root(discriminant)) / (2 * self.a)
            x2 = (-self.b - self.ft_square_root(discriminant)) / (2 * self.a)
            print(f"The discriminant is strictly positive, the two solutions are :\n{x1}\n{x2}")
        elif discriminant == 0:
            # print(f'{self.b=}, {self.a=}')
            x1 = ((-self.b) / (2 * self.a))
            print(f"The solution is : {x1}")
        elif discriminant < 0:
            x1 = f"({-self.b} + i√{discriminant}) / 2*{self.a}"
            x2 = f"({-self.b} - i√{discriminant}) / 2*{self.a}"
            print(f"The discriminant is strictly negative, the two complex solutions are :\n{x1}\n{x2}")

    # forme b * X + c
    def solve_first_degree_equation(self):
        if self.a == 0:  # P(x) = b
            print(f'{self.b}, {self.c}')
            solution = (-self.c / self.b)
            print(f"The solution is :\n{solution}")
        # Add here elif for special case when all reel number can be a solution (ax^0 = zx^0)
        else:
            solution = (-self.b) / self.a
            print(f"The solution is :\n{solution}")  # TODO : check this maybe it's redundant or false
