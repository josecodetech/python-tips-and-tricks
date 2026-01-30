

frutas = ["manzana", "banana", "cereza"]

# ❌ Forma "antigua" (estilo C/Java, poco Pythonica)
# Es verbosa y un poco difícil de leer
for i in range(len(frutas)):
    item = frutas[i]
    print(f"Índice {i}: {item}")


# ✅ Forma Pythonica con enumerate()
# Desempaquetamos el índice y el valor directamente en el bucle
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Salida:
# Índice 0: manzana
# Índice 1: banana
# Índice 2: cereza


for numero, tarea in enumerate(["Estudiar", "Hacer deporte"], start=1):
     print(f"Tarea #{numero}: {tarea}")

# Salida:
# Tarea #1: Estudiar
# Tarea #2: Hacer deporte
