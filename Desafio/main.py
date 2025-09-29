from colorama import Fore, Style, init
from src import utilidades
import time
import os
import sys

global estado

def menu():
    global estado
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.YELLOW + "        📊  MENÚ PRINCIPAL  📊")
    print(Fore.CYAN + "="*40 + Style.RESET_ALL)
    print(Fore.GREEN + "1." + Style.RESET_ALL + " Calcular Promedio y Desviación")
    print(Fore.GREEN + "2." + Style.RESET_ALL + " Cantidad de Casos por Zona Geográfica")
    print(Fore.GREEN + "3." + Style.RESET_ALL + " Aplicar Filtros a los Datos")
    print(Fore.GREEN + "4." + Style.RESET_ALL + " Crear Gráficos")
    print(Fore.RED   + "0." + Style.RESET_ALL + " Salir")
    print(Fore.CYAN + "="*40 + Style.RESET_ALL)
    estado = "menu"

def main():
    global estado
    menu()
    while True:
        match estado:
            case "menu":
                dato = input("")
                if dato == "1":
                    estado = "opcion_1"
                elif dato == "2":
                    estado = "opcion_2"
                elif dato == "3":
                    estado = "opcion_3"
                elif dato == "4":
                    estado = "opcion_4"
                elif dato == "0":
                    estado = "opcion_5"
                else:
                    utilidades.limpiar_consola()
                    print(Fore.RED + "Valor Ingresado No Existe")
                    time.sleep(2)
                    estado = "menu" 
                    

if __name__ == "__main__":
    main()