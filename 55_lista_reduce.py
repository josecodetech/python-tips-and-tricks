from functools import reduce

numeros = [1, 2, 3, 4]

# Usamos reduce con una función lambda para multiplicar
# todos los elementos de forma acumulativa:
# (((1 * 2) * 3) * 4) = 24
producto = reduce(lambda x, y: x * y, numeros)

print(producto)
