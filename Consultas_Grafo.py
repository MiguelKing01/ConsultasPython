"""Importamos la libreria de python para la conexion a base de datos"""

import mysql.connector

"""atravez de la variable db se espeficica toda la conexion"""
db = mysql.connector.connect(
    user="root",
    password="12345",
    host="localhost",
    database="grafo_ciudades",
    auth_plugin="mysql_native_password",
)

"""Se utiliza el cursor para ejecutar comandos SQL y procedimientos almacenados"""
cursor = db.cursor()

"""Definimos la primera funcion que contiene el procedimiento almacenado de consultar ciudades
    la cual Consulta y muestra las ciudades según un identificador proporcionado"""


def ConsultarCiudad():
    cursor.callproc("ConsultarCiudades", (identificador,))
    for result in cursor.stored_results():
        for row in result.fetchall():
            print(row)
    db.commit()


"""Definimos la segunda funcion que contiene el procedimiento almacenado de agregar ciudades
    la cual Inserta una nueva ciudad en la base de datos"""


def AgregarCiudad(id, nombre, departamento):
    cursor.callproc("AgregarCiudades", (id, nombre, departamento))
    db.commit()
    print("Ciudad agregada correctamente.")


"""Definimos la tercera funcion que contiene el procedimiento almacenado de actualizar ciudad
    la cual Actualiza los datos de una ciudad específica"""


def actualizar_ciudad(id, nombre, departamento):
    cursor.callproc("ActualizarCiudad", (id, nombre, departamento))
    db.commit()
    print("Ciudad actualizada correctamente.")


"""Definimos la cuarta funcion que contiene el procedimiento almacenado de eliminar ciudad
    la cual Actualiza los datos de una ciudad específica"""


def eliminar_ciudad(ciudad):
    cursor.callproc("EliminarCiudad", (ciudad,))
    db.commit()
    print("Ciudad eliminada correctamente.")


"""A continuación vamos a invocar los procedimientos almacenados creados ya sea
    para agregar, consultar, actualizar o eliminar ciudades ingresando datos o quemandolos"""
actualizar_ciudad(0, "Manizales", "Caldas")
identificador = input("Ingrese la ciudad a consultar: ")
ConsultarCiudad()
ciudad = input("Ingrese el Nombre de la ciudad a eliminar: ")
eliminar_ciudad(ciudad)
AgregarCiudad(0, "Manizales", "Caldas")

"""En la siguiente parte del codigo de rutas vamos a realizar el mismo procedimiento que 
    hicimos anteriormente con las ciudades"""


def Agregar_Ruta(id, origen, destino):
    cursor.callproc("AgregarRuta", (id, origen, destino))
    db.commit()
    print("Ruta agregada correctamente.")


def Consultar_Ruta():
    cursor.callproc("ConsultarRuta", (identificador,))
    for result in cursor.stored_results():
        for row in result.fetchall():
            print(row)

    db.commit()


def Actualizar_Ruta(id, origen, destino):
    cursor.callproc("ActualizarRuta", (id, origen, destino))
    db.commit()
    print("Ruta actualizada correctamente.")


def Eliminar_Ruta(ciudad):
    cursor.callproc("EliminarRuta", (ciudad,))
    db.commit()
    print("Ruta eliminada correctamente.")


Agregar_Ruta(1, "Manizales", "Neira")
identificador = input("Ingrese la ciudad que desea consultar su ruta: ")
Consultar_Ruta()
print("Ingrese los datos a actualizar")
id = int(input("Ingrese el id de la ruta: "))
origen = input("Ingrese el origen de la ruta: ")
destino = input("Ingrese el destino de la ruta: ")
Actualizar_Ruta(id, origen, destino)
ciudad = input("Ingrese la Ciudad la cual desea eliminar su ruta: ")
Eliminar_Ruta(ciudad)
