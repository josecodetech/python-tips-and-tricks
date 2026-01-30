
def sumar_todo(*numeros):
    # 'numeros' será una tupla con todo lo que recibas: (1, 5, 10, ...)
    total = sum(numeros)
    return print(f"La suma total es: {total}")

sumar_todo(5, 10)         # Salida: La suma total es: 15
sumar_todo(1, 2, 3, 4, 5) # Salida: La suma total es: 15


def info_usuario(**datos):
    # 'datos' será un diccionario: {'nombre': 'Ana', 'edad': 30, ...}
    for clave, valor in datos.items():
        print(f"- {clave.capitalize()}: {valor}")

info_usuario(nombre="Ana", edad=30, ciudad="Madrid")
# Salida:
# - Nombre: Ana
# - Edad: 30
# - Ciudad: Madrid
