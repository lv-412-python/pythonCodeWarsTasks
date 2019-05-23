"""ToDo."""
from tasks.kyu5 import fib_product, moving_shift, demoving_shift
from tasks.kyu8 import short_long_short, litres, starting_mark
from tasks.kyu6 import interp
from tasks.kyu7 import sum_of_square



def run_fib_product():
    """
    Runs fib_product function.
    """
    try:
        prod = int(input("Enter product of 2 numbers: "))
        print(fib_product(prod))
    except ValueError:
        print("Wrong input!")

def run_sum_of_square():
    """ THis function is entry point of program"""
    try:
        binomial_coefficients = int(input("Enter your binomial coefficients: "))
        print('Your sum of the squares: {}'.format(
            sum_of_square(binomial_coefficients)))
    except ValueError:
        print('Please enter integer')


def run_litres():
    """ run litres """
    try:
        time = float(input("enter time: "))
        print(litres(time))
    except ValueError:
        print("Wrong input!")


def run_interp():
    """ This function is entry point of program"""
    try:
        func = str(input('Enter string or trigonometric function: '))
        l_a = float(input('Enter float value l: '))
        u_b = float(input('Enter float value u: '))
        n_c = int(input("Enter integer value n: "))
        print('Your intermediate results: {}'.format(interp(func, l_a, u_b, n_c)))
    except ValueError:
        print('Please check input value ')

def run_sls():
    """
    Runs short_long_short function.
    """
    first_str = input("Enter string: ")
    second_str = input("Enter another string: ")
    while len(first_str) == len(second_str):
        print("String can't be the same length.")
        first_str = input("Enter string: ")
        second_str = input("Enter another string: ")
    print(short_long_short(first_str, second_str))

def run_moving_shift():
    """ This function is entry point of program"""
    try:
        plain_text = str(input('Enter your message: '))
        shift = int(input('Enter shift: '))
        encrypted_message = moving_shift(plain_text, shift)
        print('Your encrypted message: {}'.format(encrypted_message))
        print('Your decrypted message: {}'.format(demoving_shift(encrypted_message, shift)))
    except ValueError:
        print('Please check input value ')

def run_starting_mark():
    """ run starting_mark """
    try:
        height = float(input("enter height: "))
        print(starting_mark(height))
    except ValueError:
        print("Wrong input!")


if __name__ == '__main__':

    run_sls()
    run_moving_shift()
    run_fib_product()
    run_interp()
    run_litres()
    run_sum_of_square()
    run_starting_mark()
