from typing import NamedTuple

# ✅ Definimos la estructura
class Dimensiones(NamedTuple):
    ancho: int
    alto: int
    unidad: str

def obtener_pantalla():
    return Dimensiones(1920, 1080, "px")

# ¡Ahora el código se explica solo!
pantalla = obtener_pantalla()

print(f"Resolución: {pantalla.ancho}x{pantalla.alto} {pantalla.unidad}")
# Salida: Resolución: 1920x1080 px
