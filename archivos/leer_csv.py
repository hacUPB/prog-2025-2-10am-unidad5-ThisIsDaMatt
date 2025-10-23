import csv

with open("C:\\Users\\B09S202est\\Desktop\\archivos" + "\\sensores.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";") # Se utiliza el metodo reader
    encabezado = next(lector) # 
    # print(encabezado)
    presion = []
    print(encabezado[0])
    for fila in lector: # Con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace(",", ".")
        dato = float(fila[3])
        presion.append(dato)

print(presion)