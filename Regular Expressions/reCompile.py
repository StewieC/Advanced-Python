"""
regular expressions are compiled into pattern objects, which have methods for various operations
such as searchinf for pattern matches or performing string substitutions
"""
# this code uses regex pattern [a-e] to find a list of lowercase letters from 'a' to 'e'

import re
s = re.compile('[a-e]')
print(s.findall(" A red leather jacket like michale jackson"))

# first occurence is e and not A because it is case sensitive