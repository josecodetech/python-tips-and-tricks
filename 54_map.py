numeros = [1, 2, 3, 4]

# Usamos map junto con una función lambda para elevar al cuadrado
# map devuelve un iterador, así que lo convertimos a lista
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
# Salida: [1, 4, 9, 16]