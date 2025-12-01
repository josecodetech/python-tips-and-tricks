
def sumar_todo(*args):
  # args se convierte en una tupla con todos los valores
  return sum(args)

print(sumar_todo(1, 2, 3, 4))  # Salida: 10
print(sumar_todo(10, 20))      # Salida: 30
