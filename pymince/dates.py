# -*- coding: utf-8 -*-

import contextlib
import datetime
import enum


def irange(start_date, stop_date=None, time_step=None):
    """
    Returns a generator that produces a sequence of datetime's from "start_date" (inclusive)
    to "stop_date" (exclusive) by "time_step".

    :param datetime.datetime start_date: Inclusive.
    :param datetime.datetime stop_date: Exclusive. `utcnow` is used by default.
    :param datetime.delta time_step: one-day `timedelta` is used by default.

     Examples:
        import datetime

        from pymince.dates import irange

        ini = datetime.datetime.fromisoformat("2022-10-31")
        end = datetime.datetime.fromisoformat("2022-11-02")
        day = datetime.timedelta(days=1)

        it = irange(ini, stop_date=end, time_step=day)

        next(it) # --> datetime.datetime(2022, 10, 31, 0, 0)
        next(it) # --> datetime.datetime(2022, 11, 1, 0, 0)
        next(it) # --> raise StopIteration
    """

    this = start_date
    stop = stop_date or datetime.datetime.utcnow()
    step = time_step or datetime.timedelta(days=1)
    while this < stop:
        yield this
        this += step


def string2year(value, gte=None, lte=None, shift=None):
    """
    Function to convert a string year representation to integer year.

    :param str value: Value to convert.
    :param Optional[int] gte: if it is specified is required that: year >= gte
    :param Optional[int] lte: if it is specified is required that: year <= lte
    :param Optional[int] shift: use a two-digit year on shift

    :raise: "ValueError" if "value" cannot be converted.
    :rtype: int

    Examples:
        from pymince.dates import string2year

        string2year("53", shift=None) # --> 2053
        string2year("53", shift=1953) # --> 1953
        string2year("52", shift=1953) # --> 2052
        string2year("54", shift=1953) # --> 1954

        string2year("1954") # --> 1954

        string2year("123") # --> ValueError
        string2year("1955", gte=1956) # --> ValueError
        string2year("1955", lte=1954) # --> ValueError
    """

    year = None
    for rep in ("%Y", "%y"):
        with contextlib.suppress(ValueError, TypeError):
            year = datetime.datetime.strptime(value, rep).year
            if shift and rep == "%y":
                # Use shift for year of two-digit format
                year = (year - shift) % 100 + shift
            if (gte and not year >= gte) or (lte and not year <= lte):
                year = None
            break

    if year:
        return year
    else:
        raise ValueError


@enum.unique
class WeekDay(enum.IntEnum):
    """
    Python Enum containing Days of the Week,
    where Monday == 0 ... Sunday == 6.

    Provides a 'of' method can be used to verbalize a datetime.datetime.weekday
    return value.

    Example:
        from pymince.dates import WeekDay

        friday = datetime.datetime(2023, 2, 17)
        WeekDay.of(friday)  #  pymince.dates.WeekDay.FRIDAY
    """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @classmethod
    def of(cls, date):
        return cls(date.weekday())


@enum.unique
class IsoWeekDay(enum.IntEnum):
    """
    Python Enum containing Days of the Week, according to ISO,
    where Monday == 1 ... Sunday == 7.

    Provides a 'of' method can be used to verbalize a datetime.datetime.isoweekday
    return value.

    Example:
         from pymince.dates import IsoWeekDay

        friday = datetime.datetime(2023, 2, 17)
        IsoWeekDay.of(friday)  #  pymince.dates.IsoWeekDay.FRIDAY
    """

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def of(cls, date):
        return cls(date.isoweekday())
