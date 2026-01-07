
nombres = ["Ana", "Luis", "Maria"]
edades = [25, 30, 28]

# zip combina los elementos de ambas listas en pares
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Salida:
# Ana tiene 25 años
# Luis tiene 30 años
# Maria tiene 28 años
