
numeros = [1, 2, 3, 4, 5, 6]

# Usamos filter junto con una función lambda para
# quedarnos solo con los números pares (donde la condición es True)
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
