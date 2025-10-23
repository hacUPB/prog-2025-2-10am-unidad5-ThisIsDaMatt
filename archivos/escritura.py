ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos" # \ se usa para comandos de texto
nombre_archivo = "frutas.txt"
modo = "x" # Solo escritura - sobreescribe
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8") # C:\Users\B09S202est\Desktop\archivos\frutas.txt
frase = input("Por favor ingresa una frase: ")
fp.write(frase + "\n")
# Solicitar una variable entera y una float al usuario y la escribe en el archivo
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
# La escribimos en el archivo
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura))

fp.close()