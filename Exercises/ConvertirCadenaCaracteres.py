import re
t = "La 1 - en  + la () de su LYA1 con el LYA1 final 3 5 MO"
nc= re.compile("1").sub("primera",t)
nc= re.compile("-").sub("persona",nc)
nc= re.compile("\+").sub("mandarme",nc)
nc= re.compile("()").sub("foto",nc)
nc= re.compile("LYA1").sub("programa",nc)
nc= re.compile("3").sub("obtiene",nc)
nc= re.compile("MO").sub("extra",nc)
print(nc)
