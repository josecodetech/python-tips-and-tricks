
numeros = [1, 2, 3, 4, 5]

# ❌ Forma "clásica" (más verbosa)
cuadrados = []
for num in numeros:
    cuadrados.append(num ** 2)

# ✅ Forma Pythonica con List Comprehension
# Se lee: "Haz num al cuadrado PARA CADA num EN la lista numeros"
cuadrados = [num ** 2 for num in numeros]

print(cuadrados)
# Salida: [1, 4, 9, 16, 25]


# Solo los cuadrados de los números pares
pares_cuadrados = [num ** 2 for num in numeros if num % 2 == 0]
# Salida: [4, 16]
