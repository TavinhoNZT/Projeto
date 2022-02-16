"""
    For in Python
    Iterando strings com for
    Funcao Range (start=0, stop, step=1)
"""

texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(10):
    print(numero)

for numero in range(20, 10, -1):
    print(numero)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
