import pyautogui
import time

#acción 1: minimizar Visual Studio Code
# utilizando la presión de la tecla "Win" + dos veces la flecha hacia abajo
# y soltando "Win" obtengo el efecto de minimizar la aplicación actual, en este caso 
# minimizo Visual Studio Code
time.sleep(1)
pyautogui.keyDown('win')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.keyUp('win')

#acción 2: abrir la calculadora
time.sleep(1)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('calc', interval=0.5)
pyautogui.press('enter')

# búsqueda de las coordenadas del area de ejemplo donde recibiremos los resultados
time.sleep(1)
# pip install opencv-python
try: #captura de un error
    ubicacion = pyautogui.locateOnScreen('area_resultado.png', confidence=0.70)
    time.sleep(1)
    if ubicacion:
        print(ubicacion)
        izquierda = int(ubicacion.left)
        arriba = int(ubicacion.top)
        ancho = int(ubicacion.width)
        alto = int(ubicacion.height)
    else:
        print("No encontré la imagen")
except: # lo que sucede si hay un error en la búsqueda de la imagen 
    print("No encontré la imagen")