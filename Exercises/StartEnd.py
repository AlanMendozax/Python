import re
mo1 = re.search('agua', 'paraguas')
print(mo1.start())  # devuelve 3
print(mo1.end())  # devuelve 7
