"""ToDo."""
from tasks.kyu5 import fib_product


def run_fib_product():
    """
    Runs fib_product function.
    """
    try:
        prod = int(input("Enter product of 2 numbers: "))
        print(fib_product(prod))
    except ValueError:
        print("Wrong input!")


if __name__ == '__main__':
    run_fib_product()
