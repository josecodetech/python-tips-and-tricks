

votos = ["Python", "Java", "Python", "C++", "Python", "Java"]

# ❌ MÉTODO ANTIGUO (Verboso y manual)
conteo = {}
for lenguaje in votos:
    if lenguaje in conteo:
        conteo[lenguaje] += 1
    else:
        conteo[lenguaje] = 1

print(conteo) 
# {'Python': 3, 'Java': 2, 'C++': 1}


# ✅ MÉTODO PYTHONIC (con collections.Counter ✨)
from collections import Counter

votos = ["Python", "Java", "Python", "C++", "Python", "Java"]
conteo = Counter(votos)

print(conteo) 
# Counter({'Python': 3, 'Java': 2, 'C++': 1})

# ¡Y viene con superpoderes!
print(conteo.most_common(1)) # Devuelve el más votado: [('Python', 3)]


#Programacion #AprendePython #PythonTips #CleanCode #Pythonic #DataScience #DataAnalytics #Refactoring