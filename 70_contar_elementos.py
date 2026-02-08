from collections import Counter

palabras = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]

# ❌ Forma "manual" (lenta y verbosa)
conteo_manual = {}
for palabra in palabras:
    if palabra in conteo_manual:
        conteo_manual[palabra] += 1
    else:
        conteo_manual[palabra] = 1
# Resultado: {'manzana': 3, 'pera': 2, 'uva': 1}


# ✅ Forma Pythonica con Counter (¡Magia instantánea!)
conteo_rapido = Counter(palabras)

print(conteo_rapido)
# Salida: Counter({'manzana': 3, 'pera': 2, 'uva': 1})


print(conteo_rapido.most_common(2))
# Salida: [('manzana', 3), ('pera', 2)]
