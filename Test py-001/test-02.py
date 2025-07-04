#Este RPA va a simular dirigirse a un block de notas abierto y realizar
#una escritura.
import pyautogui

pyautogui.moveTo(x=23, y=59, duration=3)#Se dirige a las coordenadas, duración 3s
pyautogui.click()#Hace click
pyautogui.write("Escribo el primer renglon.", interval=0.4)#Escribe con intervalos

#Se prepara para realizar otra escritura en otra coordenada.
pyautogui.moveTo(x=14, y=148, duration=3)
pyautogui.click()
pyautogui.write("Escribo el segundo renglon", interval=0.4)