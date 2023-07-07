CREATE DATABASE if NOT EXISTS DB_parteB;

USE DB_parteB;
--Creacion de tablas solo con claves primarias
CREATE TABLE if NOT EXISTS Pais(Id_pais INT PRIMARY KEY, Nombre_Pais VARCHAR(50), Poblacion INT, Superficie FLOAT, Continente VARCHAR(50), Id_region INT);

CREATE TABLE if NOT EXISTS Region(Id_region INT PRIMARY KEY, Nombre_Region VARCHAR(50), Poblacion INT, Superficie FLOAT, Id_pais INT);

CREATE TABLE if NOT EXISTS Comuna(Id_Comuna INT PRIMARY KEY, Nombre_Comuna VARCHAR(50), Superficie FLOAT, Poblacion INT, Id_region INT);

CREATE TABLE if NOT EXISTS Educacion(Id_Educacion INT PRIMARY KEY, Nombre_est VARCHAR(50), Latitud FLOAT, Longitud FLOAT, Id_est INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Salud(Id_Salud INT PRIMARY KEY, Nombre_CA VARCHAR(200), Direccion VARCHAR(100), Id_CA INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Trabajo(Id_trabajador INT PRIMARY KEY, Empleados INT, Desempleados INT, mujEmp INT, mujDesemp INT, homEmp INT, homDesemp INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Seguridad(Id_Recinto INT PRIMARY KEY, Nombre_recinto VARCHAR(50), Direccion VARCHAR(200), Fono BIGINT, Id_Comi INT,Id_Comuna INT);

CREATE TABLE if NOT EXISTS Tipo_est(Id_est INT PRIMARY KEY, Descripcion VARCHAR (50), Id_Educacion INT);

CREATE TABLE if NOT EXISTS Tipo_CA(Id_CA INT PRIMARY KEY, Descripcion VARCHAR(50), Id_Salud INT);

CREATE TABLE if NOT EXISTS Tipo_Comisaria(Id_Comi INT PRIMARY KEY, Descripcion VARCHAR(50), Id_Recinto INT);

--ADICIoN DE CLAVES FORaNEAS
ALTER TABLE Pais ADD CONSTRAINT fk_Pais_Region FOREIGN KEY (Id_region) REFERENCES Region (Id_region);

ALTER TABLE Region
ADD CONSTRAINT fk_Region_Pais FOREIGN KEY (Id_pais) REFERENCES Pais (Id_pais);

ALTER TABLE Comuna
ADD CONSTRAINT fk_Comuna_Region FOREIGN KEY (Id_region) REFERENCES Region (Id_region);

ALTER TABLE Educacion ADD CONSTRAINT fk_Educacion_Tipo_est FOREIGN KEY (Id_est) REFERENCES Tipo_est (Id_est), 
ADD CONSTRAINT fk_Educacion_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Salud ADD CONSTRAINT fk_Salud_Tipo_CA FOREIGN KEY (Id_CA) REFERENCES Tipo_CA (Id_CA), 
ADD CONSTRAINT fk_Salud_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Trabajo ADD CONSTRAINT fk_Trabajo_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Seguridad ADD CONSTRAINT fk_seguridad_Tipo_Comisaria FOREIGN KEY (Id_Comi) REFERENCES Tipo_Comisaria (Id_Comi), 
ADD CONSTRAINT fk_Seguridad_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Tipo_est ADD CONSTRAINT fk_Tipo_est_Educacion FOREIGN KEY (Id_Educacion) REFERENCES Educacion (Id_Educacion);

ALTER TABLE Tipo_CA ADD CONSTRAINT fk_Tipo_CA_Salud FOREIGN KEY (Id_Salud) REFERENCES Salud (Id_Salud);

ALTER TABLE Tipo_Comisaria ADD CONSTRAINT fk_Tipo_Comisaria_Seguridad FOREIGN KEY (Id_Recinto) REFERENCES Seguridad (Id_Recinto);
