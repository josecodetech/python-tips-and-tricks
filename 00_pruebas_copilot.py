# Calcular el area de un circulo 
import math
def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2
# Ejemplo de uso
radio = 5
print(f"El área del círculo con radio {radio} es {area_circulo(radio)}")
