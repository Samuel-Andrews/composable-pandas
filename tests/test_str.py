from composable_pandas.str import capitalize, index, isalnum, isalpha, isdecimal, isdigit, isnumeric
from datetime import datetime, timedelta

import numpy as np
import pytest

from pandas import Series, _testing as tm
from pandas import DataFrame, Index, MultiIndex, Series, isna, notna




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




def test_index():
    def _check(result, expected):
        if isinstance(result, Series):
            tm.assert_series_equal(result, expected)
        else:
            tm.assert_index_equal(result, expected)

    for klass in [Series, Index]:
        s = klass(["ABCDEFG", "BCDEFEF", "DEFGHIJEF", "EFGHEF"])

        result = s >> index("EF")
        _check(result, klass([4, 3, 1, 0]))
        expected = np.array([v.index("EF") for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)

        result = s >> index("EF", start = 3)
        _check(result, klass([4, 3, 7, 4]))
        expected = np.array([v.index("EF", 3) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)


        result = s >> index("E", start = 4, end = 8)
        _check(result, klass([4, 5, 7, 4]))
        expected = np.array([v.index("E", 4, 8) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)

        with pytest.raises(ValueError, match="substring not found"):
            result = s >> index("DE")

        msg = "expected a string object, not int"
        with pytest.raises(TypeError, match=msg):
            result = s >> index(0)

    # test with nan
    s = Series(["abcb", "ab", "bcbe", np.nan])
    result = s >> index("b")
    tm.assert_series_equal(result, Series([1, 1, 0, np.nan]))
  



def test_ismethods():
    values = ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "]
    str_s = Series(values)
    alnum_e = [True, True, True, True, True, False, True, True, False, False]
    alpha_e = [True, True, True, False, False, False, True, False, False, False]
    digit_e = [False, False, False, True, False, False, False, True, False, False]

    tm.assert_series_equal(str_s >> isalnum(), Series(alnum_e))
    tm.assert_series_equal(str_s >> isalpha(), Series(alpha_e))
    tm.assert_series_equal(str_s >> isdigit(), Series(digit_e))


    assert (str_s >> isalnum()).tolist() == [v.isalnum() for v in values]
    assert (str_s >> isalpha()).tolist() == [v.isalpha() for v in values]
    assert (str_s >> isdigit()).tolist() == [v.isdigit() for v in values]




def test_isnumeric():
    # 0x00bc: ¼ VULGAR FRACTION ONE QUARTER
    # 0x2605: ★ not number
    # 0x1378: ፸ ETHIOPIC NUMBER SEVENTY
    # 0xFF13: ３ Em 3
    values = ["A", "3", "¼", "★", "፸", "３", "four"]
    s = Series(values)
    numeric_e = [False, True, True, False, True, True, False]
    decimal_e = [False, True, False, False, False, True, False]
    tm.assert_series_equal(s >> isnumeric(), Series(numeric_e))
    tm.assert_series_equal(s >> isdecimal(), Series(decimal_e))

    unicodes = ["A", "3", "¼", "★", "፸", "３", "four"]
    assert (s >> isnumeric()).tolist() == [v.isnumeric() for v in unicodes]
    assert (s >> isdecimal()).tolist() == [v.isdecimal() for v in unicodes]

    values = ["A", np.nan, "¼", "★", np.nan, "３", "four"]
    s = Series(values)
    numeric_e = [False, np.nan, True, False, np.nan, True, False]
    decimal_e = [False, np.nan, False, False, np.nan, True, False]
    tm.assert_series_equal(s >> isnumeric(), Series(numeric_e))
    tm.assert_series_equal(s >> isdecimal(), Series(decimal_e))