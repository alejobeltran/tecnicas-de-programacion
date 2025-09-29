#se importa la libreria de pandas para cargar el excel en un dataframe y la libreria de os para encontrar el path donde se encuentra guardado el excel
import pandas as pd
import os
#funcion encargada de cargar el excel y convertirlo en dataframe
def cargar_datos():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data = os.path.join(base,"data")
    data = os.path.join(data,"covid_colombia_100.xlsx")
    df = pd.read_excel(data,engine="openpyxl")
    return df