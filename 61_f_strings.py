nombre = "Ana"
edad = 30
puntuacion = 98.5

# ❌ Forma antigua (liosa y propensa a errores con los tipos)
# mensaje = "Hola, soy " + nombre + " y tengo " + str(edad) + " años."

# ✅ Forma moderna con f-string (¡Mira qué limpieza!)
mensaje = f"Hola, soy {nombre} y tengo {edad} años."
print(mensaje)

# 🚀 Bonus: ¡Puedes meter expresiones dentro!
print(f"El doble de mi puntuación es {puntuacion * 2}")

# Salida:
# Hola, soy Ana y tengo 30 años.
# El doble de mi puntuación es 197.0
