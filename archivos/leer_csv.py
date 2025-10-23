import csv

with open("C:\\Users\\B09S202est\\Desktop\\archivos" + "\\sensores.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";") # Se utiliza el metodo reader
    print(lector)
    for fila in lector: # Con el for se itera sobre el objeto para leer
        print(fila)