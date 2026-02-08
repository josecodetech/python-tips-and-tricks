

palabras = ["ana", "berto", "avión", "barco", "casa"]

# ❌ Forma "manual" (verbosa y defensiva)
grupos = {}
for palabra in palabras:
    letra_inicial = palabra[0]
    # Tienes que comprobar SIEMPRE si la clave existe
    if letra_inicial not in grupos:
        grupos[letra_inicial] = [] # Inicializas si no existe
    grupos[letra_inicial].append(palabra)

print(grupos)
# Salida: {'a': ['ana', 'avión'], 'b': ['berto', 'barco'], 'c': ['casa']}


from collections import defaultdict

# ✅ Forma Pythonica con defaultdict
# Le decimos: "Si no existe la clave, el valor por defecto será una lista nueva"
grupos_rapido = defaultdict(list)

for palabra in palabras:
    letra_inicial = palabra[0]
    # ¡Magia! ✨ No hace falta ningún 'if'.
    # Si la letra no está, crea la lista y hace el append directamente.
    grupos_rapido[letra_inicial].append(palabra)

# Funciona exactamente igual, pero el código es mucho más directo.
print(grupos_rapido)
