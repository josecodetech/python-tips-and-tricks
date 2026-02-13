

user = {"nombre": "Ana", "rol": "admin"}
config = {"tema": "oscuro", "rol": "superadmin"}



# ❌ MÉTODOS ANTIGUOS

# Opción 1: .update() -> ¡CUIDADO! Modifica el diccionario 'user' original.
# user.update(config) 

# Opción 2: Desempaquetado -> Funciona, pero la sintaxis es extraña para leer.
perfil = {**user, **config} 


# ✅ MÉTODO MODERNO (Python 3.9+)
perfil = user | config

print(perfil)
# Salida: {'nombre': 'Ana', 'tema': 'oscuro', 'rol': 'superadmin'}
