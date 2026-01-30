
numeros = [1, 2, 3, 4, 5]

# ❌ Forma "clásica" (Demasiado código para algo tan simple)
def cuadrado(x):
    return x ** 2

# Tenemos que definir la función antes de usarla
cuadrados = list(map(cuadrado, numeros))


# ✅ Forma Pythonica con Lambda (¡Todo en una línea!)
# Se lee: "Para cada elemento, aplica una función que toma 'x' y devuelve 'x al cuadrado'"
cuadrados_rapido = list(map(lambda x: x ** 2, numeros))

print(cuadrados_rapido)
# Salida: [1, 4, 9, 16, 25]


gente = [("Ana", 30), ("Berto", 25), ("Carla", 35)]

# Ordenamos usando una lambda como 'key'
# La lambda le dice a sort: "Usa el elemento en el índice 1 (la edad) para comparar"
gente.sort(key=lambda persona: persona[1])

print(gente)
# Salida: [('Berto', 25), ('Ana', 30), ('Carla', 35)]
