


usuarios = ["Ana", "Berto", "Carla"]
puntos = [150, 200, 180]


# ❌ Forma "clásica" (torpe con índices)
for i in range(len(usuarios)):
    print(f"{usuarios[i]}: {puntos[i]} puntos")


# ✅ Forma Pythonica con zip()
# Desempaquetamos el par (usuario, punto) directamente
for usuario, punto in zip(usuarios, puntos):
    print(f"{usuario}: {punto} puntos")

# Salida:
# Ana: 150 puntos
# Berto: 200 puntos
# Carla: 180 puntos


lista_larga = [1, 2, 3, 4, 5]
lista_corta = ["a", "b"]

for numero, letra in zip(lista_larga, lista_corta):
    print(numero, letra)
# Salida:
# 1 a
# 2 b
# (Los números 3, 4, 5 se ignoran)
