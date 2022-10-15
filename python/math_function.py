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

        return a math function that we can,
        evaluate.


        + => for addition.
        - => for subtraction.
        * => for multiplication.
        / => for division.
        ^ => for power.
        -x => for negative numbers.

        and you can use parentheses => '(' or ')'.

        note: you can only have only one main variable.
        note: spaces is allowed but try to avoid using them.

        valid examples:
            func(3) = 3*x+23/3^2
            func(3.3) = 8-12*23-2 * -7
            func(3.3) = 8-12*23-2*-7

        non-valid examples:
            func(3) = 3*xy23/234
            func(-1) = 12y+7 and the main-variable is x.
            func(-2) = 23&34|5!math.

            so you can't use any symbols except the symbols that,
            in SYMBOLS.

    """
    # the symbols that we only want to be on our math_function.
    __SYMBOLS = (
        " ",  # space;
        "+",
        "-",
        "^",
        "/",
        "*",
        "(",
        ")"
    )

    def __init__(self, math_function: str):

        # make sure to lower everything;
        self.math_function = math_function.lower()

        # get all the function variables;
        self.math_function_variables = self.__function_variables()

        # the only symbols allowed for for math function;
        # we do this because we need to add the variable to,
        # be allowed;
        self.__symbols = [*MathFunction.__SYMBOLS,
                          *self.math_function_variables]

    def eval(self, variable_value=None):
        """
            evaluate the math-function with the given "variable";

            return number;
        """

        # guard-condition;
        if not variable_value:
            # if our variable_value is empty;
            return self.math_function

        if not all(symbol in self.__symbols or symbol.isdecimal()
                   for symbol in self.math_function):
            # if everything not ok and our math_function,
            # contain other symbols or other variables.
            raise Exception("theres symbols that is not allowed")

        self.math_function = self.math_function.replace("^", "**")

        return eval(self.math_function.replace(self.math_function_variables[0], str(variable_value)))

    def __function_variables(self):
        """
            return all the function variables;


            return [str];
        """

        return [var for var in self.math_function if var.isalpha()]

    def __call__(self, variable_value=None):
        """"""

        return self.eval(variable_value)


fx = MathFunction("(2*x+3+y)")

print(fx.math_function_variables)
print(fx.math_function)


# print(fx(3))
