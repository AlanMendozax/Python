import re
regex = re.compile(r'\s+')
text = "     test1 test2     test3\ntest4  \ntest5   "

result = regex.sub('-', text)
print(result)