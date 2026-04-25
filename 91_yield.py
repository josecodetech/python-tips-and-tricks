

import sys

# ❌ FUNCIÓN ESTÁNDAR (Guarda todo en RAM)
def cuadrado_lista(n):
    resultado = []
    for i in range(n):
        resultado.append(i * i)
    return resultado # Devuelve la lista completa

n = 10_000_000 # 10 millones
p1_lista = cuadrado_lista(n)
#print(p1_lista) # ¡Cuidado si lo imprimes!
print(f"RAM Lista (estándar): {sys.getsizeof(p1_lista) / 1024 / 1024:.2f} MB")
# Salida: ~80-90 MB (dependiendo de tu arquitectura)


# ✅ FUNCIÓN GENERADORA (Calcula bajo demanda ✨)
def cuadrado_generador(n):
    for i in range(n):
        yield i * i # Devuelve el valor, pausa y recuerda estado

p2_gen = cuadrado_generador(n) # No calcula nada aún
#print(p2_gen) # Salida: <generator object...>
print(f"RAM Objeto Generador: {sys.getsizeof(p2_gen)} bytes")
# Salida: ~100-200 bytes (¡Prácticamente nada!)


#JoseCodeTech #Programacion #AprendePython #PythonTips #Generadores #Yield #ResourceManagement #LazyEvaluation #CleanCode #DataScience #DataEngineering