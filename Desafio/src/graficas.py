#se importan las librerias
import matplotlib.pyplot as plt
import pandas as pd
from src.carga_datos import cargar_datos

#funcion encargada de generar un histograma con los datos de edad
def histograma():
    #se carga el dataframe y se convierte la columna edad a numeros
    df = cargar_datos()    
    df = pd.to_numeric(df["Edad"], errors="coerce")

    #se usa matplotlib para empezar a generar el grafico
    plt.figure(figsize=(8, 5))
    plt.hist(df, bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribución de edades de personas contagiadas de COVID-19 en Colombia")
    plt.xlabel("Edad")
    plt.ylabel("Número de casos")
    plt.grid(axis="y", alpha=0.3)
    plt.show()

#funcion encargada de enseñar 2 graficos de barras, para el sexo y la cantidad de municipios
def barras():
    #se carga el dataframe
    df = cargar_datos()
    #se carga la columna de sexo, y se cuenta, en este caso F,M
    conteo_sexo = df["Sexo"].value_counts()
    #con estos datos se crea la tabla
    plt.figure(figsize=(10, 5))
    conteo_sexo.plot(kind="bar", color=["royalblue", "lightcoral"], edgecolor="black")
    plt.title("Cantidad de casos por sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Número de casos")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    #se realiza lo mismo de antes pero con la columna de los municipios
    conteo_municipio = df["Nombre municipio"].value_counts().head(10)  
    #y se produce la segunda grafica con estos datos
    plt.figure(figsize=(10, 6))
    conteo_municipio.plot(kind="bar", color="mediumseagreen", edgecolor="black")
    plt.title("Top 10 municipios con más casos de COVID-19")
    plt.xlabel("Municipio")
    plt.ylabel("Número de casos")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

#funcion encargada de crear el grafico de dispersion
def dispersion():
    #se cargan los datos
    df = cargar_datos()
    #se carga la columna edad y se pasa a numeros
    df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
    #tomamos las fechas de diagnostico y las pasamos de string a datetime
    df["Fecha de diagnóstico"] = pd.to_datetime(df["Fecha de diagnóstico"], errors="coerce")
    #eliminamos los valores nulos
    df = df.dropna(subset=["Edad", "Fecha de diagnóstico"])
    #se crea el grafico de dispersion con estos datos
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Fecha de diagnóstico"], df["Edad"], alpha=0.5, color="mediumseagreen", edgecolors="black", linewidths=0.5)

    plt.title("Dispersión entre la edad y la fecha de diagnóstico")
    plt.xlabel("Fecha de diagnóstico")
    plt.ylabel("Edad")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()