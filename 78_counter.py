
frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]

# ❌ MÉTODO MANUAL (Largo y aburrido)
conteo = {}
for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] += 1
    else:
        conteo[fruta] = 1

print(conteo)
# {'manzana': 3, 'pera': 2, 'uva': 1}


# ✅ CON COUNTER (Rápido y Potente ✨)
from collections import Counter

conteo = Counter(frutas)

print(conteo)
# Counter({'manzana': 3, 'pera': 2, 'uva': 1})


