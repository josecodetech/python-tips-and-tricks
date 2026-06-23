

from dataclasses import dataclass

# ✅ Con una simple etiqueta, Python escribe el código por ti
@dataclass
class Sensor:
    id_sensor: str
    tipo: str
    activo: bool = True

temperatura = Sensor(id_sensor="T-01", tipo="Térmico")

print(temperatura)
# Sensor(id_sensor='T-01', tipo='Térmico', activo=True)

