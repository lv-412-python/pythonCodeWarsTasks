"""ToDo."""
from tasks.kyu5 import (
    fib_product,
    moving_shift,
    demoving_shift,
    artificial_rain,
    zeros,
    gap_in_primes,
    smallest,
    prime_factors,
    solve
)
from tasks.kyu8 import (
    short_long_short,
    litres,
    starting_mark,
    duty_free,
    validate_usr,
    fix_the_meerkat,
    square_or_square_root,
    heads_legs,
    volume_of_a_cuboid,
    miles_per_gallon_to_kilometers_per_liter,
    am_i_wilson,
    two_decimal_places,
    abbrev_name,
    bin_to_decimal,
    Circle,
    Point,
    circle_area,
    divisible_by
)
from tasks.kyu6 import (
    interp,
    approximation,
    bouncing_ball,
    nba_cup, R,
    variance_rainfall,
    balance,
    consonant_value,
    find_nb
)
from tasks.kyu7 import (
    sum_of_square,
    sequence_sum,
    triple_shiftian,
    replicate,
    where_is_vasya,
    new_avg,
    angle,
    series_sum
)
from utils.utils import (
    integer_list_input,
    float_input,
    integer_input
)

__all__ = ['run_bouncing_ball', 'run_heads_legs', 'run_fib_product',
           'run_sum_of_square', 'run_litres', 'run_interp',
           'run_short_long_short', 'run_moving_shift', 'run_starting_mark',
           'run_sequence_sum', 'run_approximation', 'run_artificial_rain',
           'run_duty_free', 'run_validate_usr', 'run_fix_the_meerkat',
           'run_square_or_square_root', 'run_replicate', 'run_nba_cup',
           'run_triple_shiftian', 'run_gap_in_primes', 'run_variance_rainfall',
           'run_where_is_vasya', 'run_volume_of_a_cuboid',
           'run_miles_per_gallon_to_kilometers_per_liter', 'run_am_i_wilson',
           'run_new_avg', 'run_balance', 'run_smallest', 'run_two_decimals_places',
           'run_abbrev_name', 'run_bin_to_decimal', 'run_angle',
           'run_consonant_value', 'run_prime_factors', 'run_circle_area', 'run_divisible_by',
           'run_series_sum', 'run_find_nb', 'run_solve']

def get_docstring(func=None):
    '''finds docstring'''
    try:
        print(eval(func[4:]).__doc__)
    except:
        print("Sorry, but I don't have this function")


def run_bouncing_ball():
    """Runs bouncing_ball function."""
    print("Enter height(must be greater than 1.5): ")
    height = float_input(minimum=1.5)
    print("Enter bounce of the ball(between 0 and 1): ")
    bounce = float_input(minimum=0, maximum=1)
    print("Ball will be seen from the window this amount of times: {}".format(
        bouncing_ball(height, bounce)))


def run_heads_legs():
    """Runs heads_legs function."""
    print("Enter the amount of heads on the farm: ")
    heads = integer_input(maximum=1000, positive=True)
    print("Enter the amount of legs on the farm: ")
    legs = integer_input(maximum=1000, positive=True)
    print("Number of chickens and rabbits is: {}".format(
        heads_legs(heads, legs)))


def run_fib_product():
    """Runs fib_product function."""
    print("Enter product of 2 numbers: ")
    prod = integer_input(positive=True)
    print("Entered number is a product of these two numbers: {}".format(
        fib_product(prod)))


def run_sum_of_square():
    """ THis function is entry point of program"""
    binomial_coefficients = integer_input()
    print('Your sum of the squares: {}'.format(
        sum_of_square(binomial_coefficients)))


def run_litres():
    """ run litres """
    print("Enter time of the run")
    time = float_input(positive=True)
    print('You need {} litres of water'.format(litres(time)))


def run_interp():
    """ This function is entry point of program"""
    func = str(input('Enter string or trigonometric function: '))
    print('Value l')
    l_a = float_input(positive=True)
    print('Value u')
    u_b = float_input(positive=True)
    print('Value n')
    n_c = integer_input()
    print('Your intermediate results: {}'.format(interp(func, l_a, u_b, n_c)))


def run_short_long_short():
    """Runs short_long_short function."""
    first_str = input("Enter string: ")
    second_str = input("Enter another string: ")
    while len(first_str) == len(second_str):
        print("String can't be the same length.")
        first_str = input("Enter string: ")
        second_str = input("Enter another string: ")
    print("The result of short+long+short concatenation is {}:".format(short_long_short(first_str, second_str)))


def run_moving_shift():
    """ This function is entry point of program"""
    plain_text = str(input('Enter your message: '))
    print('Shift')
    shift = integer_input()
    encrypted_message = moving_shift(plain_text, shift)
    print('Your encrypted message: {}'.format(encrypted_message))
    print('Your decrypted message: {}'.format(demoving_shift(encrypted_message, shift)))


def run_starting_mark():
    """ run starting_mark """
    print("Enter athlete height between 1.22 and 2.13 meters:")
    height = float_input(minimum=1.22, maximum=2.13)
    print("best starting mark is {} meters from pole".format(starting_mark(height)))


def run_sequence_sum():
    """ run sequence sum """
    print("Start of sequence: ")
    begin_number = integer_input()
    print("End of sequence: ")
    end_number = integer_input()
    print("Step: ")
    step = integer_input()
    print("sum of sequence = {}".format(sequence_sum(begin_number, end_number, step)))

def run_approximation():
    """ run approximation """
    number = float_input(positive=True)
    print(print("approximation of {} near 0 = {}".format(number, approximation(number))))


def run_artificial_rain():
    """ run artificial rain """
    print("enter sections of your garden")
    garden = integer_list_input()
    print("maximal number of watered sections: {}".format(artificial_rain(garden)))


def run_duty_free():
    """ This function is entry point of program"""
    print('Price')
    price = integer_input(positive=True)
    print('Discount')
    discount = integer_input(positive=True)
    print('Holiday cost')
    holiday_cost = integer_input(positive=True)
    print('You can buy {} bottles of whiskey:D'.format(
        duty_free(price, discount, holiday_cost)))


def run_validate_usr():
    """ This function is entry point of program"""
    username = str(input("Enter your username: "))
    print((validate_usr(username)))


def run_fix_the_meerkat():
    """Run fix_the_meerkat function"""
    animal = ['', '', '']
    animal[0] = input("Please enter 'tail': ").lower()
    animal[1] = input("Please enter 'body': ").lower()
    animal[2] = input("Please enter 'head': ").lower()
    print(fix_the_meerkat(animal))


def run_square_or_square_root():
    """Run square_or_square_root function"""
    input_list = integer_list_input()
    print(square_or_square_root(input_list))


def run_replicate():
    """Run replicate function"""
    times = integer_input(positive=True)
    number = integer_input(positive=True)
    print(replicate(times, number))


def run_nba_cup():
    """Run nba_cup function"""
    team = input('Enter the name of the team:   ')
    print(nba_cup(R, team))


def run_triple_shiftian():
    """Runs triple_shiftian function."""
    print("Enter first three elements of Triple Shiftian: ")
    first_three_elements = integer_list_input(length=3)
    print("Enter sequence number: ")
    num = integer_input(positive=True)
    print("The {}th element of Triple Shiftian is: {}".format(num, triple_shiftian(first_three_elements, num)))


def run_zeros():
    """Run zeros function"""
    number = integer_input(positive=True)
    print(zeros(number))


def run_gap_in_primes():
    """Run gap_in_primes function."""
    print("Gap size = ")
    gap = integer_input(minimum=2, positive=True)
    print("Start position = ")
    start = integer_input(minimum=3, positive=True)
    print("End position = ")
    end = integer_input(minimum=start, positive=True)
    print(gap_in_primes(gap, start, end))


def run_variance_rainfall():
    """Calculates variance of rainfall in the city."""
    try:
        town = str(input("Place: "))
        strng = str(input("Average rainfall per month (with '\n' separator): "))
        print(variance_rainfall(town, strng))
    except (ValueError, NameError):
        print("Input values must be a 'str' type")


def run_where_is_vasya():
    """Find a number of possible positions Vasya can ocupy."""
    print("Number of people in line = ")
    total = integer_input(positive=True)
    print("In front of Vasya (no less than) = ")
    in_front = integer_input(maximum=total-1, positive=True)
    print(where_is_vasya(total, in_front))


def run_volume_of_a_cuboid():
    """Run calculation pf a volume of a cuboid."""
    print("Length of a cuboid = ")
    length = float_input(positive=True)
    print("Width of a cuboid = ")
    width = float_input(positive=True)
    print("Height of a cuboid = ")
    height = float_input(positive=True)
    print(volume_of_a_cuboid(length, width, height))


def run_miles_per_gallon_to_kilometers_per_liter():
    """Run conversion from miles per gallon into kilometers per liter."""
    print("Miles per imperial gallon = ")
    miles_per_g = float_input(positive=True)
    print(miles_per_gallon_to_kilometers_per_liter(miles_per_g))


def run_am_i_wilson():
    """Run am_i_wilson function."""
    print("Number = ")
    number = integer_input()
    print(am_i_wilson(number))


def run_new_avg():
    """Run new_avg function."""
    print("Array = ")
    arr = integer_list_input()
    print("Expected average = ")
    navg = integer_input()
    print(new_avg(arr, navg))


def run_balance():
    """Run balance function."""
    book = input("Book: ")
    print(balance(book))


def run_smallest():
    """Run smallest function."""
    print("Number = ")
    num = integer_input(positive=True)
    print(smallest(num))


def run_two_decimals_places():
    """Run two_decimals_places function."""
    print("Number = ")
    num = float_input()
    print(two_decimal_places(num))


def run_abbrev_name():
    """
    Runs abbrev_name function.
    """
    try:
        name = str(input("two-worded name: "))
        print(abbrev_name(name))
    except ValueError:
        print("Invalid input. It should be str")


def run_bin_to_decimal():
    """
    Runs bin_to_decimal function.
    """
    try:
        num = str(input("bin number: "))
        print(bin_to_decimal(num))
    except ValueError:
        print("Invalid input. It should be str")


def run_angle():
    """
        Runs angle function.
    """
    print("Input number of angles")
    number = integer_input(minimum=3, positive=True)
    print(angle(number))


def run_consonant_value():
    """
        Runs consonant value function.
    """
    try:
        name = input("input string: ")
        print(consonant_value(name))
    except ValueError:
        print("Invalid input. It should be str")


def run_prime_factors():
    """
        Runs prime_factors function.
    """
    print("number: ")
    num = integer_input(minimum=1, positive=True)
    print('it`s primes: ' + prime_factors(int(num)))



def run_circle_area():
    """Runs circle_area function"""
    print('X coordinate:')
    x_coordinate = float_input()
    print('Y coordinate:')
    y_coordinate = float_input()
    print('Radius:')
    radius = float_input()
    point = Point(x_coordinate, y_coordinate)
    circle = Circle(point, radius)
    area = circle_area(circle)
    print('The area of the circle is: {}'.format(area))


def run_divisible_by():
    """Runs divisible_by function"""
    array = integer_list_input()
    divisor = integer_input(positive=True)
    divisible = divisible_by(array, divisor)
    expression = "Numbers that are divisible by {}: {}".format(divisor, divisible) \
        if divisible else "None of given numbers are divisible by {}".format(divisor)
    print(expression)


def run_series_sum():
    """Runs series_sum function"""
    print("Input a term:")
    term = integer_input(positive=True)
    series = series_sum(term)
    print("Sum of the series up to {} term is: {}".format(term, series))


def run_find_nb():
    """Runs find_nb function"""
    print("The volume: ")
    volume = integer_input(positive=True)
    cubes = find_nb(volume)
    expression = "The number of cubes is: {}".format(cubes) \
        if not cubes == -1 else "Cannot find number of cubes for given volume"
    print(expression)


def run_solve():
    """Runs solve function"""
    print("Limit")
    limit = float_input()
    argument = solve(limit)
    print('The argument of the sequence is: {}'.format(argument))
