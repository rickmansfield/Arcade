"""
PYTHON syntax to look up most common methods
"""
import builtins
import math
import collections
import typing
from collections import Counter
from collections import UserString
from typing import Counter

"""
To search a term like "sort" which is a chainable function you must first search the variable. 
Example... 
def someFunction(arrayVariableName)
print(help(arraryVariableName))
print(someFunction([[6, 2, 3, 8]]))
...the resulting print will produce a list of all the options available to arrayVariableName including "sort" with it's explaination. 
"""
print(dir(builtins))
print(help(max)) 
# max(iterable, *[, default=obj, key=func]) -> value
# max(arg1, arg2, *args, *[, key=func]) -> value
# With a single iterable argument, return its biggest item.
# default keyword-only argument specifies an object to return if the provided iterable is empty.
# With two or more arguments, return the largest argument.
print(help([].pop))
print(help(str.pop))
print(help(set)) # Build an unordered collection of unique elements.( no duplicates)
print(help(str))
print(help(int))
print(help({}))
    # new dictionary initialized from a mapping object's (key, value) pairs
print(help(tuple))
    #  If no argument is given, the constructor returns an empty tuple.
    #  If iterable is specified the tuple is initialized from iterable's items.
print(help(sorted)) 
    # returns new sorted list in ascending order. Sort is customizable and reverse flag can be applied
print(help(list))
    # If no argument is given, the constructor creates a new empty list.
    # The argument must be an iterable if specified.
print(help(dict))
print(help(dict.values))
    #  an object providing a view on D's values
print(help(dict.get))
    # Return the value for key if key is in the dictionary, else default.
print(help(""))
    # returns a huge list of possibilities including "".join
print(help("".split)) # isolates each string by itself. Example ["push 1"] becomes ["push", "1"]
print(help("".join)) # removes spaces in a string
print(help(",".join)) # adds comma between strings
print(help(range))
print(help(reversed)) # returns reversed list of characters separated by a commma
print(help(map)) # needs two arguments (function, iterable) example (str, array)
print(help(Counter))
# |  Dict subclass for counting hashable items.  Sometimes called a bag
#  |  or multiset.  Elements are stored as dictionary keys and their counts
#  |  are stored as dictionary values.

"""
Resources
https://docs.python.org/3.6/search.html?q=
https://github.com/LambdaSchool
https://github.com/LambdaSchool/CS-Wiki
https://github.com/LambdaSchool/CS-Wiki/wiki/Javascript-Python-cheatsheet
https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Read-Specifications-and-Code
https://docs.python.org/3.6/library/
"""

""" 
String options 
    isalnum(self)
 |  isalpha(self)
 |  isascii(self)
 |  isdecimal(self)
 |  isdigit(self)
 |  isidentifier(self)
 |  islower(self)
 |  isnumeric(self)
 |  isprintable(self)
 |  isspace(self)
 |  istitle(self)
 |  isupper(self)
 |  join(self, seq)
 |  ljust(self, width, *args)
 |  lower(self)
 |  lstrip(self, chars=None)
 |  partition(self, sep)
 |  removeprefix(self, prefix, /)
 |  removesuffix(self, suffix, /)
 |  replace(self, old, new, maxsplit=-1)
 |  rfind(self, sub, start=0, end=9223372036854775807)
 |  rindex(self, sub, start=0, end=9223372036854775807)
 |  rjust(self, width, *args)
 |  rpartition(self, sep)
 |  rsplit(self, sep=None, maxsplit=-1)
 |  rstrip(self, chars=None)
 |  split(self, sep=None, maxsplit=-1)
 |  splitlines(self, keepends=False)
 |  startswith(self, prefix, start=0, end=9223372036854775807)
 |  strip(self, chars=None)
 |  swapcase(self)  
 |  title(self)
 |  translate(self, *args)
 |  upper(self)
|  zfill(self, width)
    """