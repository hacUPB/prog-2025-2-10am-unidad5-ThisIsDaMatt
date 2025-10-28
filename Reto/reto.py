import csv, os
import matplotlib.pyplot as plt

while True:
    print("=================================================")
    print("Bienvenido al procesador de archivos")
    print("=================================================")
    print("Elija una opción:")
    print("=================================================")
    print("A. Listar archivos en la ruta o ingresar una ruta")
    print("B. Procesar archivo .txt")
    print("C. Procesar archivo .csv")
    print("Q. Salir")
    print("=================================================")

    caso = input("Ingrese su selección: ")
    caso = caso.upper()

    match caso:
        case "A":
            print("===============================")
            print("Ha seleccionado listar archivos")
            print("===============================")
            print("Elija una opción:")
            print("===============================")
            print("1. Buscar en la carpeta actual")
            print("2. Ingresar ruta para buscar")
            print("===============================")

            opcion_a = input("Ingrese su selección: ")
            opcion_a = opcion_a.upper()

            if opcion_a == "1":
                ruta = "."
            else:
                ruta = input("Ingrese la ruta: ")
            
            try:
                archivos = os.listdir(ruta)
                
                txt = []
                csv = []

                for archivo in archivos:
                    if archivo.endswith(".txt"):
                        txt.append(archivo)
                    elif archivo.endswith(".csv"):
                        csv.append(archivo)
                
                print("===============================")
                print("Archivos .txt encontrados:")
                print("===============================")
                if txt:
                    for i, f in enumerate(txt, 1):
                        print(f"{i}. {f}")
                else:
                    print("No se encontraron archivos .txt")
                print("===============================")
                print("Archivos .csv encontrados:")
                print("===============================")
                if csv:
                    for i, f in enumerate(csv, 1):
                        print(f"{i}. {f}")
                else:
                    print("No se encontraron archivos .csv")

            except:
                print("No hay archivos .csv")

        case "B":
            print("================================================")
            print("Ha seleccionado procesar .txt")
            print("================================================")
            print("Elija una opción:")
            print("================================================")
            print("1. Contar palabras y caracteres")
            print("2. Reemplazar palabras")
            print("3. Generar histograma de ocurrencias de vocales")
            print("================================================")

            opcion_b = input("Ingrese su selección: ")
            opcion_b = opcion_b.upper()

            match opcion_b:
                case "1":
                    print("========================")
                    print("Palabras y caracteres")
                    print("========================")
                    print("Contenido de la carpeta:")
                    print("========================")
                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)
                    
                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        
                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()

                        print("========================================")
                        print(f"Archivo: {archivo}")
                        print("========================================")
                        print(f"# de Caracteres: {len(contenido)}")
                        print(f"# de Caracteres sin Espacios: {len(contenido.replace(" ",""))}")
                        print(f"# de Palabras: {len(contenido.split())}")
                        print("========================================")

                case "2":
                    print("===================")
                    print("Reemplazar palabras")
                    print("===================")

                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)

                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()

                        print("===================")
                        print("Contenido original: ")
                        print("===================")
                        print(contenido)
                        print("===================")

                        reemplazada = input("Ingrese la palabra que desea reemplazar: ")
                        nueva = input("Ingrese la palabra nueva: ")

                        nuevo_contenido = contenido.replace(reemplazada, nueva)

                        print("========================")
                        print("Archivo .txt modificado:")
                        print("========================")
                        print(nuevo_contenido)
                        print("========================")

                        guardar = input("Desea guardar este nuevo contenido? S/N: ")
                        guardar = guardar.upper()

                        if guardar == "S":
                            with open(archivo, "w", encoding="utf-8") as f:
                                f.write(nuevo_contenido)
                            print("El archivo se ha guardado, revisa los cambios.")
                        else:
                            print("Cambios no guardados.")
                
                case "3":
                    print("====================================")
                    print("Histograma de ocurrencias de vocales")
                    print("====================================")
                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)
                    
                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()
                        
                        contenido_low = contenido.lower()
                        
                        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                        
                        for letra in contenido_low:
                            if letra in vocales:
                                vocales[letra] += 1
                        
                        print("==============================================")
                        print(f"Histograma de vocales - Archivo: {archivo}")
                        print("==============================================")
                        print("Generando grafico con MatPlotLib...")        
                        print("==============================================")
                        print(f"Total de vocales: {sum(vocales.values())}")
                        print("==============================================")

                        vocales_list = list(vocales.keys())
                        cantidades = list(vocales.values())
                        
                        plt.figure(figsize=(10, 6))
                        plt.bar(vocales_list, cantidades, color='skyblue', edgecolor='black', width=0.6)
                        plt.xlabel('Vocales', fontsize=12)
                        plt.ylabel('Cantidad de Ocurrencias', fontsize=12)
                        plt.title(f'Histograma de Vocales - {archivo}', fontsize=14, fontweight='bold')
                        plt.grid(axis='y', alpha=0.3, linestyle='--')
                        
                        for i, v in enumerate(cantidades):
                            plt.text(i, v + max(cantidades) * 0.02, str(v), ha='center', fontweight='bold')
                        
                        plt.tight_layout()
                        plt.show()
        case "C":
            print("======================================")
            print("Ha seleccionado procesar .csv")
            print("======================================")
            print("Elija una opción:")
            print("======================================")
            print("1. Mostrar 15 primeras filas")
            print("2. Calcular estadísticas")
            print("3. Graficar columna completa con datos")
            print("======================================")

            opcion_c = input("Ingrese su selección: ")
            opcion_c = opcion_c.upper()

            match opcion_c:
                case "1":
                    print("=========================")
                    print("Mostrar 15 primeras filas")
                    print("=========================")
                    archivos = os.listdir(".")
                    archivos_csv = []

                    for f in archivos:
                        if f.endswith(".csv"):
                            archivos_csv.append(f)

                    if not archivos_csv:
                        print("No se encontraron archivos .csv")
                    else:
                        for i, f in enumerate(archivos_csv, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_csv[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            lector = csv.reader(f)

                            print("=============================")
                            print("Primeras 15 filas del archivo")
                            print("=============================")

                            for i, fila in enumerate(lector):
                                if i < 15:
                                    print(f"Fila {i+1}: {fila}")
                                else:
                                    break
                                
                            print("=============================")
                
                case "2":
                    print("=================================")
                    print("Calcular estadisticas del archivo")
                    print("=================================")
                    archivos = os.listdir(".")
                    archivos_csv = []

                    for f in archivos:
                        if f.endswith(".csv"):
                            archivos_csv.append(f)

                    if not archivos_csv:
                        print("No se encontraron archivos .csv")
                    else:
                        for i, f in enumerate(archivos_csv, 1):
                            print(f"{i}. {f}")
                        
                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_csv[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            lector = csv.reader(f)

                            

        case "Q":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción incorrecta, ingrese una opción de nuevo.")
