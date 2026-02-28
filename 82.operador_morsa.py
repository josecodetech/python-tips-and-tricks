


texto = "Programación en Python"

# ❌ MÉTODO TRADICIONAL (Dos pasos)
longitud = len(texto)
if longitud > 10:
    print(f"El texto es muy largo, tiene {longitud} caracteres.")


# ✅ MÉTODO MODERNO (Operador Morsa 🦭)
# Asignamos 'longitud' y verificamos la condición ¡todo a la vez!

if (longitud := len(texto)) > 10:
    print(f"El texto es muy largo, tiene {longitud} caracteres.")

