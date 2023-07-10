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

def llenaIndicador(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB" #la primera es 5602 y 4, la ultima 5405 y 2
    )
    mycursor = mydb.cursor() 
    mycursor.execute("SELECT C.Id_Comuna, COUNT(DISTINCT S.Id_Salud) AS Cantidad_Centros_Salud, COUNT(DISTINCT E.Id_Educacion) AS Cantidad_Establecimientos_Educacionales, COUNT(DISTINCT SE.Id_Recinto) AS Cantidad_Centros_Seguridad, T.Empleados AS Cantidad_Empleados FROM Comuna C LEFT JOIN Salud S ON C.Id_Comuna = S.Id_Comuna LEFT JOIN Educacion E ON C.Id_Comuna = E.Id_Comuna LEFT JOIN Seguridad SE ON C.Id_Comuna = SE.Id_Comuna LEFT JOIN Trabajo T ON C.Id_Comuna = T.Id_Comuna GROUP BY C.Id_Comuna;")
    resultados = mycursor.fetchall()
    ind_Salud=0
    ind_Educacion=0
    ind_Seguridad=0
    ind_Trabajo=0
    totalind=0
    indicador=''
    for resultado in resultados:
        sql = "INSERT IGNORE INTO Indicador_Bienestar (Id_Indicador, Cant_CA, Cant_est, Cant_recintos, Cant_emp, ind_Salud, ind_Educacion, ind_Seguridad, ind_Trabajo, total_indicador, indicador, Id_Comuna) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if (resultado[1] in range(0, 26)):
            ind_Salud = 1
        if (resultado[1] in range (27, 53)):
            ind_Salud = 2
        if (resultado[1] in range (54, 80)):
            ind_Salud = 3

        if (resultado[2] in range(1, 104)):
            ind_Educacion = 1
        if (resultado[2] in range (105, 209)): 
            ind_Educacion = 2
        if (resultado[2] in range (210, 313)):
            ind_Educacion = 3

        if (resultado[3] in range(0, 5)):
            ind_Seguridad = 1
        if (resultado[3] in range (6, 11)):
            ind_Seguridad = 2
        if (resultado[3] in range (12, 16)):
            ind_Seguridad = 3

        if (resultado[4] in range (207, 89413)): 
            ind_Trabajo = 1
        if (resultado[4] in range (89414, 178619)):
            ind_Trabajo = 2
        if (resultado[4] in range (178620, 267827)):
            ind_Trabajo = 3
        totalind = ind_Salud + ind_Educacion + ind_Seguridad + ind_Trabajo
        if (totalind <= 4):
            indicador = 'malo'
        if (totalind >= 5 and totalind <=8): 
            indicador = 'medio'
        if (totalind >=9 and totalind <=12):
            indicador ='bueno'
        values = (resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], ind_Salud, ind_Educacion, ind_Seguridad, ind_Trabajo, totalind, indicador, resultado[0])
        mycursor.execute(sql, values)
        mydb.commit()
        
def main():
    usuario, contraseña = accedeMariadb()
    llenaIndicador(usuario, contraseña)
main()