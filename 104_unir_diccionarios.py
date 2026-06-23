


perfil = {"nombre": "Jose", "rol": "Admin"}
ajustes = {"rol": "SuperAdmin", "modo": "oscuro"}

# ❌ El método antiguo y ruidoso
resultado = {**perfil, **ajustes}

# ✅ El método moderno y limpio ✨
resultado = perfil | ajustes

print(resultado)
# {'nombre': 'Jose', 'rol': 'SuperAdmin', 'modo': 'oscuro'}
