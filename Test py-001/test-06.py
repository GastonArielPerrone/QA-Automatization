import pyautogui
import time
import pytesseract  # type: ignore
from PIL import Image, ImageEnhance

# Instalar Pillow
#   pip install pillow
# Instalar PyTesseract
#   pip install pytesseract 
# Instalar Tesseract
# https://github.com/tesseract-ocr/tesseract/releases

# Configurar ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

# Acción 1: minimizar Visual Studio Code (Win + flecha abajo dos veces)
time.sleep(1)
pyautogui.keyDown('win')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.keyUp('win')

# Esperar para que se refleje el cambio
time.sleep(1)

# Acción 2: tomar parte de la pantalla con el resultado
x, y, ancho, alto = 1010, 261, 88, 24
imagen = pyautogui.screenshot(region=(x, y, ancho, alto))  # captura de pantalla

# Mejorar contraste para OCR
imagen = ImageEnhance.Contrast(imagen).enhance(2.5)

# Guardar imagen para revisión
imagen.save("asercion.png")

# Aplicar OCR, modo línea única para mejorar precisión
texto = pytesseract.image_to_string(imagen, config='--psm 7').strip()

print("Resultado obtenido:", repr(texto))

# Limpiar texto: conservar solo dígitos
texto_limpio = ''.join(filter(str.isdigit, texto))

if texto_limpio:
    numero = int(texto_limpio)
    if numero == 44:
        print("La calculadora funciona bien")
    else:
        print(f"La calculadora funciona mal, devolvió {numero}")
else:
    print("No se detectó un número válido en la imagen OCR.")