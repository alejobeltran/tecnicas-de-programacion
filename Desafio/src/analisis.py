#se importa el archivo carga de datos y se usa src para indicar que viene de la carpeta src en caso de ser llamado de otro archivo externo
from src.carga_datos import cargar_datos
import pandas as pd

#funcion encargada de devolver un dataframe para su uso en las graficas
def data_frame():
    df = cargar_datos()
    return df

#funcion que se encarga de generar el promedio de edad desde el dataframe
def promedio():
    #se cargan los datos desde cargar_datos()
    df = cargar_datos()
    #se usa .mean que toma toda la columna de edad para generar su promedio
    media = df["Edad"].mean()
    #se retorna el resultado
    return media

#funcion encargada de generar la desviacion
def desviacion():
    #se cargan los datos desde cargar_datos()
    df = cargar_datos()
    #se usa std para encontrar la desviacion de la columna edad del dataframe y se retorna
    desv = df["Edad"].std()
    return desv

#funcion encargada de extraer todos los municipios en el documento
def zona_geografica():
    df = cargar_datos()
    #extrae todos los valores del dataframe especificamente de la columna "nombre municipio"
    #de esta columna cuenta cuantos municipios hay y retorna municipio y cantidad de veces que se repite
    municipio = df["Nombre municipio"].value_counts().to_dict()
    #se retorna en forma de diccionario
    return municipio

#funcion encargada de generar las zonas geograficas con casos mayor al promedio
def mayor_promedio():
    #se toman todas las zonas geograficas de la anterior funcion
    diccionario = zona_geografica()
    #se establece una lista vacia para calcular el promedio
    cantidad = []
    #se extrae los valores de la zona geografica para encontrar el promedio
    for indice,valor in diccionario.items():
        cantidad.append(valor)
    promedio = sum(cantidad)/len(cantidad)
    #se crea un diccionario vacio para luego guardar los nuevos valores mayor al promedio
    municipios = {}
    for indice,valor in diccionario.items():
        if valor > promedio:
            municipios[indice] = valor
    #se retorna promedio y municipios en una lista
    return [promedio,municipios]

#funcion encargada de buscar la fecha de recuperacion y cuantas personas fallecidas hay
def recuperacion():
    #se carga el dataframe
    df = cargar_datos()
    #se convierte toda la columna de fechas que se encuentran en formato string a datetime
    df["Fecha de recuperación"] = pd.to_datetime(df["Fecha de recuperación"],errors="coerce")
    #se extraen los casos del 2020
    recuperados_2020 = df[df["Fecha de recuperación"].dt.year == 2020]
    #se extraen los casos del 2021
    recuperados_2021 = df[df["Fecha de recuperación"].dt.year == 2021]
    #las personas fallecidas al no contar con una fecha de recuperacion valida, esta se convierte en un valor null
    #por lo tanto contamos cuantos valores null hay, para asi saber la cantidad de personas fallecidas
    fallecidos = df[df["Fecha de recuperación"].isna()]
    #se retorna una lista con todas las variables
    return [recuperados_2020,recuperados_2021,fallecidos]
