

from enum import Enum

# ✅ Definimos un grupo de constantes con nombre
class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

# Ahora el código es legible para humanos
status = EstadoPedido.ENVIADO

if status == EstadoPedido.ENVIADO:
    print("¡Tu paquete está en camino!")

