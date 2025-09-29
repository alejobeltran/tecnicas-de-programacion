import pandas as pd

# Cargar el dataset grande
df = pd.read_excel(r"C:\Users\equipo\code\universidad\tecnicas de programacion\Desafio\data\Casos_positivos_covid.xlsx",engine="openpyxl")

# Quedarse solo con 100 filas
df_100 = df.head(101)

# Guardar en un nuevo archivo
df_100.to_excel(r"C:\Users\equipo\code\universidad\tecnicas de programacion\Desafio\data\covid_colombia_100.xlsx", index=False,engine="openpyxl")

print("Archivo reducido a 100 filas guardado con éxito.")
