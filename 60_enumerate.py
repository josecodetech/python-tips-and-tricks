frutas = ["manzana", "banana", "cereza"]

# ❌ Forma antigua (menos limpia)
# i = 0
# for fruta in frutas:
#     print(f"{i}: {fruta}")
#     i += 1

# ✅ Forma Pythonica con enumerate()
# "desempaquetamos" el índice (i) y el valor (fruta) directamente
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

# Salida:
# Índice 0: manzana
# Índice 1: banana
# Índice 2: cereza