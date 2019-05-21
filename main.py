"""ToDo."""
from tasks.kyu8 import example
from tasks.kyu5 import solve


def run_example():
    """ToDo"""
    first = input("a: ")
    second = input("b: ")
    print(example(first, second))


def run_solve():
    """Print x out of sequence 'x + 2x**2 + 3x**3 + .. + nx**n'"""
    try:
        limit = float(input("Input a limit: "))
        argument = solve(limit)
        print("The argument is: {}".format(argument))
    except ValueError:
        print("Wrong input data")


if __name__ == '__main__':
    run_example()
    run_solve()
