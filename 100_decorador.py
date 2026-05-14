

import time

def medir_tiempo(func):
    def envoltorio(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        print(f"⏱️ Tardó {time.time() - inicio:.2f} seg")
        return resultado
    return envoltorio

@medir_tiempo
def proceso_complejo():
    time.sleep(2) # Simulamos trabajo
    print("✅ Proceso terminado")

proceso_complejo()
# ✅ Proceso terminado
# ⏱️ Tardó 2.00 seg

