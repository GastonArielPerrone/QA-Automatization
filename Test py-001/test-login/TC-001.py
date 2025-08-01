import time
import pyautogui

#Acción 1: Abrir y ejecutar el programa a automatizar
pyautogui.hotkey('win','r') # digito win + r para abrir la pantalla de 'ejecutar' aplicaciones
pyautogui.write(r'C:/Users/usuario/Desktop/Usuarios/usuarios.exe')
pyautogui.press('enter')

#Acción 2: Escribir un usuario y clave válidos
time.sleep(4) # tiempo de espera de 3 segundos
pyautogui.write('admin') #escribo el usuario
pyautogui.press('tab')  #presiono la tecla tabulador
pyautogui.write('usernew') #escribo la clave
pyautogui.press('tab')     #presiono la tecla tabulador
pyautogui.press('space')   #presiono la tecla espacio 
time.sleep(1) # tiempo de espera de 1 segundos

#Acción 3: chequeo del resultado esperado (Aserción). Ingreso correcto a la aplicación.
try: # Probá de encontrar la imagen
    respuesta = pyautogui.locateOnScreen('img/Pantalla_Inicial_ok.png',confidence=0.90)
    if respuesta:
        print('Ingreso Correcto!')
except: # si no encuentra la imagen, en vez de un error, muestra este mensaje:
    print('Falló el acceso')

#Acción 4: cerrar el programa
time.sleep(1) # tiempo de espera de 1 segundos
pyautogui.hotkey('alt','f4') #cerrar el programa activo ('ctrl','f4')
