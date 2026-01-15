nombres = ["Ana", "Berto", "Carla", "Daniel"]

# Objetivo: Crear un diccionario donde la CLAVE es el nombre
# y el VALOR es el número de letras que tiene.

# ❌ Forma "clásica" (verbosa)
longitudes_dict = {}
for nombre in nombres:
    longitudes_dict[nombre] = len(nombre)

# ✅ Forma Pythonica con Dict Comprehension
# Usamos llaves {} y definimos la estructura clave:valor
longitudes_dict = {nombre: len(nombre) for nombre in nombres}

print(longitudes_dict)
# Salida: {'Ana': 3, 'Berto': 5, 'Carla': 5, 'Daniel': 6}
