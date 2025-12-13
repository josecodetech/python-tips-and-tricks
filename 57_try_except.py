
try:
  # Intentamos ejecutar un código que podría fallar
  resultado = 10 / 0
  print(f"El resultado es: {resultado}")
except ZeroDivisionError:
  # Si ocurre el error específico, ejecutamos este bloque
  print("¡Error! No puedes dividir por cero.")

# El programa continúa su ejecución normal
print("Continuando con el programa...")
