# Crear un programa que administre una lista de tareas para agregar, eliminar y ver tareas.

tareas = []

def agregar_tarea(tarea):
    """Agrega una tarea a la lista de tareas."""
    tareas.append(tarea)
    print(f"✓ Tarea '{tarea}' agregada exitosamente.")

def eliminar_tarea(tarea):
    """Elimina una tarea de la lista de tareas si existe."""
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"✓ Tarea '{tarea}' eliminada exitosamente.")
    else:
        print(f"✗ Error: La tarea '{tarea}' no existe en la lista.")

def ver_tareas():
    """Devuelve la lista de tareas actuales."""
    if tareas:
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas registradas.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n=== ADMINISTRADOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas")
    print("4. Salir")

def main():
    """Función principal con menú interactivo."""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            tarea = input("Ingresa la tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
            else:
                print("✗ Error: No puedes agregar una tarea vacía.")
        
        elif opcion == "2":
            ver_tareas()
            tarea = input("Ingresa la tarea a eliminar: ").strip()
            if tarea:
                eliminar_tarea(tarea)
            else:
                print("✗ Error: Debes ingresar una tarea.")
        
        elif opcion == "3":
            ver_tareas()
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("✗ Error: Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
