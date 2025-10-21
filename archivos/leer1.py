# 1. Abrir el archivo y definir el modo
archivo = open("texto.txt", "r")
# 2. Leer el archivo
datos = archivo.readlines()
print(datos)
# 3. Cerrar el archivo
archivo.close()