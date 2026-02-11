from pathlib import Path

# ✅ Crear una ruta es súper sencillo
carpeta = Path("usuarios")
archivo = carpeta / "config.txt"  # ¡Sí, puedes usar el operador /!

print(archivo)
# Salida (en Windows): usuarios\config.txt
# Salida (en Linux/Mac): usuarios/config.txt

# ✅ Comprobar cosas sin errores
if archivo.exists():
    print(f"El nombre del archivo es: {archivo.name}")
    print(f"La extensión es: {archivo.suffix}")
    print(f"La carpeta padre es: {archivo.parent}")