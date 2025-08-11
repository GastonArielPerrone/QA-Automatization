import pyautogui
import time

class HomePage:
    def is_login_ok(self):
        #Acción 3: chequeo del resultado esperado (Aserción). Ingreso correcto a la aplicación.
        try: # Probá de encontrar la imagen y la encuentra
            respuesta = pyautogui.locateOnScreen('img/Pantalla_Inicial_ok.png',confidence=0.70)
            return True ## si es true encontró la imagen
        except: # si no encuentra la imagen, en vez de un error, muestra este mensaje:
            return False # es falso si no encontró la imagen

    def close_app(self):
        #Acción 4: cerrar el programa
        time.sleep(0.5) # tiempo de espera de 0.5 segundos
        pyautogui.hotkey('alt','f4') #cerrar el programa activo ('ctrl','f4')

    def envia_space(self):
        #Se utiliza en algunas ventanas para enviar una barra espaciadora extra
        pyautogui.press('space')
