import mysql.connector
from mysql.connector import cursor
from mysql.connector.constants import CNX_POOL_ARGS
from tabulate import tabulate

def accedeMariadb():
    usuario = input("Ingrese su usuario local de MariaDB: ")
    contraseña = input("Ingrese la contraseña correspondiente a su usuario de MariaDB: ")
    while True:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=usuario,
                password=contraseña
            )
            break
        except:
            print("Usuario o contraseña incorrectos, por favor, ingréselos nuevamente")
            usuario = input("Ingrese su usuario local de MariaDB: ")
            contraseña = input("Ingrese la contraseña correspondiente a su usuario de MariaDB: ")
    return usuario, contraseña

def preguntanum():
    print("1.-¿Cuántas comunas pertenecen a cada región?")
    print("2.-¿Cuál es la región con la mayor población?")
    print("3.-¿Cuáles son las comunas cuya población es mayor a * habitantes?")
    print("4.-¿Cuál es el promedio de superficie de las comunas en cada región?")
    print("5.-¿Cuál es la población total en cada región?")
    print("6.-¿Cuál es la región con la mayor superficie total de comunas?")
    print("7.-¿Cuál es el establecimiento de educación con la menor longitud de coordenadas (latitud + longitud)?")
    print("8.-¿Cuál es la región con la menor población total en sus comunas?")
    print("9.-¿Cuál es el promedio de población en el sector de trabajo en todas las comunas?")
    print("10.-Ordena las regiones de Chile de mayor a menor población")
    print("11.-¿Cuál es la comuna con el mayor número de desempleados?")
    print("12.-Lista todos los establecimientos educacionales de la comuna de *")
    print("13.-¿Cuál es la comuna con menor cantidad de Centros de Salud?")
    print("14.-¿Cuál es la cantidad de recintos de tipo * por región?")
    consulta = int(input("Ingrese el número de la consulta que desea hacer a la base de datos: "))
    while consulta not in range(1, 15):
        consulta = int(input("Consulta no válida. Ingrese un número entre 1 y 14: "))
    return consulta

def consultasSQL(usuario, contraseña, consulta):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    mycursor = mydb.cursor()
    if consulta == 1:
        mycursor.execute("SELECT R.Id_region, R.Nombre_Region, COUNT(*) AS Num_Comunas FROM Region R INNER JOIN Comuna C ON R.Id_region = C.Id_region GROUP BY R.Nombre_Region;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Num Comunas"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 2:
        mycursor.execute("SELECT Id_region, Nombre_Region, MAX(Poblacion) AS Max_Poblacion FROM Region;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Población Máxima"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 3:
        hab = int(input("Ingrese el número de habitantes: "))
        mycursor.execute("SELECT Id_Comuna, Nombre_Comuna, Poblacion FROM Comuna WHERE Poblacion > %s;", (hab,))
        resultados = mycursor.fetchall()
        headers = ["Id Comuna", "Nombre Comuna", "Población"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 4:
        mycursor.execute("SELECT R.Id_region, R.Nombre_Region, AVG(C.Superficie) AS Promedio_Superficie FROM Region R INNER JOIN Comuna C ON R.Id_region = C.Id_region GROUP BY R.Nombre_Region;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Promedio Superficie"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 5:
        mycursor.execute("SELECT R.Id_region, R.Nombre_Region, SUM(C.Poblacion) AS Poblacion_Total FROM Region R INNER JOIN Comuna C ON R.Id_region = C.Id_region GROUP BY R.Nombre_Region;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Población Total"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 6:
        mycursor.execute("SELECT R.Id_region, R.Nombre_Region, SUM(C.Superficie) AS Superficie_Total FROM Region R INNER JOIN Comuna C ON R.Id_region = C.Id_region GROUP BY R.Nombre_Region ORDER BY Superficie_Total DESC LIMIT 1;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Superficie Total"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 7:
        mycursor.execute("SELECT Nombre_est, (Latitud + Longitud) AS Longitud_Total FROM Educacion WHERE (Latitud + Longitud) = (SELECT MIN(Latitud + Longitud) FROM Educacion);")
        resultados = mycursor.fetchall()
        headers = ["Nombre Establecimiento", "Longitud Total"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 8:
        mycursor.execute("SELECT R.Id_region, R.Nombre_Region, SUM(C.Poblacion) AS Poblacion_Total FROM Region R INNER JOIN Comuna C ON R.Id_region = C.Id_region GROUP BY R.Nombre_Region ORDER BY Poblacion_Total ASC LIMIT 1;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Población Total"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 9:
        mycursor.execute("SELECT AVG(Empleados + Desempleados) AS Promedio_Poblacion FROM Trabajo;")
        resultados = mycursor.fetchall()
        headers = ["Promedio Población"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 10:
        mycursor.execute("SELECT Id_region, Nombre_Region, Poblacion FROM Region ORDER BY Poblacion DESC;")
        resultados = mycursor.fetchall()
        headers = ["Id Región", "Nombre Región", "Población"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 11:
        mycursor.execute("SELECT C.Id_Comuna, C.Nombre_Comuna, T.Desempleados FROM Trabajo T JOIN Comuna C ON T.Id_Comuna = C.Id_Comuna WHERE T.Desempleados = (SELECT MAX(Desempleados) FROM Trabajo) LIMIT 1;")
        resultados = mycursor.fetchall()
        headers = ["Id Comuna", "Nombre Comuna", "Desempleados"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 12:
        com = input("Ingrese el nombre de la comuna: ")
        mycursor.execute("SELECT E.Nombre_est FROM Educacion E JOIN Comuna C ON E.Id_Comuna = C.Id_Comuna WHERE C.Nombre_Comuna = %s;", (com,))
        resultados = mycursor.fetchall()
        headers = ["Nombre Establecimiento"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 13:
        mycursor.execute("SELECT C.Nombre_Comuna, COUNT(S.Id_Salud) AS Num_Centros_Salud FROM Comuna C LEFT JOIN Salud S ON C.Id_Comuna = S.Id_Comuna GROUP BY C.Nombre_Comuna ORDER BY Num_Centros_Salud ASC LIMIT 1;")
        resultados = mycursor.fetchall()
        headers = ["Nombre Comuna", "Num Centros Salud"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    elif consulta == 14:
        tipo = input("Ingrese el tipo de recinto de seguridad (COMISARIA, SUBCOMISARIA, TENENCIA, RETEN, ZONA, PREFECTURA): ")
        mycursor.execute("SELECT R.Nombre_Region, COUNT(S.Id_Recinto) AS Cantidad_Recintos FROM Region R JOIN Comuna C ON R.Id_region = C.Id_region JOIN Seguridad S ON C.Id_Comuna = S.Id_Comuna WHERE S.Nombre_recinto LIKE %s GROUP BY R.Nombre_Region;", ('%' + tipo + '%',))
        resultados = mycursor.fetchall()
        headers = ["Nombre Región", "Cantidad Recintos"]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))

def main():
    usuario, contraseña = accedeMariadb()
    while True:
        consulta = preguntanum()
        consultasSQL(usuario, contraseña, consulta)
        opcion = input("¿Desea realizar otra consulta? (s/n): ")
        while opcion.lower() not in ['s', 'n']:
            opcion = input("Opción inválida. Ingrese 's' para sí o 'n' para no: ")
        if opcion.lower() == 'n':
            break

main()
