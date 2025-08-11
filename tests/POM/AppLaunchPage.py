import pyautogui
import time

class AppLaunchPage:
    #funcion que ejecuta la aplicacion a testear
    def launch_app(self):
        #Acción 1: Abrir y ejecutar el programa a automatizar
        time.sleep(1)
        pyautogui.hotkey('win','r') # digito win + r para abrir la pantalla de 'ejecutar' aplicaciones
        pyautogui.write(r'C:\\Users\\usuario\\Desktop\\Usuarios\\usuarios.exe')
        pyautogui.press('enter')
        time.sleep(1)