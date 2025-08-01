import time # Para darle tiempo a la ejecución
import pyautogui # Para automatizar.

# Acción 1: Abrir y ejecutar el programa
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write(r'C:/Users/usuario/Desktop/Usuarios/usuarios.exe')
pyautogui.press('enter')

# Cambiar codificación de salida para soportar UTF-8

print("Buscando el logo en pantalla...")

try:
    ubicacion_logo = pyautogui.locateOnScreen('img/logo.png', confidence=0.3)
    if ubicacion_logo:
        print("Logo encontrado en:", ubicacion_logo)
    else:
        print("Logo no encontrado en pantalla.")
except pyautogui.ImageNotFoundException:
    print("No se encontró la imagen del logo (ImageNotFoundException).")
except Exception as e:
    print("Ocurrió un error durante la búsqueda del logo:", str(e))