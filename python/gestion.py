#Marta

import csv
from datetime import date
import os


archivo = 'inventario.csv'

# Crear archivo si no existe
if not os.path.exists(archivo):
    with open(archivo, 'w', newline='') as f:
        pass

# Función para agregar un componente
def agregar_componente(id_comp, nombre, cantidad, estado):
    with open(archivo, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_comp, nombre, cantidad, date.today(), estado])
    print(f"Componente {nombre} agregado.")

# Función para ver todos los componentes
def ver_inventario():
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        print("\nID | Nombre | Cantidad | Fecha | Estado")
        print("-" * 40)
        for fila in reader:
            print(" | ".join(fila))

# Función para marcar como defectuoso
def marcar_defectuoso(id_comp):
    filas = []
    encontrado = False

    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for fila in reader:
            if fila[0] == str(id_comp):
                fila[4] = 'defectuoso'
                encontrado = True
            filas.append(fila)

    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(filas)

    if encontrado:
        print(f"Componente {id_comp} actualizado a defectuoso.")
    else:
        print("Componente no encontrado.")

# Programa principal
def menu():
    while True:
        print("\n--- INVENTARIO FABRICADOS LOPEZ ---")
        print("1. Agregar componente")
        print("2. Ver inventario")
        print("3. Marcar componente como defectuoso")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_comp = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = input("Cantidad: ")
            estado = input("Estado (bueno/defectuoso): ")
            agregar_componente(id_comp, nombre, cantidad, estado)

        elif opcion == "2":
            ver_inventario()

        elif opcion == "3":
            id_comp = input("ID del componente: ")
            marcar_defectuoso(id_comp)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    print("Bienvenidos a la base de datos de Fabricados Lopez")
    menu()
