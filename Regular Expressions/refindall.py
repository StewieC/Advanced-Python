"""
return all non-overlapping matches of pattern in string,
as a list of strings. the string is scanned left to right and matches are rerutned in order found
"""

#this code uses a regular expression (\d+) to find all the sequences of one or more digits in the given string
# it searches for numeric values and stores them in a list

import re
s = """im stewie , reg 2250 and born in 2004"""

regex = '\d+'
match = re.findall(regex, s)
print(match)