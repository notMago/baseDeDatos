import mysql.connector
import pymysql
from mysql.connector import cursor
from mysql.connector.constants import CNX_POOL_ARGS
#Este script se encuentra en github.
def accedeMariadb():
    usuario = input("Ingrese su usuario local de MariaDB: ")
    contraseña = input ("Ingrese la contraseña correspondiente a su usario de MariaDB: ")
    while True:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = usuario,
                password = contraseña
            )
            break
        except:
            print("Usuario o contraseña incorrectos, por favor, ingreselos nuevamente")
            usuario = input("Ingrese su usuario local de MariaDB: ")
            contraseña = input ("Ingrese la contraseña correspondiente a su usario de MariaDB: ")
    return usuario, contraseña

def cargaPais(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    
    with open('Pais.csv', 'r', encoding='latin-1') as file:
        next(file, None)
        for linea in file:
            linea = linea.rstrip()
            lista = linea.split(';')
            idpais = int(lista[0])
            nompais = str(lista[1])
            poblacion = int(lista[2])
            superficie = float(lista[3])
            cont = str(lista[4])
            idregion = int(lista[5]) if lista[5] != "NULL" else None
            
            mycursor = mydb.cursor()
            sql = "INSERT IGNORE INTO Pais (Id_pais, Nombre_Pais, Poblacion, Superficie, Continente, Id_region) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (idpais, nompais, poblacion, superficie, cont, idregion)
            mycursor.execute(sql, values)
    
    mydb.commit()
    print("Carga de país a la base de datos lista")


def cargaRegion(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    
    # Primero, obtén los datos de los países existentes
    paises = {}
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Id_pais FROM Pais")
    resultados = mycursor.fetchall()
    for resultado in resultados:
        paises[resultado[0]] = True

    with open('Region.csv', 'r') as file:
        next(file, None)  # Salta la primera línea que es texto que no queremos.
        for linea in file:
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            idRegion = int(lista[0])
            nomRegion = str(lista[1])
            poblacion = int(lista[2])
            superficie = float(lista[3])
            idPais = int(lista[4])

            # Verifica si el país existe en la tabla País
            if idPais in paises:
                mycursor = mydb.cursor()
                mycursor.execute("INSERT IGNORE INTO Region (Id_region, Nombre_Region, Poblacion, Superficie, Id_pais)" 
                                f"VALUES ({idRegion}, '{nomRegion}', {poblacion}, {superficie}, {idPais})")
                #print(f"idRegion: {idRegion}, Nombre: '{nomRegion}', Poblacion: {poblacion}, Superficie: {superficie}, Pais: {idPais}.")
            else:
                print(f"El país con Id_pais: {idPais} no existe en la tabla País.")
        mydb.commit()
        print("Carga de regiones a la base de datos lista")

def cargaComuna(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Comunas.csv', 'r') as file:
        next(file, None)
        for linea in file:
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            idComuna = int(lista[0])
            nombreCom = str(lista[1])
            superficie = float(lista[2])
            poblacion = int(lista[3])
            idRegion = int(lista[4])
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Comuna (Id_Comuna, Nombre_Comuna, Superficie, Poblacion, Id_region)" 
                            f"VALUES ({idComuna}, '{nombreCom}', {superficie}, {poblacion}, {idRegion})")
            #print(f"Id Comuna: {idComuna} Nombre: {nombreCom}, Superficie {superficie}, Poblacion de {poblacion}, Id Region: {idRegion}.")
        mydb.commit()
        print("Carga de comunas a la base de datos lista")

def cargaTrabajo(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Trabajo.csv', 'r') as file:
        next(file, None)
        aidi =0
        for linea in file:
            aidi+=1
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            comuna = int(lista[0])
            mujEmp = int(lista[1])
            mujDesemp = int(lista[2])
            homEmp = int(lista[3])
            homDesemp = int(lista[4])
            totalEmp = int(lista[5])
            totalDesemp = int(lista[6])
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Trabajo (Id_trabajador, Empleados, desempleados, mujEmp, mujDesemp, homEmp, homDesemp, Id_Comuna)"
                            f"VALUES ({aidi}, {totalEmp}, '{totalDesemp}', '{mujEmp}', '{mujDesemp}', '{homEmp}', {homDesemp}, {comuna})")
        mydb.commit()
        print("Carga de trabajo a la base de datos lista")

def cargaSalud(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Salud.csv', 'r', encoding='latin-1') as file:
        next(file, None)
        aidisalud = 0
        for linea in file:
            aidisalud += 1
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            idComuna = int(lista[0])
            comuna = str(lista[1])
            establec = str(lista[2])  # Escapa las comillas simples
            pertenencia = str(lista[3])
            direc = str(lista[4])  # Escapa las comillas simples
            mycursor = mydb.cursor()
            query = "INSERT IGNORE INTO Salud (Id_Salud, Nombre_CA, Direccion, Id_Comuna) VALUES (%s, %s, %s, %s)"
            values = (aidisalud, establec, direc, idComuna)
            mycursor.execute(query, values)
        mydb.commit()
        print("Carga de salud a la base de datos lista")

def cargaEducacion(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Educacion.csv', 'r') as file:
        next(file, None)
        aidi = 0
        for linea in file:
            aidi += 1
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            idcomuna = int(lista[0])
            nombreEst = lista[2].replace("'", "''")  # Escapa las comillas simples
            lat = float(lista[3].replace(',', '.'))  # Reemplaza la coma por un punto
            lon = float(lista[4].replace(',', '.'))  # Reemplaza la coma por un punto
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Educacion (Id_Educacion, Nombre_est, Latitud, Longitud, Id_Comuna) "
                    f"VALUES ({aidi}, '{nombreEst}', {lat}, {lon}, {idcomuna})")
        mydb.commit()
        print("Carga de educación a la base de datos lista")

def cargaSeguridad(usuario, contraseña): 
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Seguridad.csv', 'r', encoding='latin-1') as file:
        next(file, None)
        aidi=0
        for linea in file:
            aidi+=1
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            idComuna = int(lista[0])
            idComisaria = int(lista[1])
            nombreComi = str(lista[2])
            direc = str(lista[3])
            fono = str(lista[4])
            tipo = str(lista[5])
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Seguridad(Id_Recinto, Nombre_recinto, Direccion, Fono, Id_Comuna)"
                    f"VALUES ({idComisaria}, '{nombreComi}', '{direc}', '{fono}', {idComuna})")
    mydb.commit()
    print("Carga de seguridad a la base de datos lista")

def cargaTipo_est(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Educacion.csv', 'r') as file:
        next(file, None)
        aidi = 0
        for linea in file:
            aidi += 1
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            descrip = str(lista[5])
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Tipo_est (Id_est, Descripcion) "
                            f"VALUES ({aidi}, '{descrip}')")  # Agrega el paréntesis de cierre y las comillas simples
        mydb.commit()
        print("Carga de tipo_est a la base de datos lista")

def cargaTipo_CA(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Salud.csv', 'r', encoding='latin-1') as file:
        next(file, None)
        aidisalud = 0
        for linea in file:
            aidisalud += 1
            linea = linea.rstrip()  # Remueve el salto de línea
            lista = linea.split(';')
            pertenencia = str(lista[3])
            mycursor = mydb.cursor()
            query = "INSERT IGNORE INTO Tipo_CA(Id_CA, Descripcion) VALUES (%s, %s)"
            values = (aidisalud, pertenencia)
            mycursor.execute(query, values)
        mydb.commit()
        print("Carga de Tipo_CA a la base de datos lista")

def cargaTipo_comisaria(usuario, contraseña):
    mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=contraseña,
        database="DB_parteB"
    )
    with open('Seguridad.csv', 'r', encoding='latin-1') as file:
        next(file, None)
        aidi=0
        for linea in file:
            aidi+=1
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            idComisaria = int(lista[1])
            tipo = str(lista[5])
            mycursor = mydb.cursor()
            mycursor.execute("INSERT IGNORE INTO Tipo_Comisaria(Id_Comi, Descripcion)"
                    f"VALUES ({idComisaria}, '{tipo}')")
    mydb.commit()
    print("Carga de Tipo_comisaria a la base de datos lista")


def main():
    usuario, contraseña = accedeMariadb()
    cargaPais(usuario, contraseña)
    cargaRegion(usuario, contraseña)
    cargaComuna(usuario, contraseña)
    cargaTrabajo(usuario, contraseña)
    cargaSalud(usuario, contraseña)
    cargaEducacion(usuario, contraseña)
    cargaSeguridad(usuario, contraseña)
    cargaTipo_est(usuario, contraseña)
    cargaTipo_CA(usuario, contraseña)
    cargaTipo_comisaria(usuario, contraseña)
main()