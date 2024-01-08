'''import re
data= 
    Both patterns and strings to be searched can be Unicode strings (str) as
    well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot 
    be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa;
    similarly, when asking for a substitution, the replacement string must be of the same
    type as both the pattern and the search string

pattern =re.compile(r'/d')
result =pattern.finditer(data)
for l in (list(result)):
 print(l)
 '''
'''
import re
match = re.search('ing', 'you are doing good.Having nice thought')
print(match)
text='you are doing good.Having nice thought'
matches=re.finditer('ing', 'you are doing good.Having nice thought')
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])'''

import re

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.group('first_name',flag=0)
m.group('last_name')

text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

