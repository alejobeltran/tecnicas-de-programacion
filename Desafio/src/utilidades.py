import os
#funcion encargada de ir limpiando la consola en cada cambio de menu u opcion
def limpiar_consola():
    #usando os se escribe en la consola cls para borrarla
    os.system("cls" if os.name == "nt" else "clear")