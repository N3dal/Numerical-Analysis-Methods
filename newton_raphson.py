"""
newton raphson method.
"""


from tools import (clear,
                   math_eval,
                   approximate_error,
                   create_table_row,
                   plt)

clear()


def newton_raphson(math_function: str, function_derivative: str, x0: int, iteration: int = 100, tolerance: float = 0.003):
    """"""

    # first evaluated our functions.
    func = math_eval(math_function)
    func_derivative = math_eval(function_derivative)

    iter_count = 0
    error = 1.0
    xn

    while iter_count < iteration or error < tolerance:
        pass


def main():
    pass


if __name__ == "__main__":
    newton_raphson("x^2-5*x+6", "2*x-5", x0=1)
