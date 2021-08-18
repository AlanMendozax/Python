import re
correo = input("Ingrese un correo: ")

if re.match('^[(a-z,ñ0-9\_\-\.)]+@[(gmail)]+\.[(com)]{2,15}$', correo.lower()):
    print("El correo es valido ")
else:
    print("El correo no es valido")
