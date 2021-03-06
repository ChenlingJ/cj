from typing import Iterable, Iterator, Optional


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
def my_pow(value: int, exponent: int) -> Optional[int]:
    """
    Raises an integer "value" to the "exponent" power. Does not support negative powers.
    :param value: An integer value.
    :param exponent: An integer value.
    :return: "value" raised to the power of "exponent".
    """
    if exponent < 0:
        return None
    power = 1  # Define variables closest to where they are used.
    for i in range(exponent):
        power *= value
    return power


def my_any(values: Iterable[bool]) -> bool:
    """
    Return "True" if any of the "values" is True.
    :param values: An iterable of booleans.
    :return: True if any value from "values" is True, otherwise False.
             If "values" is empty, returns False.
    """
    for value in values:
        if value:
            return True
    return False


def my_all(values: Iterable[bool]) -> bool:
    """
    Return "True" if all of the "values" are True.
    :param values: An iterable of booleans.
    :return: True if all values from "values" are True, otherwise False.
             If "values" is empty, returns True vacuous truth.
    """
    for value in values:
        if not value:
            return False
    return True


# Please use a loop for this solution.
def my_len(items: list) -> int:
    """
    Counts the number of items in a given list.
    :param items: The list to count.
    :return: The number of items in the list.
    """
    count = 0
    for _ in items:  # _ means irrelevant in the for loop.
        count += 1
    return count


def my_reversed(values: list) -> list:
    """
    Produces a new list with the contents of "values" but in reverse order.
    :param values: The list to reverse.
    :return: A new list with reversed contents.
    """
    my_reversed_list = []
    # for i in range(len(values)):
    #     my_reversed_list.append(values[len(values) - i - 1])
    for i in range(len(values)):
        my_reversed_list.append(values[-1 - i])
    # for i in range(-1, -len(values)-1, -1):
    #     my_reversed_list.append(values[i])
    # for i in range(len(values), 0, -1):
    # my_reversed_list.append(values[i - 1])
    return my_reversed_list


def my_round(value: float, decimals: int = 0) -> float:
    """
    Rounds the given "value" to the specified number of decimal places.
    :param value: The value to round.
    :param decimals: The maximum precision of decimal places to include in the output.
    :return: A rounded floating point number.
    """
    magnitude = 10 ** decimals
    # "/" always returns a float.
    return int(value * magnitude + 0.5) / magnitude


# Please use a generator function for this solution (contains a "yield" expression).
def my_range(start: int, end: Optional[int] = None, step: int = 1) -> Iterator[int]:
    """
    Returns a generator that will return integers between "start" (inclusive) and "end" (exclusive),
    counting up by "step".
    :param start: The starting value, always included in the output.
    :param end: The end value, never included in the output.
    :param step: The amount to add each time. If no argument is passed to step, step is 1.
    :return: Yields values starting with "start", counting by "step", and stopping before "end".
    """
    if step == 0:
        raise ValueError("step must not be 0")
    # my_range(10)
    # start=10, end=None, step=1
    # how do we get to: start=0, end=10, step=1
    if end is None:
        start, end = 0, start
        # end = start
        # start = 0
    while (start < end and step > 0) or (start > end and step < 0):
        yield start
        start += step
