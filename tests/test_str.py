from composable_pandas.str import capitalize, isalnum, isalpha, isdigit
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