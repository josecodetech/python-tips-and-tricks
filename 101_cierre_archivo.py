

# ❌ MÉTODO ANTIGUO (Verboso y propenso a olvidos)
archivo = open("datos.txt", "w")
try:
    archivo.write("Hola Mundo")
    # Si hay un error aquí, el archivo podría no cerrarse bien 🛑
finally:
    archivo.close() # Cierre garantizado, pero ruidoso


# ✅ MÉTODO PYTHONIC (Limpio y seguro con Context Managers ✨)

with open("datos.txt", "w") as archivo:
    archivo.write("Hola Mundo")

