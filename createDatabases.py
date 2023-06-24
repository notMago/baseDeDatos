#mysql -u mago -h 45.235.99.158 -p
import mysql.connector

# Establece los datos de conexión a la base de datos
mydb = mysql.connector.connect(
        host="45.235.99.158",
        user='mago',
        password='123',
        database="DB_parteB"
    )
mycursor = mydb.cursor()

# Crea la base de datos
# Create_database_query = ("CREATE DATABASE DB_parteB;")
# Crea las tablas
create_tables_query = ("CREATE TABLE Pais(Id_pais INT PRIMARY KEY,Nombre_pais char,Poblacon int,Superficie float,Continente char,idRegion int);",
                        "CREATE TABLE Region(Id_region INT PRIMARY KEY,Nombre_region char, Poblacion int, Superficie float, Fk_idPais int, FOREIGN KEY (Fk_idPais) REFERENCES Pais(Id_pais));",
                        "CREATE TABLE Comuna(Id_comuna INT PRIMARY KEY, Nombre_comuna char, Poblacion int, Superficie float, Fk_idRegion int, FOREIGN KEY(Fk_idRegion) REFERENCES Region(Id_region));",
                        "CREATE TABLE Trabajo(Empleados int, Desempleados int,mujOcup int,mujDeso int,homOcup int,homDeso int, FK_idComuna int, FOREIGN KEY(Fk_idComuna) REFERENCES Region(Id_region));",
                        "CREATE TABLE Salud(FK_idComuna int,idSalud int PRIMARY KEY, Nombre_CA char, pertenencia char, Dirección char, FOREIGN KEY (Fk_idComuna) REFERENCES Region(Id_region));",
                        "CREATE TABLE Educacion (Id_Educacion int PRIMARY KEY, Nombre_est char, Latitud float, Longitud float, FK_idComuna int, FOREIGN KEY (Fk_idComuna) REFERENCES Region(Id_region));",
                        "CREATE TABLE Seguridad(Id_Recinto int PRIMARY KEY, Nombre_recinto char, Dirección char, Fono int, FK_idComuna int, FOREIGN KEY (Fk_idComuna) REFERENCES Region(Id_region));",
                        "CREATE TABLE Tipo_est (Id_est int PRIMARY KEY, Descripción char,Fk_idEducacion int, FOREIGN KEY (Fk_idEducacion) REFERENCES Educacion(Id_Educacion));",
                        "CREATE TABLE Tipo_CA(Id_CA int PRIMARY KEY, Descripción char, Fk_idSalud int, FOREIGN KEY (Fk_idSalud) REFERENCES Salud(idSalud));",
                        "CREATE TABLE Tipo_Comisaria(Id_Comi int PRIMARY KEY, Descripción char, Fk_idRecinto int, FOREIGN KEY (Fk_idRecinto) REFERENCES Seguridad(id_Recinto));")
# Ejecuta en mariadb la sintaxis sql 
mycursor.execute(create_tables_query)
mydb.commit()
mycursor.close()