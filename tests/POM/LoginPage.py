import pyautogui
import time

class LoginPage:
    def login(self,usuario,clave): #
       #Acción 2: Escribir un usuario y clave válidos
        time.sleep(2) # tiempo de espera de 2 segundos
        pyautogui.write(usuario) #escribo el usuario
        pyautogui.press('tab')  #presiono la tecla tabulador
        pyautogui.write(clave) #escribo la clave
        pyautogui.press('tab')     #presiono la tecla tabulador
        pyautogui.press('space')   #presiono la tecla espacio 
        time.sleep(1) # tiempo de espera de 1 segundos 