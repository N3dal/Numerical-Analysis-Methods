"""

create custom math function;

so we can use those object to create math functions,
and evaluate them;

using MathFunction we can create math-function in python;

"""


from math import (sin, cos, tan)
from tools import Tools


Tools.clear()


class MathFunction:
    """
        to create your "math-equations => function" in python;
    """

    def __init__(self, math_function: str):

        self.math_function = math_function

        # get all the function variables;
        self.math_function_variables = self.__function_variables()

    def eval(self, variable_value=None):
        """
            evaluate the math-function with the given "variable";

            return number;
        """

    def __function_variables(self):
        """
            return all the function variables;


            return [str];
        """

        return [var for var in self.math_function if var.isalpha()]

    def __call__(self, variable_value):
        """"""

        return self.eval(variable_value)


fx = MathFunction("2x+3")

print(fx.math_function_variables)
print(fx.math_function)


fx(3)
