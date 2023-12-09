import csv
from collections import Counter
from datetime import datetime
import time

def leer_archivo_csv(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Leer la primera fila como encabezados
        datos = [fila for fila in lector_csv]
    return encabezados, datos

def parsear_fecha_hora(fecha_hora_str):
    # Formato de fecha y hora: "2023-04-24 10:30:10"
    formato = "%Y-%m-%d %H:%M:%S"
    return datetime.strptime(fecha_hora_str, formato)

def estaciones_mas_calientes(datos, hora_inicio, hora_fin):
    estaciones_origen = [fila[4] for fila in datos if hora_inicio <= parsear_fecha_hora(fila[3]).time() <= hora_fin]
    contador_estaciones = Counter(estaciones_origen)
    estaciones_calientes = contador_estaciones.most_common(3)
    return estaciones_calientes

# Ruta del archivo CSV 
ruta_archivo = 'datos_2023.csv'

# Definir el rango de horas para la mañana (de 6 a 11:59)
hora_inicio = datetime.strptime('06:00:00', '%H:%M:%S').time()
hora_fin = datetime.strptime('11:59:59', '%H:%M:%S').time()

# Leer el archivo CSV
encabezados, datos = leer_archivo_csv(ruta_archivo)

# Imprimir mensaje de procesamiento
print("Procesando el archivo... Esto puede tomar un momento.")

# Simular un proceso con un gif o indicador de carga (puedes ajustar según tus necesidades)
for _ in range(10):
    time.sleep(0.1)
    print(".", end="", flush=True)  # La función flush=True permite imprimir en la misma línea

# Encontrar las tres estaciones de origen más "calientes" en el rango de horas
estaciones_calientes = estaciones_mas_calientes(datos, hora_inicio, hora_fin)

# Imprimir los resultados
print("\nLas tres estaciones de origen más 'calientes' en la mañana son:")
for estacion, cantidad in estaciones_calientes:
    print(f"Estación {estacion}: {cantidad} recorridos")
