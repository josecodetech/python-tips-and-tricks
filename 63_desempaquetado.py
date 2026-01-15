

datos = (10, 20, 30)
# ✅ Forma Pythonica (Desempaquetado)
a, b, c = datos

print(f"a={a}, b={b}, c={c}")
# Salida: a=10, b=20, c=30


valores = [1, 2, 3, 4, 5, 6]
# Quiero el primero, el segundo, y guardar el resto
primero, segundo, *resto = valores

print(f"Primero: {primero}") # 1
print(f"Resto: {resto}")     # [3, 4, 5, 6]