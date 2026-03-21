
# ❌ MÉTODO ANTIGUO/INSEGURO (Manual)
f = open("datos.txt", "r")
# Si ocurre un error aquí, el archivo podría quedar abierto.
print(f.read())
f.close() # <-- Es fácil olvidar esta línea

# ✅ MÉTODO MODERNO/SEGURO (con with)
with open("datos.txt", "r") as f:
    # Python gestiona el archivo automáticamente
    print(f.read())
    # Al salir del bloque, el archivo se cierra SOLO, pase lo que pase.
