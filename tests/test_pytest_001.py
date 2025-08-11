from POM.AppLaunchPage import AppLaunchPage
from POM.LoginPage import LoginPage
from POM.HomePage import HomePage
import pytest # instalar con: pip install pytest en la terminal
import time

@pytest.fixture(scope="module")
def setup_app():
    # cargar las clases 
    launcher = AppLaunchPage()
    login_page = LoginPage()
    home_page = HomePage()

    #Paso 1: Abrir la app
    launcher.launch_app()
    #Paso 2: Escribir los datos del Login #usuario y # clave
    yield login_page, home_page
    #Teardown  (al final del módulo)
    time.sleep(0.5)
    home_page.close_app()

def test_login_con_datos_json(setup_app: tuple[LoginPage, HomePage]):
    #Act
    login_page, home_page = setup_app
    login_page.login("admin","usernew") # escribe los datos en pantalla

    # Assert
    time.sleep(0.5)
    assert home_page.is_login_ok(), "El acceso no funcionó correctamente"