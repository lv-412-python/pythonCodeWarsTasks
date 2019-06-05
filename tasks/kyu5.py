# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/first-variation-on-caesar-cipher
"""
import math

RUNNERS = 5
NUMBERS_OF_LETTERS_IN_THE_ALPHABET = 26


def fib(num):
    """
    Finds n-th element from a Fibonacci sequence.
    :param num: int : sequence number.
    :return: int : n-th element from a Fibonacci sequence.
    """
    first, second = 0, 1
    for _ in range(2, num - 1):
        first, second = second, first + second
    return second


def fib_product(product):
    """
    Finds two consistent Fibonacci numbers, being given their possible product.
    In case it is - returns a list with [fib(n), fib(n+1), True],
    otherwise [fib(n), fib(n+1), False].
    :param product: int : product of two numbers.
    :return: list : list with first two elements from Fibonacci sequence and a boolean.
    """
    current_value, num = 0, 0
    fib1 = fib2 = 0

    while current_value < product:
        num += 1
        fib1 = fib(num)
        fib2 = fib(num + 1)
        current_value = fib1 * fib2

    if current_value == product:
        return [fib1, fib2, True]

    return [fib1, fib2, False]


def chunk_string(text: str, parts: int) -> list:
    """divide by message length between the five runners.
        :text : str : chipher text
        :parts : int : shows how many parts you need to split the text
        :returns : list : returns list with length which equal RUNNERS
    """
    res = [text[i:i + len(text) // parts + 1] for i in range(0, len(text), len(text) // parts + 1)]
    return res


def moving_shift(plain_text: str, shift: int) -> list:
    """Search for some intermediate results.
        :plain_text : str : input text which need to encrypt
        :shift : int : number of places up or down the alphabet
        :returns : list : returns list with length which equal RUNNERSs
    """
    chipher_text = ''
    for letter in plain_text:
        if letter.isalpha():
            shift_letter = ord(letter) + shift
            if shift_letter > ord('z'):
                shift_letter -= NUMBERS_OF_LETTERS_IN_THE_ALPHABET
            chipher_text += chr(shift_letter)
        else:
            chipher_text += letter

    return chunk_string(chipher_text, RUNNERS)


def stick_together(chunks_chipher_text: list) -> str:
    """ Converts the list to string
        :chunks_chipher_text : list : encrypted tex is divided into RUNNERS elements
        :returns: str : returns full chipher text
    """
    chipher_text = ''
    chipher_text = ''.join(chunks_chipher_text)

    return chipher_text


def demoving_shift(chunks_chipher_text: list, shift: int) -> str:
    """ Decrypt chipher text
        :chunks_chipher_text : list : results of work moving_shift
        :shift : int : number of places up or down the alphabet
        :returns : str : returns plain text
    """
    chipher_text = stick_together(chunks_chipher_text)
    plain_text = ""
    for letter in chipher_text:
        if letter.isalpha():
            shift_letter = ord(letter) - shift
            if shift_letter > ord('z'):
                shift_letter += NUMBERS_OF_LETTERS_IN_THE_ALPHABET
            plain_text += chr(shift_letter)
        else:
            plain_text += letter

    return plain_text


def artificial_rain(garden):
    """
    counts longest descending subsequence
    :param garden: list : your garden
    :return: int : Best spot for artificial rain
    """
    result_arr = [1]
    length = len(garden)
    for i in range(1, length):
        result = 1
        for j in range(i, length):
            if garden[j] >= garden[j-1]:
                result += 1
            else:
                break
        for k in range(i+result-1, length):
            if garden[k] <= garden[k-1]:
                result += 1
            else:
                break
        result_arr.append(result)
    return max(result_arr)


def zeros(num):
    """
    Calculate the number of trailing zeros in a factorial of a given number and return number.
    :param num: int : Input number.
    :return: int : Number of the zeros
    """
    i = 5
    num_of_zeros = 0
    while num >= i:
        num_of_zeros += num // i
        i *= 5
    return num_of_zeros


def gap_in_primes(gap, start, end):
    """Find a first pair of two successive prime numbers spaced with a defined gap-size.

    :param gap: int : Size of the gap between two primes.
    :param start: int : Gives the start number of the search (inclusive).
    :param end: int : Gives the end number of the search (inclusive).

    :return: list: The pair of two successive primes between start and end.
    :return: None: When there is no two successive prime numbers between start and end.

    """
    primes = []

    for possible_prime in range(start, end + 1):
        is_prime = True

        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(possible_prime)

    i = 0
    while i < len(primes) - 1:
        if primes[i + 1] - primes[i] == gap:
            return [primes[i], primes[i + 1]]
        i += 1

    return None


def solve(limit):
    """
    Calculates x out of sequence 'x + 2x**2 + 3x**3 + .. + nx**n'

    :param limit: float : The limit of the sequence.
    :return: float : argument of the sequence.
    """
    discriminant = math.pow((1 + 2 * limit), 2) - 4 * limit * limit
    argument = (- (1 + 2 * limit) + math.sqrt(discriminant)) / (-2 * limit)
    return argument


def smallest(number):
    """
        Find the smallest number doing only one permutation.
        :param number: int : number.
        :return: tuple : [the smallest number we got, the index of the digit we took,
                        the index where we insert digit].
    """
    min_num, from_i, to_i = number, 0, 0
    number = str(number)
    for i in enumerate(number):
        num1 = number[:i[0]] + number[i[0] + 1:]
        for j in range(len(num1) + 1):
            num = int(num1[:j] + number[i[0]] + num1[j:])
            if num < min_num:
                min_num, from_i, to_i = num, i[0], j
    return [min_num, from_i, to_i]


def prime_factors(number):
    """
       Finds prime factors of the number.
       :param number: int : The initial number.
       :return: str : String with factors.
    """
    fact = []
    i = 2
    result = ''
    while i <= number:
        if number % i == 0:
            fact.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        fact.append(number)
    k = 0
    while k < len(fact):
        num = fact.count(fact[k])
        if num > 1:
            result += '(' + str(fact[k]) + '**' + str(num) + ')'
        else:
            result += '(' + str(fact[k]) + ')'
        k += num
    return result
