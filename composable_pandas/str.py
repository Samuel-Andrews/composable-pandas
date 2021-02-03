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
    return col.str.capitalize()




@pipeable
def isalnum(col):
    """isalnum() method of pandas.core.strings.accessor.StringMethods instance
    Check whether all characters in each string are alphanumeric.
    
    This is equivalent to running the Python string method
    :meth:`str.isalnum` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    isalpha : Check whether all characters are alphabetic.
    isdigit : Check whether all characters are digits.
    isdecimal : Check whether all characters are decimal.
    isnumeric : Check whether all characters are numeric.
    
    Examples
    --------
    **Checks for Alphabetic and Numeric Characters**
    
    >>> s1 = pd.Series(['one', 'one1', '1', ''])
    
    >>> s1 >> isalpha()
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    
    >>> s1 >> isnumeric()
    0    False
    1    False
    2     True
    3    False
    dtype: bool
    
    >>> s1 >> isalnum()
    0     True
    1     True
    2     True
    3    False
    dtype: bool
    
    Note that checks against characters mixed with any additional punctuation
    or whitespace will evaluate to false for an alphanumeric check.
    
    >>> s2 = pd.Series(['A B', '1.5', '3,000'])
    >>> s2 >> isalnum()
    0    False
    1    False
    2    False
    dtype: bool
    
    
    
    """
    return col.str.isalnum()




@pipeable
def isalpha(col):
    """isalpha() method of pandas.core.strings.accessor.StringMethods instance
    Check whether all characters in each string are alphabetic.
    
    This is equivalent to running the Python string method
    :meth:`str.isalpha` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    isalnum : Check whether all characters are alphanumeric.
    isdigit : Check whether all characters are digits.
    isdecimal : Check whether all characters are decimal.
    isnumeric : Check whether all characters are numeric.
    
    Examples
    --------
    **Checks for Alphabetic and Numeric Characters**
    
    >>> s1 = pd.Series(['one', 'one1', '1', ''])
    
    >>> s1 >> isalpha()
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    
    >>> s1 >> isnumeric()
    0    False
    1    False
    2     True
    3    False
    dtype: bool
    
    >>> s1 >> isalnum()
    0     True
    1     True
    2     True
    3    False
    dtype: bool
    
    Note that checks against characters mixed with any additional punctuation
    or whitespace will evaluate to false for an alphanumeric check.
    
    >>> s2 = pd.Series(['A B', '1.5', '3,000'])
    >>> s2 >> isalnum()
    0    False
    1    False
    2    False
    dtype: bool
    
    
    
    """
    return col.str.isalpha()   




@pipeable
def isdigit(col):
    """isdigit() method of pandas.core.strings.accessor.StringMethods instance
    Check whether all characters in each string are digits.
    
    This is equivalent to running the Python string method
    :meth:`str.isdigit` for each element of the Series/Index. If a string
    has zero characters, ``False`` is returned for that check.
    
    Returns
    -------
    Series or Index of bool
        Series or Index of boolean values with the same length as the original
        Series/Index.
    
    See Also
    --------
    isalpha : Check whether all characters are alphabetic.
    isalnum : Check whether all characters are alphanumeric.
    isdecimal : Check whether all characters are decimal.
    isnumeric : Check whether all characters are numeric.
    
    Examples
    --------
    **Checks for Alphabetic and Numeric Characters**
    
    >>> s1 = pd.Series(['one', 'one1', '1', ''])
    
    >>> s1 >> isalpha()
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    
    >>> s1 >> isnumeric()
    0    False
    1    False
    2     True
    3    False
    dtype: bool
    
    >>> s1 >> isalnum()
    0     True
    1     True
    2     True
    3    False
    dtype: bool
    
    Note that checks against characters mixed with any additional punctuation
    or whitespace will evaluate to false for an alphanumeric check.
    
    >>> s2 = pd.Series(['A B', '1.5', '3,000'])
    >>> s2 >> isalnum()
    0    False
    1    False
    2    False
    dtype: bool
    
    
    
    """
    return col.str.isdigit()       