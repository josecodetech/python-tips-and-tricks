numeros = [1, 2, 3, 4, 5, 6]

# ❌ MÉTODO TRADICIONAL (Verboso)
cuadrados_pares = []
for num in numeros:
    if num % 2 == 0:
        cuadrados_pares.append(num**2)

print(cuadrados_pares) 
# Salida: [4, 16, 36]

# ✅ LIST COMPREHENSION (Pythonic ✨)
# La sintaxis es: [expresion for elemento in iterable if condicion]
cuadrados_pares_pro = [num**2 for num in numeros if num % 2 == 0]

print(cuadrados_pares_pro)
# Salida: [4, 16, 36]
