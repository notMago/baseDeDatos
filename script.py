#Este script se encuentra en github.
def cargaRegion():
    with open('Region.csv', 'r') as file:
        next(file, None) #salta la primera linea que es texto que no queremos.
        for linea in file:
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            idRegion = int(lista[0])
            nomRegion = str(lista[1])
            poblacion = int(lista[2])
            super = float(lista[3])
            idPais = int(lista[4])
            print(f"idRegion: {idRegion}, Nombre: {nomRegion}, Poblacion {poblacion}, Superficie: {super}, Pais: {idPais}.")
        
def cargaComuna():
    with open('Comunas.csv', 'r') as file:
        next(file, None)
        for linea in file:
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            idComuna = int(lista[0])
            nombreCom = str(lista[1])
            super = float(lista[2])
            poblacion = int(lista[3])
            idRegion = int(lista[4])
            print(f"Id Comuna: {idComuna} Nombre: {nombreCom}, Superficie {super}, Poblacion de {poblacion}, Id Region: {idRegion}.")

def cargaTrabajo():
    with open('Trabajo.csv', 'r') as file:
        next(file, None)
        for linea in file:
            linea = linea.rstrip()#Remueve el salto de linea
            lista = linea.split(';')
            comuna = int(lista[0])
            mujOcup = int(lista[1])
            mujDeso = int(lista[2])
            homOcup = int(lista[3])
            homDeso = int(lista[4])
            totalEmp = int(lista[5])
            totalDesemp=int(lista[6])
            print(f"Comuna: {comuna} con {mujOcup} mujeres ocupadas, {mujDeso} mujeres desocupadas {homOcup} hombres ocupados y {homDeso} hombres desocupados. Un total de {totalEmp} personas empleadas y {totalDesemp} personas desempleadas")

def cargaSalud():
    print('Test.')

def main():
    cargaRegion()
    cargaComuna()
    cargaTrabajo()

main()