"""ToDo."""
from tasks.kyu8 import example
from tasks.kyu6 import approxi

def run_example():
    """ToDo"""
    first = int(input("a: "))
    second = int(input("b: "))
    print(example(first, second))


def run_approxi():
    """ run approxi() """
    num = float(input("num: "))
    print(approxi(num))

if __name__ == '__main__':
    run_example()
    run_approxi()
