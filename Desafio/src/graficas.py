import matplotlib.pyplot as plt
import pandas as pd
from src.carga_datos import cargar_datos

def histograma():
    df = cargar_datos()    
    df = pd.to_numeric(df["Edad"], errors="coerce")
    plt.figure(figsize=(8, 5))
    plt.hist(df, bins=20, color="skyblue", edgecolor="black")

    plt.title("Distribución de edades de personas contagiadas de COVID-19 en Colombia")
    plt.xlabel("Edad")
    plt.ylabel("Número de casos")
    plt.grid(axis="y", alpha=0.3)

    plt.show()

def barras():
    df = cargar_datos()
    conteo_sexo = df["Sexo"].value_counts()
    
    plt.figure(figsize=(10, 5))
    conteo_sexo.plot(kind="bar", color=["royalblue", "lightcoral"], edgecolor="black")
    plt.title("Cantidad de casos por sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Número de casos")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    conteo_municipio = df["Nombre municipio"].value_counts().head(10)  

    plt.figure(figsize=(10, 6))
    conteo_municipio.plot(kind="bar", color="mediumseagreen", edgecolor="black")
    plt.title("Top 10 municipios con más casos de COVID-19")
    plt.xlabel("Municipio")
    plt.ylabel("Número de casos")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

def dispersion():
    df = cargar_datos()

    df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
    df["Fecha de diagnóstico"] = pd.to_datetime(df["Fecha de diagnóstico"], errors="coerce")
    df = df.dropna(subset=["Edad", "Fecha de diagnóstico"])

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Fecha de diagnóstico"], df["Edad"], alpha=0.5, color="mediumseagreen", edgecolors="black", linewidths=0.5)

    plt.title("Dispersión entre la edad y la fecha de diagnóstico")
    plt.xlabel("Fecha de diagnóstico")
    plt.ylabel("Edad")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()