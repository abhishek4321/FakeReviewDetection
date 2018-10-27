import re


l = "Page 1 of 123"
r3 = re.compile('[0-9].*')
r = re.compile('f [0-9].*')
s = r.search(l)
s = r3.search(s.group())
print s.group()

