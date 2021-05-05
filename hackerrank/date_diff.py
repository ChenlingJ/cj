from itertools import accumulate


MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_STARTS = list(accumulate([0] + MONTH_LENGTHS[:-1]))  # [0, 31, 31+28, 31+28+31, ...]


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def epoch_days_offset(year: int) -> int:
    """
    Gets the number of days that `year` is offset from 1970, accounting
    for leap years. For example, if `year` is 1971, then the value is 365.
    If `year` is 1968, the value is -731 (equal to -(365 + 366), because
    1968 was a leap year.)
    """
    start = 1970
    end = year
    negative = start > end  # Are we going backwards from 1970?
    if negative:
        end, start = start, end

    days = 0
    for year in range(start, end):
        days += 365
        if is_leap_year(year):
            days += 1

    if negative:
        days *= -1
    return days


def to_timestamp(date: str) -> int:
    """
    Converts a date in the format 'Thu 01 Jan 1970 00:00:00 +0000'
    into a `Unix epoch time <https://en.wikipedia.org/wiki/Unix_time>`.
    Unlike true epoch, supports values before 1970-01-01.
    """
    _, day, month, year, time, timezone = date.split()  # First element is weekday so ignore it.

    year, day = int(year), int(day)  # Convert to integers.
    day -= 1  # Number days starting from 0.
    month = MONTH_NAMES.index(month)
    day_of_year = MONTH_STARTS[month] + day
    if month >= 2 and is_leap_year(year):
        day_of_year += 1
    days_since_epoch = epoch_days_offset(year) + day_of_year  # The number of days to add to Jan 1 1970.

    timezone = int(timezone)  # Parsed as base 10.
    timezone_hour = abs(timezone) // 100
    timezone_minute = abs(timezone) % 100
    if timezone < 0:
        timezone_hour *= -1
        timezone_minute *= -1
    hour, minute, second = map(int, time.split(':'))
    hour -= timezone_hour
    minute -= timezone_minute
    seconds_since_midnight = (hour * 60 * 60) + (minute * 60) + second

    return (days_since_epoch * 24 * 60 * 60) + seconds_since_midnight


def date_diff(start: str, end: str) -> int:
    return abs(to_timestamp(end) - to_timestamp(start))
