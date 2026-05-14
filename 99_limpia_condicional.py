# Escenario: Verificar si todos los servidores están activos 
# o si hay al menos uno con error.

servidores = [
    {"nombre": "Web01", "status": "online"},
    {"nombre": "DB01", "status": "online"},
    {"nombre": "Auth01", "status": "offline"},
]

# ❌ MÉTODO ANTIGUO (Verboso con banderas/flags)
todos_online = True
para_revisar = False

for s in servidores:
    if s["status"] != "online":
        todos_online = False
        para_revisar = True
        break

print(f"¿Todos bien?: {todos_online}")


# ✅ MÉTODO PYTHONIC (Limpio y expresivo con any/all ✨)

# Verificamos si TODOS cumplen la condición
todos_ok = all(s["status"] == "online" for s in servidores)

# Verificamos si AL MENOS UNO tiene error
alerta = any(s["status"] == "offline" for s in servidores)

print(f"¿Estado verde?: {todos_ok}") # False
print(f"¿Lanzar alerta?: {alerta}")   # True