import sqlite3

# Aqui se conectar a la base de datos o se para crear una nueva
conn = sqlite3.connect('biblioteca_nolasco.db')


conn.execute('CREATE TABLE libros (\
                id INTEGER PRIMARY KEY,\
                título TEXT,\
                autor TEXT,\
                editorial TEXT,\
                año_de_publicación INTEGER,\
                isbn TEXT)')


conn.execute('CREATE TABLE usuarios (\
                id INTEGER PRIMARY KEY,\
                nombre TEXT,\
                apellido TEXT,\
                dirección TEXT,\
                correo_electrónico TEXT,\
                número_de_teléfono TEXT)')


conn.execute('CREATE TABLE préstamos (\
                id INTEGER PRIMARY KEY,\
                id_del_libro INTEGER,\
                id_del_usuario INTEGER,\
                fecha_de_préstamo TEXT,\
                fecha_de_devolución TEXT,\
                FOREIGN KEY(id_del_libro) REFERENCES libros(id),\
                FOREIGN KEY(id_del_usuario) REFERENCES usuarios(id))')

# Esto es para cerrar la conexión con la base de datos
conn.close()

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('biblioteca_nolasco.db')

# Insertar un nuevo libro
conn.execute("INSERT INTO libros (título, autor, editorial, año_de_publicación, isbn) VALUES ('El Señor de los Anillos', 'J.R.R. Tolkien', 'Editorial Martins Fontes', 1954, '9788578270691')")

# Seleccionar todos los libros
libros = conn.execute("SELECT * FROM libros").fetchall()
print(libros)

# Cerrar la conexión con la base de datos
conn.close()

# Función para conectar a la base de datos
def conectar():
    conn = sqlite3.connect('biblioteca_nolasco.db')
    return conn

# Función para insertar un nuevo libro en la tabla llamada libros
def insertar_libro(título, autor, editorial, año_de_publicación, isbn):
    conn = conectar()
    conn.execute("INSERT INTO libros (título, autor, editorial, año_de_publicación, isbn) VALUES (?, ?, ?, ?, ?)", (título, autor, editorial, año_de_publicación, isbn))
    conn.commit()
    conn.close()

# Esta función para insertar un nuevo usuario en la tabla llamada usuarios
def insertar_usuario(nombre, apellido, dirección, correo_electrónico, número_de_teléfono):
    conn = conectar()
    conn.execute("INSERT INTO usuarios (nombre, apellido, dirección, correo_electrónico, número_de_teléfono) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, dirección, correo_electrónico, número_de_teléfono))
    conn.commit()
    conn.close()

# Esta es para insertar un nuevo préstamo en la tabla llamada préstamos
def insertar_préstamo(id_del_libro, id_del_usuario, fecha_de_préstamo, fecha_de_devolución):
    conn = conectar()
    conn.execute("INSERT INTO préstamos (id_del_libro, id_del_usuario, fecha_de_préstamo, fecha_de_devolución) VALUES (?, ?, ?, ?)", (id_del_libro, id_del_usuario, fecha_de_préstamo, fecha_de_devolución))
    conn.commit()
    conn.close()

# Función para recuperar todos los libros actualmente prestados
def obtener_libros_prestados():
    conn = conectar()
    resultado = conn.execute("SELECT libros.título, usuarios.nombre, usuarios.apellido, préstamos.fecha_de_préstamo, préstamos.fecha_de_devolución \
                           FROM libros \
                           INNER JOIN préstamos ON libros.id = préstamos.id_del_libro \
                           INNER JOIN usuarios ON usuarios.id = préstamos.id_del_usuario \
                           WHERE préstamos.fecha_de_devolución IS NULL").fetchall()
    conn.close()
    return resultado

# Aqui se actualiza la fecha de devolución de un préstamo
def actualizar_fecha_devolución(id_del_préstamo, fecha_de_devolución):
    conn = conectar()
    conn.execute("UPDATE préstamos SET fecha_de_devolución = ? WHERE id = ?", (fecha_de_devolución, id_del_préstamo))
    conn.commit()
    conn.close()

    # Aqui se importa la funciones creada
 #from funciones_de_base_de_datos import *

# Se define una función para mostrar el menú y recibir la entrada del usuario
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Insertar un nuevo libro")
    print("2. Insertar un nuevo usuario")
    print("3. Realizar un préstamo")
    print("4. Actualizar la fecha de devolución de un préstamo")
    print("5. Mostrar todos los libros actualmente prestados")
    print("0. Salir")

    elección = input("Ingrese el número de opción deseado: ")
    return elección

# Este el Bucle principal del programa
while True:
    elección = mostrar_menu()

    if elección == "1":
        título = input("Ingrese el título del libro: ")
        autor = input("Ingrese el nombre del autor del libro: ")
        editorial = input("Ingrese el nombre de la editorial del libro: ")
        año = input("Ingrese el año de publicación del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        insertar_libro(título, autor, editorial, año, isbn)
        print("Libro insertado exitosamente!")

    elif elección == "2":
        nombre = input("Ingrese el primer nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        dirección = input("Ingrese la dirección del usuario: ")
        correo_electrónico = input("Ingrese la dirección de correo electrónico del usuario: ")
        número_de_teléfono = input("Ingrese el número de teléfono del usuario: ")

        insertar_usuario(nombre, apellido, dirección, correo_electrónico, número_de_teléfono)
        print("Usuario insertado exitosamente!")

    elif elección == "3":
        id_del_usuario = input("Ingrese el ID del usuario: ")
        id_del_libro = input("Ingrese el ID del libro: ")

        insertar_préstamo(id_del_usuario, id_del_libro, None, None)
        print("Préstamo realizado exitosamente!")

    elif elección == "4":
        id_del_préstamo = input("Ingrese el ID del préstamo: ")
        fecha_de_devolución = input("Ingrese la nueva fecha de devolución (formato: AAAA-MM-DD): ")

        actualizar_fecha_devolución(id_del_préstamo, fecha_de_devolución)
        print("Fecha de devolución actualizada exitosamente!")

    elif elección == "5":
        libros_prestados = obtener_libros_prestados()
        print("Libros actualmente prestados:")
        for libro in libros_prestados:
            print(f"Título: {libro[0]}, Nombre del usuario: {libro[1]} {libro[2]}, Fecha de préstamo: {libro[3]}, Fecha de devolución: {libro[4]}")

    elif elección == "0":
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

        break