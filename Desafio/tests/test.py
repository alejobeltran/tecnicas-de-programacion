import pandas as pd
import os
# Cargar el dataset grande
print("Directorio actual:", os.getcwd())
print("Archivos en este directorio:", os.listdir())
df = pd.read_csv("Accidentes_Viales_20251007.csv")

# Quedarse solo con 100 filas
df_100 = df.head(101)

# Guardar en un nuevo archivo
df_100.to_excel("Accidentes_Viales_20251007.csv", index=False,engine="openpyxl")

print("Archivo reducido a 100 filas guardado con éxito.")
