lista = ["Starchild", "Scam", "Love Foolosophy", "Runaway", "Cosmic Girl"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
modo = "w"
# \ se usa para comandos de texto
nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="utf-8")
for cancion in lista:
    fp.write(cancion+"\n")
fp.close()