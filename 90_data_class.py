# ❌ MÉTODO ANTIGUO (Verboso y repetitivo)
class ProductoTradicional:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        # Necesario para que print() muestre algo útil
        return f"Producto(nombre='{self.nombre}', precio={self.precio}, stock={self.stock})"

    def __eq__(self, other):
        # Necesario para comparar si dos productos son iguales
        if not isinstance(other, ProductoTradicional):
            return NotImplemented
        return (self.nombre, self.precio, self.stock) == (other.nombre, other.precio, other.stock)

p1 = ProductoTradicional("Teclado", 49.99, 10)
print(p1) # Producto(nombre='Teclado', precio=49.99, stock=10)


# ✅ CON DATACLASSES (Limpio y Automático ✨)
from dataclasses import dataclass

@dataclass
class ProductoModerno:
    nombre: str
    precio: float
    stock: int

# ¡Python genera automáticamente __init__, __repr__, __eq__ y más!
p2 = ProductoModerno("Teclado", 49.99, 10)
print(p2) # ProductoModerno(nombre='Teclado', precio=49.99, stock=10)
print(p1 == p2) # False (son clases distintas, pero la comparación funciona)
