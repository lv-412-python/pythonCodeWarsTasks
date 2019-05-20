"""ToDo."""
from tasks.kyu8 import square_or_square_root


def Run():
    """ToDo."""
    try:
        input_ = input("Enter a sequence of numbers separated by a space -    ")
        input_list = [int(number) for number in input_.split(' ')]
        print(square_or_square_root(input_list))
    except ValueError:
        print("You must enter only numbers.")

if __name__ == '__main__':
    Run()
