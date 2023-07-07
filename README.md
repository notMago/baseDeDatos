#145_BaseDeDatos

Trabajo de Base de Datos con profesor Luis Veas

Dentro de la carpeta "Documento" se encuentra el informe donde se puede encontramos el diagrama entidad-relación, diagrama modelo relacional, las variables a estudiar, documentación sobre la descarga de los datos para los archivos .csv, nuestro indicador de bienestar y 14 preguntas sql con sus respectivos códigos para ver la información en la base de datos.

Dentro de la carpeta "Programas" se encuentran el programa "Script.py" que rellena la base de datos vacía. 

Dentro de la carpeta "Datos" se encuentran los archivos csv que creamos en excel para poder importarlas a nuestra base de datos.
- En el archivo Trabajo.csv encontramos información por comuna sobre la cantidad de hombres empleados y desemplados, mujeres empleadas y desempleadas, y una cantidad total entre hombres y mujeres empleados y desempleados.
- En el archivo Seguridad.csv encontramos información por comuna sobre los recintos de carabineros, indicando nombre, dirección, fono y tipo de recinto.
- En el archivo Salud.csv encontramos información por comuna sobre los establecimientos de salud, indicando el nombre del estacionamiento, dirección y si es público o privado.
- En el archivo Educacion.csv encontramos información por comuna sobre los establecimientos educacionales, indicando nombre, latitud y longitud. 
- En el archivo Region.csv encontramos informacion sobre cada una de las regiones de Chile, indicando su nombre, población y superficie. 
- En el archivo Comunas.csv encontramos información sobre cada una de las comunas de Chile, indicando su nombre, población y superficie. 

Dentro de la carpeta "sql" se encuentra el script de la creación de la base de datos llamado "script_creabase" que crea todas las tablas vacías con sus respectivas Primary Key y Foreign Key.

Luego de tener las tablas vacías, se ejecuta script.py que se encuentra en la carpeta "Programas" que rellena la base de datos con la información de los archivos .csv que se encuentran en la carpeta "Datos". Teniendo lista la base de datos con esta información cargada estamos listos para poder continuar con las preguntas sql. 
