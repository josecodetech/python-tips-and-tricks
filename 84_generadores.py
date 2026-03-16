import sys

n = 10_000_000 # 10 millones

# ❌ CON LIST COMPREHENSION (Inseguro para grandes datos)
# Genera y guarda los 10 millones de cuadrados de una vez.
cuadrados_lista = [x**2 for x in range(n)]

# Verificamos el tamaño en RAM: ¡Pesa cientos de MB!
print(f"RAM Lista: {sys.getsizeof(cuadrados_lista) / 1024 / 1024:.2f} MB")
# Salida: ~80-90 MB (dependiendo de la arquitectura)

# ✅ CON EXPRESIÓN GENERADORA (Súper Eficiente ✨)
# Solo crea el objeto generador, no los datos.
cuadrados_gen = (x**2 for x in range(n))

# Verificamos el tamaño en RAM: ¡Pesa solo unos bytes!
print(f"RAM Generador: {sys.getsizeof(cuadrados_gen)} bytes")
# Salida: ~100-200 bytes (¡Prácticamente nada!)
