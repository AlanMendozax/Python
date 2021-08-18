import re
cadena = 'tengo una yama que yama se llama'
lista = re.findall('..ama', cadena)
print(lista)  # muestra: [' yama', ' yama', 'llama']
