import unittest
import datetime as dt
from random import randrange
from hackerrank.date_diff import to_timestamp, MONTH_LENGTHS, MONTH_NAMES, is_leap_year


class Tests(unittest.TestCase):
    def test_to_timestamp(self):
        # Every day from `start` to `end`, choose a random time and timezone and compare
        # the above output to the one from datetime.
        for year in range(1853, 2025):
            for month in range(12):
                month_length = MONTH_LENGTHS[month]
                if month == 1 and is_leap_year(year):
                    month_length += 1
                for day in range(month_length):
                    tz_hour = randrange(-11, 13)
                    tz_minute = randrange(0, 60)
                    hour = randrange(0, 24)
                    minute = randrange(0, 60)
                    second = randrange(0, 60)

                    date_str = 'Day {d:02} {m} {y} {H:02}:{M:02}:{S:02} {tzh:+03}{tzm:02}'.format(
                        d=day + 1,
                        m=MONTH_NAMES[month],
                        y=year,
                        H=hour,
                        M=minute,
                        S=second,
                        tzh=tz_hour,
                        tzm=tz_minute,
                    )

                    timezone_offset = dt.timedelta(
                        hours=abs(tz_hour),
                        minutes=tz_minute,
                    )
                    if tz_hour < 0:
                        timezone_offset = -timezone_offset
                    date_obj = dt.datetime(
                        year,
                        month + 1,
                        day + 1,
                        hour,
                        minute,
                        second,
                        tzinfo=dt.timezone(timezone_offset),
                    )

                    expected = int(date_obj.timestamp())
                    actual = to_timestamp(date_str)

                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
