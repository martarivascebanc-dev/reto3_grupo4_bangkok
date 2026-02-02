#Marta y Andoni

import sqlite3


# Conectar (o crear) la base de datos
conn = sqlite3.connect("fabricas_coches.db")
cursor = conn.cursor()

# Crear tabla de fábricas
cursor.execute("""
CREATE TABLE IF NOT EXISTS fabrica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais TEXT NOT NULL
)
""")

# Crear tabla de coches
cursor.execute("""
CREATE TABLE IF NOT EXISTS coche (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    precio REAL NOT NULL,
    fabrica_id INTEGER,
    FOREIGN KEY (fabrica_id) REFERENCES fabrica(id)
)
""")

# Insertar fábricas
cursor.executemany("""
INSERT INTO fabrica (nombre, pais)
VALUES (?, ?)
""", [
    ("Toyota", "Japón"),
    ("Volkswagen", "Alemania"),
    ("Ford", "Estados Unidos")
])

# Insertar coches
cursor.executemany("""
INSERT INTO coche (modelo, precio, fabrica_id)
VALUES (?, ?, ?)
""", [
    ("Corolla", 22000, 1),
    ("Yaris", 18000, 1),
    ("Golf", 27000, 2),
    ("Mustang", 45000, 3)
])

conn.commit()

# Consulta: mostrar coches con su fábrica
cursor.execute("""
SELECT coche.modelo, coche.precio, fabrica.nombre, fabrica.pais
FROM coche
JOIN fabrica ON coche.fabrica_id = fabrica.id
""")

resultados = cursor.fetchall()

print("COCHES Y SUS FÁBRICAS:")
for modelo, precio, fabrica, pais in resultados:
    print(f"- {modelo} | {precio}€ | {fabrica} - {pais}")

# Cerrar conexión
conn.close()
