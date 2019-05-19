"""ToDo."""
from tasks.kyu8 import example, litres


def run_example():
    """ToDo"""
    first = int(input("a: "))
    second = int(input("b: "))
    print(example(first, second))


def run_litres():
    """Run Litres"""
    time = input("time: ")
    print(litres(time))


if __name__ == '__main__':
    run_example()
    run_litres()
