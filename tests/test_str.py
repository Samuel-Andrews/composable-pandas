from composable_pandas.str import capitalize, is_leap_year, minute, month, quarter, week
from datetime import datetime

import numpy as np
import pytest
import pandas as pd

from pandas import Series, _testing as tm

def test_capitalize():
    values = Series(["FOO", "BAR", np.nan, "Blah", "blurg"])
    result = values >> capitalize()
    exp = Series(["Foo", "Bar", np.nan, "Blah", "Blurg"])
    tm.assert_series_equal(result, exp)

    # mixed
    mixed = Series(["FOO", np.nan, "bar", True, datetime.today(), "blah", None, 1, 2.0])
    mixed = mixed >> capitalize()
    exp = Series(["Foo", np.nan, "Bar", np.nan, np.nan, "Blah", np.nan, np.nan, np.nan])
    tm.assert_almost_equal(mixed, exp)


def test_minute():
    result = pd.Series(pd.date_range("2000-01-01", periods=12, freq="T"))
    exp = Series(range(0,12))
    tm.assert_series_equal(result >> minute(), exp)

    # roll over
    roll = pd.Series(pd.date_range("2000-01-01 00:59:00", periods=3, freq="T"))
    exp = Series([59,0,1])
    tm.assert_series_equal(roll.tail(3) >> minute(), exp)


def test_month():
    result = pd.Series(pd.date_range("2000-01-01", periods=12, freq="M"))
    exp = Series(range(1,13))
    tm.assert_series_equal(result >> month(), exp)

    # roll over
    roll = pd.Series(pd.date_range("2000-12-01", periods=3, freq="M"))
    exp = Series([12,1,2])
    tm.assert_series_equal(roll.tail(3) >> month(), exp)


def test_quarter():
    result = pd.Series(pd.date_range("2000-01-01", periods=4, freq="Q"))
    exp = Series(range(1,5))
    tm.assert_series_equal(result >> quarter(), exp)

    # roll over
    roll = pd.Series(pd.date_range("2000-12-01", periods=5, freq="Q"))
    exp = Series([4,1,2,3,4])
    tm.assert_series_equal(roll >> quarter(), exp)



def test_week():
    result = pd.Series(pd.date_range("2000-01-05", periods=12, freq="W"))
    exp = Series(range(1,13))
    tm.assert_series_equal(result >> week(), exp)

    # roll over
    roll = pd.Series(pd.date_range("2000-12-31", periods=3, freq="W"))
    exp = Series([52,1,2])
    tm.assert_series_equal(roll >> week(), exp)


def test_is_leap_year():
        dt = pd.Series(pd.date_range("2000-01-01", periods=1, freq="Y"))
        assert (dt >> is_leap_year())[0]

        dt = pd.Series(pd.date_range("1999-01-01", periods=1, freq="Y"))
        assert not (dt >> is_leap_year())[0]

        dt = pd.Series(pd.date_range("2004-01-01", periods=1, freq="Y"))
        assert (dt >> is_leap_year())[0]

        dt = pd.Series(pd.date_range("2100-01-01", periods=1, freq="Y"))
        assert not (dt >> is_leap_year())[0]