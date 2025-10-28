nombre_archivo = "canciones.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
with open(ubicacion + "\\" + nombre_archivo, "r", encoding="utf-8") as archivo:
    # Leer todas las lineas dentro de una lista
    lista = archivo.readlines()

# Se imprime la lista elemento por elemento
for c in lista:
    print(c)