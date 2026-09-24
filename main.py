# Sistema de Gestión de Materiales de Construcción

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE MATERIALES ---")
    print("1. Ver inventario de materiales")
    print("2. Agregar nuevo material")
    print("3. Salir")

def gestionar_inventario():
    inventario = [
        {"nombre": "Cemento (bolsas)", "cantidad": 50},
        {"nombre": "Varilla de Fierro 1/2", "cantidad": 120},
        {"nombre": "Ladrillo King Kong", "cantidad": 1000}
    ]

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print("\n--- INVENTARIO ACTUAL ---")
            for idx, item in enumerate(inventario, 1):
                print(f"{idx}. {item['nombre']}: {item['cantidad']} unidades")
        elif opcion == "2":
            nombre = input("Nombre del material: ")
            try:
                cantidad = int(input("Cantidad disponible: "))
                inventario.append({"nombre": nombre, "cantidad": cantidad})
                print(f"¡{nombre} agregado exitosamente!")
            except ValueError:
                print("Error: Ingresa un número válido para la cantidad.")
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    gestionar_inventario()