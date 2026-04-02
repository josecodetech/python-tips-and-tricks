
nombres = ["Ana", "Luis", "Carlos"]
edades = [28, 34, 25]

# ❌ MÉTODO ANTIGUO (Propenso a errores de índice)
for i in range(len(nombres)):
    nombre = nombres[i]
    edad = edades[i]
    print(f"{nombre} tiene {edad} años")


# ✅ MÉTODO PYTHONIC (Limpio y Seguro ✨)
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
