'''
Usage of regex
'''

import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) # find only first occurance

if match:
  print(match.group())
else:
  print("pattern not found")

print(string[match.span()[0]:match.span()[1]])