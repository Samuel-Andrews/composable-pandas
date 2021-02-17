from composable import pipeable
import pandas as pd


@pipeable
def capitalize(col):
    """Convert strings in the Series/Index to be capitalized.
    
    Equivalent to :meth:`str.capitalize`.
    
    Returns
    -------
    Series or Index of object
    
    See Also
    --------
    str.lower : Converts all characters to lowercase.
    str.upper : Converts all characters to uppercase.
    str.title : Converts first character of each word to uppercase and
        remaining to lowercase.
    str.capitalize : Converts first character to uppercase and
        remaining to lowercase.
    str.swapcase : Converts uppercase to lowercase and lowercase to
        uppercase.
    str.casefold: Removes all case distinctions in the string.
    
    Examples
    --------
    >>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
    >>> s
    0                 lower
    1              CAPITALS
    2    this is a sentence
    3              SwApCaSe
    dtype: object
    
    >>> s >> capitalize
    0                 Lower
    1              Capitals
    2    This is a sentence
    3              Swapcase
    dtype: object
    
    """
    return col.str.capitalize() ###

@pipeable
def minute(col):
    """The minutes of the datetime.
    
    Examples
    --------
    >>> datetime_series = pd.Series(
    ...     pd.date_range("2000-01-01", periods=3, freq="T")
    ... )
    >>> datetime_series
    0   2000-01-01 00:00:00
    1   2000-01-01 00:01:00
    2   2000-01-01 00:02:00
    dtype: datetime64[ns]
    >>> datetime_series >> minute()
    0    0
    1    1
    2    2
    dtype: int64

    """
    return col.dt.minute

@pipeable
def month(col):
    """The month as January=1, December=12.
    
    Example
    --------
    >>> datetime_series = pd.Series(
    ...     pd.date_range("2000-01-01", periods=3, freq="M")
    ... )
    >>> datetime_series
    0   2000-01-31
    1   2000-02-29
    2   2000-03-31
    dtype: datetime64[ns]
    >>> datetime_series >> month()
    0    1
    1    2
    2    3
    dtype: int64

    """
    return col.dt.month


@pipeable
def quarter(col):
    """The quarter of the date.
        1 = Jan, Feb, Mar
        2 = Apr, May, June
        3 = July, Aug, Sept
        4 = Oct, Nov, Dec
    Example
    --------
    >>> datetime_series = pd.Series(
    ...     pd.date_range("2000-01-01", periods=3, freq="Q")
    ... )
    >>> datetime_series
    0   2000-01-31
    1   2000-06-30
    2   2000-09-30
    dtype: datetime64[ns]
    >>> datetime_series >> quarter()
    0    1
    1    2
    2    3
    dtype: int64

    """
    return col.dt.quarter

@pipeable
def week(col):
    """The week ordinal of the year.

    Example
    --------
    >>> datetime_series = pd.Series(
    ...     pd.date_range("2000-01-01", periods=5, freq="W")
    ... )
    >>> datetime_series
    0   2000-01-02
    1   2000-01-09
    2   2000-01-16
    3   2000-01-23
    4   2000-01-30
    dtype: datetime64[ns]
    >>> datetime_series >> week()
    0    52
    1    1
    2    2
    3    3
    4    4
    dtype: int64

    """

    return col.dt.week


@pipeable
def is_leap_year(col):
    """Boolean indicator if the date belongs to a leap year.
    
    A leap year is a year, which has 366 days (instead of 365) including
    29th of February as an intercalary day.
    Leap years are years which are multiples of four with the exception
    of years divisible by 100 but not by 400.
    
    Returns
    -------
    Series or ndarray
         Booleans indicating if dates belong to a leap year.
    
    Examples
    --------
    This method is available on Series with datetime values under
    the ``.dt`` accessor, and directly on DatetimeIndex.
    
    >>> idx = pd.date_range("2012-01-01", "2015-01-01", freq="Y")
    >>> idx
    DatetimeIndex(['2012-12-31', '2013-12-31', '2014-12-31'],
                  dtype='datetime64[ns]', freq='A-DEC')
    >>> idx.is_leap_year
    array([ True, False, False])
    
    >>> dates_series = pd.Series(idx)
    >>> dates_series
    0   2012-12-31
    1   2013-12-31
    2   2014-12-31
    dtype: datetime64[ns]
    >>> dates_series.dt.is_leap_year
    0     True
    1    False
    2    False
    dtype: bool
    """
    return col.dt.is_leap_year