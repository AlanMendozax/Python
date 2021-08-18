import re
Clave = "La 1 - en  + la () de su LYA1 con el LYA1 final 3 5 MO"
patron = re.compile("1")



nueva_clave = patron.sub("primera", Clave)


print(nueva_clave)
print(type (patron))
nueva_clave= re.compile("\D").sub("0",Clave)
