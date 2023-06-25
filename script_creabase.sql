CREATE DATABASE if NOT EXISTS DB_parteB;

USE DB_parteB;
--Creación de tablas sólo con claves primarias
CREATE TABLE if NOT EXISTS País(Id_pais INT PRIMARY KEY, Nombre_Pais VARCHAR(50), Población INT, Superficie FLOAT, Continente VARCHAR(50), Id_región INT);

CREATE TABLE if NOT EXISTS Región(Id_region INT PRIMARY KEY, Nombre_Región VARCHAR(50), Poblacion INT, Superficie FLOAT, Id_pais INT);

CREATE TABLE if NOT EXISTS Comuna(Id_Comuna INT PRIMARY KEY, Nombre_Comuna VARCHAR(50), Superficie FLOAT, Población INT, Id_región INT);

CREATE TABLE if NOT EXISTS Educación(Id_Educación INT PRIMARY KEY, Nombre_est VARCHAR(50), Latitud FLOAT, Longitud FLOAT, Id_est INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Salud(Id_Salud INT PRIMARY KEY, Nombre_CA VARCHAR(200), Dirección VARCHAR(100), Id_CA INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Trabajo(Id_trabajador INT PRIMARY KEY, Empleados INT, Desempleados INT, mujEmp INT, mujDesemp INT, homEmp INT, homDesemp INT, Id_Comuna INT);

CREATE TABLE if NOT EXISTS Seguridad(Id_Recinto INT PRIMARY KEY, Nombre_recinto VARCHAR(50), Dirección VARCHAR(200), Fono BIGINT, Id_Comi INT,Id_Comuna INT);

CREATE TABLE if NOT EXISTS Tipo_est(Id_est INT PRIMARY KEY, Descripción VARCHAR (50), Id_Educación INT);

CREATE TABLE if NOT EXISTS Tipo_CA(Id_CA INT PRIMARY KEY, Descripción VARCHAR(50), Id_Salud INT);

CREATE TABLE if NOT EXISTS Género(Id_gen INT PRIMARY KEY, Descripción VARCHAR(50));

CREATE TABLE if NOT EXISTS Tipo_Comisaria(Id_Comi INT PRIMARY KEY, Descripción VARCHAR(50), Id_Recinto INT);

--ADICIÓN DE CLAVES FORÁNEAS
ALTER TABLE País ADD CONSTRAINT fk_Pais_Región FOREIGN KEY (Id_región) REFERENCES Región (Id_región);

ALTER TABLE Región
ADD CONSTRAINT fk_Región_País FOREIGN KEY (Id_pais) REFERENCES País (Id_pais);

ALTER TABLE Comuna
ADD CONSTRAINT fk_Comuna_Región FOREIGN KEY (Id_región) REFERENCES Región (Id_región);

ALTER TABLE Educación ADD CONSTRAINT fk_Educación_Tipo_est FOREIGN KEY (Id_est) REFERENCES Tipo_est (Id_est), 
ADD CONSTRAINT fk_Educación_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Salud ADD CONSTRAINT fk_Salud_Tipo_CA FOREIGN KEY (Id_CA) REFERENCES Tipo_CA (Id_CA), 
ADD CONSTRAINT fk_Salud_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Trabajo ADD CONSTRAINT fk_Trabajo_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Seguridad ADD CONSTRAINT fk_seguridad_Tipo_Comisaria FOREIGN KEY (Id_Comi) REFERENCES Tipo_Comisaria (Id_Comi), 
ADD CONSTRAINT fk_Seguridad_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

ALTER TABLE Tipo_est ADD CONSTRAINT fk_Tipo_est_Educación FOREIGN KEY (Id_Educación) REFERENCES Educación (Id_Educación);

ALTER TABLE Tipo_CA ADD CONSTRAINT fk_Tipo_CA_Salud FOREIGN KEY (Id_Salud) REFERENCES Salud (Id_Salud);

ALTER TABLE Tipo_Comisaria ADD CONSTRAINT fk_Tipo_Comisaria_Seguridad FOREIGN KEY (Id_Recinto) REFERENCES Seguridad (Id_Recinto);
