import csv

test = ["Hola", 33, "Fernando Alonso"]
a = ["A", 1, "a"]
prices = ["$2000", "$3000", "$0.00001"]

with open("C:\\Users\\B09S202est\\Desktop\\archivos" + "\\salida.csv", "w", newline="") as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(["Nombre", "Edad", "Ciudad"]) # Fila de encabezados
    escritor.writerow(["John", 25, "Nueva York"])
    escritor.writerow(test)
    escritor.writerow(a)
    escritor.writerow(prices)