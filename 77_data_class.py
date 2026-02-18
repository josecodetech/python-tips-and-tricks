# ❌ CLASE TRADICIONAL (Mucho código manual)
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock})"

# ✅ CON DATACLASS (Automático y Limpio ✨)
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0  # ¡Incluso soporta valores por defecto!

# El resultado es idéntico, pero escribiste 3 veces menos código.
item = Producto("Laptop", 999.99)
print(item) 
# Salida: Producto(nombre='Laptop', precio=999.99, stock=0)
