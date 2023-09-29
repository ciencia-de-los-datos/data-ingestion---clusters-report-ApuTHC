"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    
    dict_df = {
        "cluster": [],
        "cantidad_de_palabras_clave": [],
        "porcentaje_de_palabras_clave": [],
        "principales_palabras_clave": [],
    }

    aux_row = ""
    
    with open('clusters_report.txt', 'r') as archivo:
        for index, linea in enumerate(archivo):
            if index >= 4:
                # print(linea.strip())
                if linea.strip() == "":
                    columnas = re.sub(r'\s+', ' ', aux_row.strip())
                    columnas = re.sub(r'\.', '', columnas)
                    cols = columnas.split(" % ")
                    col = cols[0].split(" ")
                    dict_df["cluster"] += [int(col[0])]
                    dict_df["cantidad_de_palabras_clave"] += [int(col[1])]
                    dict_df["porcentaje_de_palabras_clave"] += [float(col[2].replace(",", "."))]
                    dict_df["principales_palabras_clave"] += [cols[1]]
                    aux_row = ""
                else:
                    aux_row += " " + linea.strip()
    df = pd.DataFrame(dict_df)
    return df