

datos = [
    ("Funcional", "Haskell"),
    ("Orientado a Objetos", "Java"),
    ("Funcional", "Scala"),
    ("Orientado a Objetos", "Python")
]

# ❌ MÉTODO ANTIGUO (Verboso y con chequeos manuales)
agrupados = {}
for paradigma, lenguaje in datos:
    if paradigma not in agrupados:
        agrupados[paradigma] = []
    agrupados[paradigma].append(lenguaje)

print(agrupados)
# {'Funcional': ['Haskell', 'Scala'], 'Orientado a Objetos': ['Java', 'Python']}


# ✅ MÉTODO PYTHONIC (Limpio y directo con defaultdict ✨)
from collections import defaultdict

datos = [
    ("Funcional", "Haskell"),
    ("Orientado a Objetos", "Java"),
    ("Funcional", "Scala"),
    ("Orientado a Objetos", "Python")
]

# Le decimos que el valor por defecto sea una lista vacía: list
agrupados = defaultdict(list)

for paradigma, lenguaje in datos:
    # No hace falta comprobar si existe, ¡Python se encarga!
    agrupados[paradigma].append(lenguaje)

print(dict(agrupados))
