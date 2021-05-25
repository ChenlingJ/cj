from math import inf
from typing import Generator, Iterable, Optional, Iterator


def my_max(items: Iterable[int]) -> Optional[int]:
    """
    Finds the maximum integer value in "items".
    :param items: An iterable containing integers.
    :return: The maximum value from "items". If "items" is empty, returns "None".
    """
    maximum = None
    # if "items" is empty, the for loop will not run.
    for item in items:
        if maximum is None or item > maximum:
            maximum = item
    return maximum


def my_min(items: Iterable[int]) -> Optional[int]:
    """
    Finds the minimum integer value in "items".
    :param items: An iterable containing integers.
    :return: The minimum value from "items". If "items" is empty, returns "None".
    """
    minimum = None
    for item in items:
        if minimum is None or item < minimum:
            minimum = item
    return minimum


def my_sum(items: Iterable[int]) -> int:
    """
    Computes the sum of all the integers in "items".
    :param items: An iterable containing integers.
    :return: The sum of "items".
    """
    total = 0
    for item in items:
        total += item
    return total


def my_abs(value: int) -> int:
    """
    Computes the absolute value of "value".
    :param value: An integer.
    :return: The absolute value of "value".
    """
    if value >= 0:
        return value
    return -value


# Please use a loop for this implementation.
def my_pow(value: int, exponent: int) -> int:
    """
    Raises an integer "value" to the "exponent" power. Does not support negative powers.
    :param value: An integer value.
    :param exponent: An integer value.
    :return: "value" raised to the power of "exponent".
    """
    pass


def my_any(values: Iterable[bool]) -> bool:
    """
    Return "True" if any of the "values" is True.
    :param values: An iterable of booleans.
    :return: True if any value from "values" is True, otherwise False.
    """
    pass


def my_all(values: Iterable[bool]) -> bool:
    """
    Return "True" if all of the "values" are True.
    :param values: An iterable of booleans.
    :return: True if all values from "values" are True, otherwise False.
    """
    pass


# Please use a loop for this solution.
def my_len(items: list) -> int:
    """
    Counts the number of items in a given list.
    :param items: The list to count.
    :return: The number of items in the list.
    """


def my_reversed(values: list) -> list:
    """
    Produces a new list with the contents of "values" but in reverse order.
    :param values: The list to reverse.
    :return: A new list with reversed contents.
    """
    pass


def my_round(value: float, decimals: int = 0) -> float:
    """
    Rounds the given "value" to the specified number of decimal places.
    :param value: The value to round.
    :param decimals: The maximum precision of decimal places to include in the output.
    :return: A rounded floating point number.
    """
    pass


# Please use a generator function for this solution (contains a "yield" expression).
def my_range(start: int, end: int, step: int = 1) -> Iterator[int]:
    """
    Returns a generator that will return integers between "start" (inclusive) and "end" (exclusive),
    counting up by "step".
    :param start: The starting value, always included in the output.
    :param end: The end value, never included in the output.
    :param step: The amount to add each time.
    :return: Yields values starting with "start", counting by "step", and stopping before "end".
    """
    pass
