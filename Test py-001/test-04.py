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

#acción 3: realizar cálculo matemático - 7 * 8 = 56
time.sleep(1)
pyautogui.hotkey('num7','*','num8', 'enter', interval=1) #num7 (tecla numérica-derecha) <> 7 (teclado general)

#acción 4: resetear calculadora
time.sleep(1)
ubicacionReset = pyautogui.locateOnScreen('reset.png', confidence=0.8)
if ubicacionReset is not None:
    centroReset = pyautogui.center(ubicacionReset)
    pyautogui.click(centroReset)
else:
    print("No se encontró el símbolo C para resetear")

#Ahora otra operación matemática que no me acepta por teclado como el "+" y otras.
#Usando recorte:
time.sleep(1)
pyautogui.press('num5')

time.sleep(1)
ubicacionSuma = pyautogui.locateOnScreen('suma.png')
centroSuma = pyautogui.center(ubicacionSuma)
pyautogui.click(centroSuma)

pyautogui.press('num6')
time.sleep(0.5)
pyautogui.press('enter')