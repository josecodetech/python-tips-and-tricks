import os

# ❌ MÉTODO ANTIGUO (Cadena de texto, difícil de leer)
user_home = os.path.expanduser("~")
directorio = os.path.join(user_home, "data")
ruta_final = os.path.join(directorio, "results.csv")

print(ruta_final)
# /home/usuario/data/results.csv (o C:\Users\usuario\data\results.csv)


# ✅ CON PATHLIB (Objetos inteligentes ✨)
from pathlib import Path

# Obtenemos el home directory
user_home = Path.home()

# ¡Magia! Usamos / para concatenar rutas de forma natural
ruta_final = user_home / "data" / "results.csv"

print(ruta_final)
# /home/usuario/data/results.csv
print(type(ruta_final)) # <class 'pathlib.PosixPath' o WindowsPath>


