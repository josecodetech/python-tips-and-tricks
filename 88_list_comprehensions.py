# Un bucle tradicional que todos conocemos:
numeros = [1, 2, 3, 4, 5]

# ❌ MÉTODO ANTIGUO
cuadrados = []
for n in numeros:
    cuadrados.append(n * n)

# ✅ MÉTODO PYTHONIC (Una línea, claro y elegante ✨)
cuadrados = [n * n for n in numeros]
print(cuadrados)  # Output: [1, 4, 9, 16, 25]

