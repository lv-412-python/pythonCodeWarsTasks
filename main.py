"""ToDo."""
from tasks.kyu8 import example
from tasks.kyu5 import artificial_rain

def run_example():
    """ToDo"""
    first = int(input("a: "))
    second = int(input("b: "))
    print(example(first, second))


def run_artificial_rain():
    """ run artificial_rain() """
    input_string = input("Enter a list element separated by space: ")
    garden = input_string.split()
    print(artificial_rain(garden))

if __name__ == '__main__':
    run_example()
    run_artificial_rain()
