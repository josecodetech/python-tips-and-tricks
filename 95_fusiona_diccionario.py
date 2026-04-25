

config_base = {"tema": "oscuro", "idioma": "es"}
config_usuario = {"idioma": "en", "notificaciones": True}

# ❌ MÉTODOS ANTIGUOS (Poco intuitivos o verbosos)

# Opción A (Requiere múltiples líneas):
resultado = config_base.copy()
resultado.update(config_usuario)

# Opción B (Desempaquetado, críptico para principiantes):


# ✅ MÉTODO PYTHONIC (A partir de Python 3.9 ✨)

resultado = config_base | config_usuario

print(resultado)
# {'tema': 'oscuro', 'idioma': 'en', 'notificaciones': True}


#JoseCodeTech #Programacion #AprendePython #PythonTips #CleanCode #Pythonic #DataScience #WebDev #Backend