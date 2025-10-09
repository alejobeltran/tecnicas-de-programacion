from colorama import Fore, Style, init
from src import utilidades
from src import analisis
import time
import os
import sys

global estado

def menu():
    global estado
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "             📊  MENÚ PRINCIPAL  📊")
    print(Fore.CYAN + "="*50 + Style.RESET_ALL)
    print(Fore.GREEN + "1." + Style.RESET_ALL + " Calcular Promedio y Desviación")
    print(Fore.GREEN + "2." + Style.RESET_ALL + " Cantidad de Casos por Zona Geográfica")
    print(Fore.GREEN + "3." + Style.RESET_ALL + " Municipios con Casos Mayor al Promedio")
    print(Fore.GREEN + "4." + Style.RESET_ALL + " Fechas de Recuperacion y Casos de Fallecimiento")
    print(Fore.GREEN + "5." + Style.RESET_ALL + " Crear Gráficos")
    print(Fore.RED   + "0." + Style.RESET_ALL + " Salir")
    print(Fore.CYAN + "="*50 + Style.RESET_ALL)

def main():
    global estado
    estado = "menu"
    while True:
        match estado:
            case "menu":
                utilidades.limpiar_consola()
                menu()
                dato = input("")
                if dato == "1":
                    estado = "opcion_1"
                elif dato == "2":
                    estado = "opcion_2"
                elif dato == "3":
                    estado = "opcion_3"
                elif dato == "4":
                    estado = "opcion_4"
                elif dato == "5":
                    estado = "opcion_5"
                elif dato == "0":
                    estado = "opcion_0"

                else:
                    utilidades.limpiar_consola()
                    print(Fore.RED + "Valor Ingresado No Existe"+Style.RESET_ALL)
                    time.sleep(2)
                    estado = "menu" 
            case "opcion_1":
                utilidades.limpiar_consola()
                media_edad = analisis.promedio()
                desviacion_edad = analisis.desviacion()
                print(Fore.CYAN + "\n📊 Análisis de la Edad de los Contagiados" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*60 + Style.RESET_ALL)
                print(f"📌 Promedio de edad: {Fore.YELLOW}{media_edad:.2f}{Style.RESET_ALL} años")
                print(f"👉 En promedio, las personas contagiadas de {Fore.YELLOW}COVID{Style.RESET_ALL} "
                f"tienen alrededor de {Fore.YELLOW}{media_edad:.2f}{Style.RESET_ALL} años.\n")
                print(f"📌 Desviación estándar: {Fore.YELLOW}{desviacion_edad:.2f}{Style.RESET_ALL} años")
                if desviacion_edad < 10:
                     print("✅ Esto significa que la mayoría de los contagiados tienen edades "
                    "similares, concentradas cerca del promedio.\n")
                elif desviacion_edad < 20:
                    print("⚖️ Esto indica una dispersión moderada: los contagiados incluyen "
                    "tanto jóvenes como adultos.\n")
                else:
                    print("🌍 Esto sugiere una alta dispersión: hay casos en casi todas las "
                    "edades (niños, adultos y mayores).\n")
                print(Fore.BLUE + "-"*60 + Style.RESET_ALL)
                input(Fore.YELLOW + "👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)
                estado = "menu"

            case "opcion_2":
                utilidades.limpiar_consola()
                municipio = analisis.zona_geografica()
                print(Fore.CYAN + "\n📊 Cantidad de Casos por Ciudad" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*40 + Style.RESET_ALL)
                print(Fore.YELLOW + f"{'Ciudad':<25}{'Casos':>10}" + Style.RESET_ALL)
                print("-"*40)
                for indice,valor in municipio.items():
                    print(f"{indice:<25}{valor:>10}")
                print(Fore.BLUE + "-"*40 + Style.RESET_ALL)
                input(Fore.YELLOW + "\n👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)
                estado = "menu"

            case "opcion_3":
                utilidades.limpiar_consola()
                

            case "opcion_0":
                utilidades.limpiar_consola()
                exit()
                    

if __name__ == "__main__":
    main()