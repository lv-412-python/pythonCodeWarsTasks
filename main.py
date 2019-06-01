"""ToDo."""
from tasks.kyu5 import (
    fib_product,
    moving_shift,
    demoving_shift,
    artificial_rain,
    zeros,
    gap_in_primes,
    smallest,
    prime_factors
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
    bin_to_decimal
)
from tasks.kyu6 import (
    interp,
    approximation,
    bouncing_ball,
    nba_cup, R,
    variance_rainfall,
    balance,
    consonant_value
)
from tasks.kyu7 import (
    sum_of_square,
    sequence_sum,
    triple_shiftian,
    replicate,
    where_is_vasya,
    new_avg,
    angle
)


def run_bouncing_ball():
    """
    Runs bouncing_ball function.
    """
    try:
        height = float(input("Enter height(must be greater than 1.5): "))
        bounce = float(input("Enter bounce of the ball(between 0 and 1): "))
        print(bouncing_ball(height, bounce))
    except ValueError:
        print("Wrong input!")


def run_heads_legs():
    """
    Runs heads_legs function.
    """
    try:
        heads = int(input("Enter the amount of heads on the farm: "))
        legs = int(input("Enter the amount of legs on the farm: "))
        while heads > 1000 or legs > 1000:
            print("Wrong input! Both numbers must be positive integers not greater than 1000.")
            heads = int(input("Enter the amount of heads on the farm: "))
            legs = int(input("Enter the amount of legs on the farm: "))
        print(heads_legs(heads, legs))
    except ValueError:
        print("Wrong input!")


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


def run_sequence_sum():
    """ run sequence sum """
    try:
        begin_number = int(input("enter start: "))
        end_number = int(input("enter end: "))
        step = int(input("enter step: "))
        print(sequence_sum(begin_number, end_number, step))
    except ValueError:
        print("Wrong input!")


def run_approximation():
    """ run approximation """
    try:
        number = float(input("enter number: "))
        print(approximation(number))
    except ValueError:
        print("Wrong input!")


def run_artificial_rain():
    """ run artificial rain """
    try:
        input_string = input("Enter a list element separated by space ")
        garden = input_string.split()
        print(artificial_rain(garden))
    except ValueError:
        print('Wrong input!')


def run_duty_free():
    """ This function is entry point of program"""
    try:
        price = int(input("Price is: "))
        discount = int(input("Discount is: "))
        holiday_cost = int(input("Holiday cost is: "))
        print('You can buy {} bottles of whiskey:D'.format(
            duty_free(price, discount, holiday_cost)))
    except ValueError:
        print('Please enter number!')


def run_validate_usr():
    """ This function is entry point of program"""

    username = str(input("Enter your username: "))
    print((validate_usr(username)))


def run_fix_the_meerkat():
    """Run fix_the_meerkat function"""
    print(fix_the_meerkat(["tail", "body", "head"]))


def run_square_or_square_root():
    """Run square_or_square_root function"""
    try:
        input_ = input("Enter a sequence of numbers separated by a space: ")
        input_list = [int(number) for number in input_.split(' ')]
        print(square_or_square_root(input_list))
    except ValueError:
        print("You must enter only numbers.")


def run_replicate():
    """Run replicate function"""
    try:
        times = int(input("a: "))
        number = int(input("b: "))
        print(replicate(times, number))
    except ValueError:
        print("You must input only numbers.")


def run_nba_cup():
    """Run nba_cup function"""
    team = input('Enter the name of the team:   ')
    print(nba_cup(R, team))


def run_triple_shiftian():
    """
    Runs triple_shiftian function.
    """
    first_three_elements = list()
    try:
        first_three_elements.append(int(input("Enter 1st element of Triple Shiftian: ")))
        first_three_elements.append(int(input("Enter 2nd element of Triple Shiftian: ")))
        first_three_elements.append(int(input("Enter 3rd element of Triple Shiftian: ")))
        num = int(input("Enter sequence number: "))
        print(triple_shiftian(first_three_elements, num))
    except ValueError:
        print("Wrong input! All variables should be integers.")


def run_zeros():
    """Run zeros function"""
    try:
        number = int(input("Enter number   "))
        print(zeros(number))
    except ValueError:
        print("You should enter number.")


def find_primes():
    """Run gap_in_primes function."""
    try:
        gap = int(input("gap size: "))
        start = int(input("start of the search, inclusive: "))
        end = int(input("end of the search, inclusive: "))
        print(gap_in_primes(gap, start, end))
    except (ValueError, NameError):
        print("Input value must be an integer number")


def calculate_variance_of_rainfall():
    """Calculates variance of rainfall in the city."""
    try:
        town = str(input("Place: "))
        strng = str(input("Average rainfall per month (with '\n' separator): "))
        print(variance_rainfall(town, strng))
    except (ValueError, NameError):
        print("Input values must be a 'str' type and in quotation marks")


def find_vasya():
    """Find a number of possible positions Vasya can ocupy."""
    try:
        total = int(input("number of people in line: "))
        in_front = int(input("in front of Vasya (no less than): "))
        print(where_is_vasya(total, in_front))
    except (ValueError, NameError):
        print("Input value must be an integer value")


def calculate_volume():
    """Run calculation pf a volume of a cuboid."""
    try:
        length = float(input("length: "))
        width = float(input("width: "))
        height = float(input("height: "))
        print(volume_of_a_cuboid(length, width, height))
    except (ValueError, NameError):
        print("Input value must be a number")


def make_conversion():
    """Run conversion from miles per gallon into kilometers per liter."""
    try:
        miles_per_g = float(input("miles per imperial gallon: "))
        print(miles_per_gallon_to_kilometers_per_liter(miles_per_g))
    except (ValueError, NameError):
        print("Input value must be a number")


def run_am_i_wilson():
    """Run am_i_wilson function."""
    try:
        number = int(input("Number: "))
        print(am_i_wilson(number))
    except (NameError, ValueError):
        print("You must enter a number.")


def run_new_avg():
    """Run new_avg function."""
    try:
        arr = input("Array: ")
        navg = int(input("Expected average: "))
        print(new_avg(arr, navg))
    except (NameError, ValueError):
        print("You must enter a number.")


def run_balance():
    """Run balance function."""
    book = input("Book: ")
    print(balance(book))


def run_smallest():
    """Run smallest function."""
    try:
        num = int(input("Number: "))
        print(smallest(num))
    except (ValueError, NameError):
        print("You must enter a number.")


def run_two_decimals_places():
    """Run two_decimals_places function."""
    try:
        number = float(input("Number: "))
        print(two_decimal_places(number))
    except (ValueError, NameError):
        print("You must enter a number.")


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


def run_sum_of_angles():
    """
        Runs angle function.
    """
    try:
        number = int(input("number of angles: "))
        print(angle(number))
    except ValueError:
        print("Invalid input. It should be int")


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
    try:
        name = input("number: ")
        print('it`s primes: ' + prime_factors(int(name)))
    except ValueError:
        print('Please enter integer')


if __name__ == '__main__':
    run_sls()
    run_moving_shift()
    run_fib_product()
    run_triple_shiftian()
    run_heads_legs()
    run_interp()
    run_litres()
    run_sum_of_square()
    run_starting_mark()
    run_sequence_sum()
    run_approximation()
    run_artificial_rain()
    run_duty_free()
    run_validate_usr()
    run_fix_the_meerkat()
    run_bouncing_ball()
    run_triple_shiftian()
    run_replicate()
    run_nba_cup()
    run_zeros()
    make_conversion()
    run_am_i_wilson()
    run_new_avg()
    run_abbrev_name()
    run_bin_to_decimal()
    run_sum_of_angles()
    run_consonant_value()
    run_prime_factors()
