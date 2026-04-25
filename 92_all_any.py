

notas = [8, 9, 7, 10, 6]

# ❌ MÉTODO ANTIGUO (Uso de "flags" y bucles)
aprobado_todo = True
for nota in notas:
    if nota < 5:
        aprobado_todo = False
        break # Detenemos el bucle por eficiencia

print(aprobado_todo) # True


# ✅ MÉTODO PYTHONIC (Limpio, directo y en una línea ✨)
notas = [8, 9, 7, 10, 6]

# ¿Aprobó TODAS? (Devuelve True solo si todas cumplen la condición)
aprobado_todo = all(nota >= 5 for nota in notas)

# ¿Tiene AL MENOS un 10? (Devuelve True si alguna cumple la condición)
tiene_excelencia = any(nota == 10 for nota in notas)

print(f"Todo aprobado: {aprobado_todo}") # True
print(f"Tiene excelencia: {tiene_excelencia}") # True
