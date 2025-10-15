#se importa la libreria de pandas para cargar el excel en un dataframe y la libreria de os para encontrar el path donde se encuentra guardado el excel
import pandas as pd
import os
#funcion encargada de cargar el excel y convertirlo en dataframe
def cargar_datos():
    #se usa la libreria os para encontrar la direccion base
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #usando la direccion base, se busca la carpeta data donde se encuentra el excel
    data = os.path.join(base,"data")
    #se busca en esa carpeta el nombre del excel
    data = os.path.join(data,"covid_colombia_100.xlsx")
    #teniendo la direccion completa en data, se carga el archivo en pandas convirtiendolo en dataframe y se retorna el dataframe
    df = pd.read_excel(data,engine="openpyxl")
    return df