import re
s = 'stewart is a winger in the field'
match = re.search(r'stewart', s)
print('start index: ', match.start())
print('end index: ', match.end())