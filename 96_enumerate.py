

tareas = ["Lavar", "Codear", "Dormir"]

# ❌ MÉTODO ANTIGUO (Estilo manual y ruidoso)
for i in range(len(tareas)):
    print(f"Tarea {i + 1}: {tareas[i]}")

# ✅ MÉTODO PYTHONIC (Limpio y directo con enumerate ✨)
tareas = ["Lavar", "Codear", "Dormir"]

for i, tarea in enumerate(tareas, start=1):
    print(f"Tarea {i}: {tarea}")

# Salida:
# Tarea 1: Lavar
# Tarea 2: Codear
# Tarea 3: Dormir
