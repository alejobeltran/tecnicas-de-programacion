#Se importa libreria encargada de cambiar los colores de los print
from colorama import Fore, Style
#se inportan los archivos del paquete de datos SRC
from src import utilidades
from src import analisis
from src import graficas
#Se importa time para usar sleep
import time

#variable global encargada de fijar el estado de la interfaz
global estado

#funcion menu que enseña el menu principal con todas sus opciones
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

#funcion principal de todo el programa que se encarga de gestionar la interfaz y conectar toda la logica
def main():
    #se establece la variable global como "menu" para que se inicie con el menu principal
    global estado
    estado = "menu"
    #ciclo infinito para actualizar la interfaz
    while True:
        #se usa match para cambiar la interfaz dependiendo de la variable estado
        match estado:
            case "menu":
                #utilidades.limpiar_consola() pone automaticamente cls en la consola para dejarla limpia
                utilidades.limpiar_consola()
                #se llama al menu principal
                menu()
                #se espera que el usuario ingrese un valor para seleccionar el menu
                dato = input("")
                #dependiendo del valor se establece un texto a la variable estado que luego se usa en el match case
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
                    #si un valor erroneo es ingresado se limpia la consola y se manda un mensaje de error por 2 segundos
                    utilidades.limpiar_consola()
                    print(Fore.RED + "Valor Ingresado No Existe"+Style.RESET_ALL)
                    time.sleep(2)
                    estado = "menu" 

            case "opcion_1":
                #opcion 1 se encarga de calcular el promedio y desviacion
                utilidades.limpiar_consola()
                #el archivo analisis se encarga de calcular todos los datos de la base de datos, en este caso se llama el promedio y desviacion
                media_edad = analisis.promedio()
                desviacion_edad = analisis.desviacion()
                print(Fore.CYAN + "\n📊 Análisis de la Edad de los Contagiados" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*60 + Style.RESET_ALL)
                print(f"📌 Promedio de edad: {Fore.YELLOW}{media_edad:.2f}{Style.RESET_ALL} años")
                print(f"👉 En promedio, las personas contagiadas de {Fore.YELLOW}COVID{Style.RESET_ALL} "
                f"tienen alrededor de {Fore.YELLOW}{media_edad:.2f}{Style.RESET_ALL} años.\n")
                print(f"📌 Desviación estándar: {Fore.YELLOW}{desviacion_edad:.2f}{Style.RESET_ALL} años")

                #dependiendo de la desviacion se establece un texto diferente para explicar la situacion

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

                #se usa un input para bloquear el codigo y que este siga solo al dar enter
                input(Fore.YELLOW + "👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)
                estado = "menu"

            case "opcion_2":
                #la opcion se encarga de enseñar la cantidad de casos por zona geografica
                utilidades.limpiar_consola()
                #zona geografica devuelve un diccionario con los municipios y los casos 
                municipio = analisis.zona_geografica()
                print(Fore.CYAN + "\n📊 Cantidad de Casos por Municipios" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*40 + Style.RESET_ALL)
                print(Fore.YELLOW + f"{'Ciudad':<25}{'Casos':>10}" + Style.RESET_ALL)
                print("-"*40)
                #se extraen los datos del for para enseñarlos de forma ordenada en la consola
                for indice,valor in municipio.items():
                    print(f"{indice:<25}{valor:>10}")
                print(Fore.BLUE + "-"*40 + Style.RESET_ALL)
                input(Fore.YELLOW + "\n👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)
                estado = "menu"

            case "opcion_3":
                #opcion 3 se encarga de enseñar los municipios que cuentan con casos mayor al promedio
                utilidades.limpiar_consola()
                #mayor al promedio devuelve una lista con 2 datos, el promedio y un diccionario con los municipios mayor al promedio
                promedio, municipios = analisis.mayor_promedio()
                print(Fore.CYAN + "\n🏙️  Municipios con casos por encima del promedio" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)
                print(f"📊 Promedio general de casos por municipio: {Fore.YELLOW}{promedio:.2f}{Style.RESET_ALL}\n")
                print(Fore.YELLOW + f"{'Municipio':<25}{'Casos':>10}" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)
                #se extraen los datos del diccionario para ordenarlos adecuadamente
                for nombre, cantidad in municipios.items():
                    print(f"{nombre:<25}{cantidad:>10}")

                print(Fore.BLUE + "-"*65 + Style.RESET_ALL)
                print(f"👉 {Fore.GREEN}Estos municipios superan el promedio nacional de casos registrados.{Style.RESET_ALL}")

                input(Fore.YELLOW + "\nPresiona ENTER para volver al menú..." + Style.RESET_ALL)
                estado = "menu"
                
            case "opcion_4":
                #La opcion 4 se encarga de enseñar las personas recuperadas y fallecidas
                utilidades.limpiar_consola()
                #Recuperacion devuelve 3 datos, un diccionario con los recuperados en 2020, en 2021 y los fallecidos
                rec_2020, rec_2021, fallecidos = analisis.recuperacion()
                #se extrae el total de los datos
                total_2020 = len(rec_2020)
                total_2021 = len(rec_2021)
                total_fallecidos = len(fallecidos)
                total_casos = total_2020 + total_2021 + total_fallecidos

                # evitar división por cero
                if total_casos > 0:
                    #se saca el porcentaje
                    porc_2020 = (total_2020 / total_casos) * 100
                    porc_2021 = (total_2021 / total_casos) * 100
                    porc_fallecidos = (total_fallecidos / total_casos) * 100
                else:
                    porc_2020 = porc_2021 = porc_fallecidos = 0.0

                # Definir espacios de los print
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

                print("📈 Interpretación breve:")
                print(f"   • Total casos considerados: {total_casos}")
                print("   • Los registros sin fecha de recuperación se consideran fallecimientos según la regla del dataset.\n")

                input(Fore.YELLOW + "👉 Presiona ENTER para volver al menú..." + Style.RESET_ALL)

                estado = "menu"
            case "opcion_5":
                #la opcion 5 cuenta con otro menu el cual se encarga de enseñarnos graficas de los datos
                utilidades.limpiar_consola()
                #se imprime el menu de graficas
                print(Fore.CYAN + "\n📊 MENÚ DE GRÁFICOS" + Style.RESET_ALL)
                print(Fore.BLUE + "-"*45 + Style.RESET_ALL)
                print("1. Histograma de la distribución de edades")
                print("2. Gráfico de barras (por sexo, municipio)")
                print("3. Gráfico de dispersión entre dos variables")
                print("0. Volver al menú principal")
                print(Fore.BLUE + "-"*45 + Style.RESET_ALL)
                #se espera que el usuario ingrese una opcion
                opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
                
                #se llama al archivo graficas que genera el histograma, grafica de barras y grafico de dispersion 
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
                #en caso de que la opcion 0 se active, el programa se cierra
                exit()
                    
#esta funcion se usa ya que contamos con varios archivos de python y asegura que la funcion main solo se ejecute cuando sea llamada desde este mismo codigo y no de otro
if __name__ == "__main__":
    main()