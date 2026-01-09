import random
#en un archivo guarda el stock de todas las piezas de los coches
with open ("piezas.txt", "r") as f:
    piezas=f.readlines()
    
with open ("listado.txt", "w") as archivo:
    for pieza in piezas:
        cantidad = random.randint(1, 20)
        archivo.write(f"{pieza} = {cantidad}\n")

print("Archivo 'listado.txt' creado correctamente.")
