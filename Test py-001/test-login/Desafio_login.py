import time
import pyautogui

#Acción 1: Abrir y ejecutar el programa a automatizar
pyautogui.hotkey('win','r') # digito win + r para abrir la pantalla de 'ejecutar' aplicaciones
pyautogui.write(r'C:/Users/usuario/Desktop/Usuarios/usuarios.exe')
pyautogui.press('enter')
