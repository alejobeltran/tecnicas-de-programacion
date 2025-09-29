from src.carga_datos import cargar_datos
import pandas as pd

def promedio():
    df = cargar_datos()
    media = df["Edad"].mean()
    return media

def desviacion():
    df = cargar_datos()
    desv = df["Edad"].std()
    return desv

print(promedio())
print(desviacion())