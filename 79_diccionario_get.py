

usuario = {"nombre": "Carlos", "rol": "editor"}

# ❌ MÉTODO INSEGURO Y VERBOSO
if "edad" in usuario:
    edad = usuario["edad"]
else:
    edad = "Desconocida"


# ✅ MÉTODO PYTHONIC (Seguro y en una línea ✨)
edad = usuario.get("edad", "Desconocida")

print(edad) 
# Salida: Desconocida (¡Y el programa sigue funcionando!)
