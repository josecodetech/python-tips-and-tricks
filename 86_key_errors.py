

data = [("A", 1), ("B", 2), ("A", 3), ("B", 4), ("C", 5)]

# ❌ MÉTODO INSEGURO Y LENTO
grupos = {}
for key, value in data:
    if key not in grupos:
        grupos[key] = [] # <-- Inicialización manual
    grupos[key].append(value)


# ✅ MÉTODO PYTHONIC (con defaultdict 🤩)
from collections import defaultdict

grupos = defaultdict(list) # <-- Definimos la fábrica de listas

for key, value in data:
    # Si 'key' no existe, se crea como [] y luego se hace append.
    grupos[key].append(value)

print(grupos)
