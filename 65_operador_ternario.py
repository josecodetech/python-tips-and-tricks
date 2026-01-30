edad = 20

# ❌ Forma "clásica" (ocupa mucho espacio para algo simple)
status = ""
if edad >= 18:
    status = "Mayor de edad"
else:
    status = "Menor de edad"

# ✅ Forma Pythonica (Operador Ternario)
# Se lee: "El status es 'Mayor' SI la edad es >= 18, SINO es 'Menor'"
status_rapido = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(status_rapido)
# Salida: Mayor de edad
