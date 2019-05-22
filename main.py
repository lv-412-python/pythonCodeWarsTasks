"""ToDo."""
from tasks.kyu6 import nba_cup, R
from tasks.kyu5 import fib_product
from tasks.kyu8 import short_long_short

def run_nba_cup():
    """Run nba_cup function""
    team = input('Enter the name of the team:   ')
    print(nba_cup(R, team))

def run_fib_product():
    """
    Runs fib_product function.
    """
    try:
        prod = int(input("Enter product of 2 numbers: "))
        print(fib_product(prod))
    except ValueError:
        print("Wrong input!")

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


if __name__ == '__main__':
    run_sls()
    run_nba_cup()
