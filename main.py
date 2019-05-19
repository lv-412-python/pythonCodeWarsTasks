"""ToDo."""
from tasks.kyu8 import example
from tasks.kyu8 import Point, Circle, circle_area


def run_example():
    """ToDo"""
    first = int(input("a: "))
    second = int(input("b: "))
    print(example(first, second))


def run_circle_area():
    """Prints the are of a circle"""
    x_point = int(input('Input x: '))
    y_point = int(input('Input y: '))
    point = Point(x_point, y_point)
    radius = int(input('Input radius: '))
    circle = Circle(point, radius)
    area = circle_area(circle)
    print("The area of circle: {}".format(area))


if __name__ == '__main__':
    run_example()
    run_circle_area()
