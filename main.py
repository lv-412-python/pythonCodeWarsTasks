"""ToDo."""
from tasks.kyu8_2 import validate_usr
from tasks.kyu8 import short_long_short

def main():
    """ THis function is entry point of program"""
    username = str(input("Enter your username: "))
    print((validate_usr(username)))

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
    main()
    run_sls()
