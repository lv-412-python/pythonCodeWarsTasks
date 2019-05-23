# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/first-variation-on-caesar-cipher
"""
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
    res = [text[i:i+len(text)//parts+1] for i in range(0, len(text), len(text)//parts+1)]
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
            shift_letter = ord(letter)+shift
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
            shift_letter = ord(letter)-shift
            if shift_letter > ord('z'):
                shift_letter += NUMBERS_OF_LETTERS_IN_THE_ALPHABET
            plain_text += chr(shift_letter)
        else:
            plain_text += letter

    return plain_text

def desc(sub):
    """
    counts descending subsequence of passed array
    :param sub: list : subsequence of garden
    :return: int : length of descending sequence
    """
    result = 1
    for i, _ in enumerate(sub):
        if sub[i] <= sub[i - 1]:
            result += 1
        else:
            break
    return result


def artificial_rain(garden):
    """
    counts longest descending subsequence
    :param garden: list : your garden
    :return: int : Best spot for artificial rain
    """
    result_arr = [1]
    if len(garden) == 1:
        return 1
    result_arr.append(desc(garden))
    result_arr.append(desc(garden[::-1]))
    for i, _ in enumerate(garden[:-1]):
        if garden[i] >= garden[i - 1] and garden[i] >= garden[i + 1]:
            result_arr.append(desc(garden[i - 1::-1]) + desc(garden[i:]))
    return max(result_arr)
    