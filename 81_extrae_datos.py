

notas = [4, 6, 7, 8, 8, 10]

# ❌ MÉTODO TRADICIONAL (Con índices y slicing)
peor = notas[0]
mejor = notas[-1]
medio = notas[1:-1] # ¡Fácil equivocarse aquí!

print(medio) # [6, 7, 8, 8]


# ✅ MÉTODO PYTHONIC (Desempaquetado Ninja 🥷✨)

peor, *medio, mejor = notas

print(peor)  # Salida: 4
print(medio) # Salida: [6, 7, 8, 8]
print(mejor) # Salida: 10
