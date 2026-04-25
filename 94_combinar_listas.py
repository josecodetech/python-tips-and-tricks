

ciudades = ["Sevilla", "Andalucía", "Málaga"]
paises = ["España", "Andalucía"]

# ❌ MÉTODO ANTIGUO (Verboso y manual)
combinado = []
len_ciudades = len(ciudades)
for i in range(len_ciudades):
    ciudad = ciudades[i]
    if i < len(paises):
        pais = paises[i]
    else:
        # Relleno manual aburrido 🥱
        pais = "Desconocido"
    combinado.append(f"{ciudad} - {pais}")

print(combinado)
# ['Sevilla - España', 'Andalucía - Andalucía', 'Málaga - Desconocido']


# ✅ MÉTODO PYTHONIC (con itertools.zip_longest 🤩)
from itertools import zip_longest

ciudades = ["Sevilla", "Andalucía", "Málaga"]
paises = ["España", "Andalucía"]

# Rellena automáticamente los huecos con el valor que definas (por defecto None)
combinado = [f"{c} - {p}" for c, p in zip_longest(ciudades, paises, fillvalue="Desconocido")]

print(combinado)
# ['Sevilla - España', 'Andalucía - Andalucía', 'Málaga - Desconocido']
