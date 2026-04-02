

productos = ["manzana", "platano", "cereza"]

# ❌ MÉTODO ANTIGUO (No Pythonic y propenso a errores)
for i in range(len(productos)):
    producto = productos[i]
    print(f"[{i}] -> {producto}")


# ✅ MÉTODO PYTHONIC (Limpio y elegante ✨)
for i, producto in enumerate(productos):
    print(f"[{i}] -> {producto}")
