import csv
from datetime import date

archivo = 'inventario.csv'

# Función para agregar un componente
def agregar_componente(id_comp, nombre, cantidad, estado):
    with open("inventario.txt", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([id_comp, nombre, cantidad, date.today(), estado])
    print(f"Componente {nombre} agregado.")

# Función para ver todos los componentes
def ver_inventario():
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for fila in reader:
            print(fila)

# Función para marcar como defectuoso
def marcar_defectuoso(id_comp):
    filas = []
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for fila in reader:
            if fila[0] == str(id_comp):
                fila[4] = 'defectuoso'
            filas.append(fila)
    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(filas)
    print(f"Componente {id_comp} actualizado.")