import os

# ❌ MÉTODO ANTIGUO (Tratando rutas como strings)
directorio = "usuarios"
subfolder = "config"
archivo = "settings.json"

ruta = os.path.join(directorio, subfolder, archivo)
print(ruta) # usuarios/config/settings.json (o con \ en Windows)


# ✅ MÉTODO PYTHONIC (Elegancia pura con pathlib ✨)
from pathlib import Path

directorio = Path("usuarios")
ruta = directorio / "config" / "settings.json"

print(ruta) 
# ¡Mira qué fácil! El operador "/" une las rutas de forma inteligente.

# Además, tienes superpoderes:
print(ruta.exists())      # ¿Existe el archivo?
print(ruta.suffix)      # .json
print(ruta.stem)        # settings


#JoseCodeTech #Programacion #AprendePython #PythonTips #CleanCode #Pythonic #Pathlib #SoftwareDevelopment #TipsDeProgramacion