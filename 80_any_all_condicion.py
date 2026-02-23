

numeros = [2, 4, 6, 8, 10]

# ❌ MÉTODO TRADICIONAL (Largo y verboso)
todos_pares = True
for num in numeros:
    if num % 2 != 0:
        todos_pares = False
        break

print(todos_pares) # True


# ✅ MÉTODO PYTHONIC (Corto y Elegante ✨)

# ¿Son TODOS pares?
todos_pares = all(num % 2 == 0 for num in numeros)

# ¿Hay ALGÚN número mayor que 9?
hay_mayores = any(num > 9 for num in numeros)

print(todos_pares)  # Salida: True
print(hay_mayores)  # Salida: True
