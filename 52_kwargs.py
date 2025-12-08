
def mostrar_datos(**kwargs):
  # kwargs se convierte en un diccionario
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_datos(nombre="Jose", edad=30, ciudad="Madrid")
