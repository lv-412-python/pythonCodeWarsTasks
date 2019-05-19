"""ToDo."""
from tasks.kyu8 import example
from tasks.kyu7 import sequence_sum


def run_example():
    """ToDo"""
    first = int(input("a: "))
    second = int(input("b: "))
    print(example(first, second))


def run_sequence_sum():
    """ run sequence_sum() """
    begin_number = int(input("begin number: "))
    end_number = int(input("end number: "))
    step = int(input("step: "))
    print(sequence_sum(begin_number, end_number, step))

if __name__ == '__main__':
    run_example()
    run_sequence_sum()
