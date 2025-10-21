ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos" # \ se usa para comandos de texto
nombre_archivo = "frutas.txt"
modo = "w" # Solo escritura - sobreescribe
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8") # C:\Users\B09S202est\Desktop\archivos\frutas.txt

fp.close()