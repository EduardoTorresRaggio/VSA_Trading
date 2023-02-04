import csv
import requests

import requests
import pandas as pd

def ObtenerDatosLink():

    url = "https://es.investing.com/dbc56af4-aa50-48a5-8fea-8b6f31d2735b"
    response = requests.get(url)

    if response.status_code == 200:
        df = pd.DataFrame(response)
        df.to_csv('NASDAQ.csv', index=False)
        print("La respuesta se guardó exitosamente en formato CSV.")
    else:
        print("La solicitud GET falló con código de estado:", response.status_code)

def UsarArchivoCSV():
    #leer el archivo
    with open('Datos_historicos_Nasdaq100.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
    #guardar archivo formato pandas
    df = pd.read_csv("Datos_historicos_Nasdaq100.csv")
    df
UsarArchivoCSV()