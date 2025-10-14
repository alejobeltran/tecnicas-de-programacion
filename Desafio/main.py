from colorama import Fore, Style, init
from src import utilidades
from src import analisis
from src import graficas
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
                promedio, municipios = analisis.mayor_promedio()
                print(Fore.CYAN + "\n🏙️  Municipios con casos por encima del promedio" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)
                print(f"📊 Promedio general de casos por municipio: {Fore.YELLOW}{promedio:.2f}{Style.RESET_ALL}\n")
                print(Fore.YELLOW + f"{'Municipio':<25}{'Casos':>10}" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)

                for nombre, cantidad in municipios.items():
                    print(f"{nombre:<25}{cantidad:>10}")

                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)
                print(f"👉 {Fore.GREEN}Estos municipios superan el promedio nacional de casos registrados.{Style.RESET_ALL}")

                input(Fore.YELLOW + "\nPresiona ENTER para volver al menú..." + Style.RESET_ALL)
                input()
                estado = "menu"
                
            case "opcion_4":
                utilidades.limpiar_consola()
                rec_2020, rec_2021, fallecidos = analisis.recuperacion()
                total_2020 = len(rec_2020)
                total_2021 = len(rec_2021)
                total_fallecidos = len(fallecidos)
                total_casos = total_2020 + total_2021 + total_fallecidos

                # evitar división por cero
                if total_casos > 0:
                    porc_2020 = (total_2020 / total_casos) * 100
                    porc_2021 = (total_2021 / total_casos) * 100
                    porc_fallecidos = (total_fallecidos / total_casos) * 100
                else:
                    porc_2020 = porc_2021 = porc_fallecidos = 0.0

                # Definir anchos (ajusta si quieres columnas más estrechas/anchas)
                col1 = 30   # ancho para la etiqueta (Año / Tipo)
                col2 = 10   # ancho para 'Casos'
                col3 = 12   # ancho para 'Porcentaje' (sin el %)

                print(Fore.CYAN + "\n🩺 Análisis de Recuperaciones y Fallecimientos" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*(col1 + col2 + col3) + Style.RESET_ALL)

                # Encabezado con los mismos anchos
                header = f"{'Año / Tipo':<{col1}}{'Casos':>{col2}}{'Porcentaje':>{col3}}"
                print(header)
                print(Fore.BLUE + "-"*(col1 + col2 + col3) + Style.RESET_ALL)

                # Filas con alineación: etiqueta izquierda, casos derecha, porcentaje derecha (y añadimos '%' al final)
                print(f"{Fore.YELLOW}{'Recuperados 2020':<{col1}}{total_2020:>{col2}}{porc_2020:>{col3 - 1}.2f}%{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{'Recuperados 2021':<{col1}}{total_2021:>{col2}}{porc_2021:>{col3 - 1}.2f}%{Style.RESET_ALL}")
                print(f"{Fore.RED   }{'Fallecidos':<{col1}}{total_fallecidos:>{col2}}{porc_fallecidos:>{col3 - 1}.2f}%{Style.RESET_ALL}")

                print(Fore.BLUE + "-"*(col1 + col2 + col3) + Style.RESET_ALL)

                # Interpretación breve
                print("📈 Interpretación breve:")
                print(f"   • Total casos considerados: {total_casos}")
                print("   • Los registros sin fecha de recuperación se consideran fallecimientos según la regla del dataset.\n")

                input(Fore.YELLOW + "👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)

                estado = "menu"
            case "opcion_5":
                utilidades.limpiar_consola()
                print(Fore.CYAN + "\n📊 MENÚ DE GRÁFICOS" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*45 + Style.RESET_ALL)
                print("1. Histograma de la distribución de edades")
                print("2. Gráfico de barras (por sexo, municipio)")
                print("3. Gráfico de dispersión entre dos variables")
                print("0. Volver al menú principal")
                print(Fore.BLUE + "-"*45 + Style.RESET_ALL)
                
                opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                
                if opcion == "1":
                    graficas.histograma()
                    input(Fore.YELLOW + "\nPresiona ENTER para continuar..." + Style.RESET_ALL)
                
                elif opcion == "2":
                    graficas.barras()
                    input(Fore.YELLOW + "\nPresiona ENTER para continuar..." + Style.RESET_ALL)
                
                elif opcion == "3":
                    graficas.dispersion()
                    input(Fore.YELLOW + "\nPresiona ENTER para continuar..." + Style.RESET_ALL)
                
                elif opcion == "0":
                    estado = "menu"
                
                else:
                    print(Fore.RED + "❌ Opción no válida, intenta nuevamente." + Style.RESET_ALL)
                    input(Fore.YELLOW + "\nPresiona ENTER para continuar..." + Style.RESET_ALL)
                        
            case "opcion_0":
                utilidades.limpiar_consola()
                exit()
                    

if __name__ == "__main__":
    main()