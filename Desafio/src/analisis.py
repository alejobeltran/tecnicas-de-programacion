from src.carga_datos import cargar_datos
import pandas as pd

def data_frame():
    df = cargar_datos()
    return df

def promedio():
    df = cargar_datos()
    media = df["Edad"].mean()
    return media

def desviacion():
    df = cargar_datos()
    desv = df["Edad"].std()
    return desv

def zona_geografica():
    df = cargar_datos()
    municipio = df["Nombre municipio"].value_counts().to_dict()
    return municipio

def mayor_promedio():
    diccionario = zona_geografica()
    cantidad = []
    for indice,valor in diccionario.items():
        cantidad.append(valor)
    promedio = sum(cantidad)/len(cantidad)
    municipios = {}
    for indice,valor in diccionario.items():
        if valor > promedio:
            municipios[indice] = valor
    return [promedio,municipios]
    
