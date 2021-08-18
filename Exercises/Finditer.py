import re
cadena = 'tengo una yama que yama se llama'
iterador = re.finditer('ama', cadena)
for encontrado in iterador:
    print(encontrado.span())  # (11, 14) , (20, 23) , (29, 32)
