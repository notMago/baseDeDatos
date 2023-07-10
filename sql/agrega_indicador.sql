USE DB_parteB;

CREATE TABLE if NOT EXISTS Indicador_Bienestar(Id_Indicador INT PRIMARY KEY, Cant_CA INT, Cant_est INT, Cant_recintos INT, Cant_emp INT, ind_Salud INT, ind_Educacion INT, ind_Seguridad INT, ind_Trabajo INT, total_indicador INT, indicador VARCHAR(50), Id_Comuna INT);

ALTER TABLE Indicador_Bienestar ADD CONSTRAINT fk_Indicador_Comuna FOREIGN KEY (Id_Comuna) REFERENCES Comuna (Id_Comuna);

