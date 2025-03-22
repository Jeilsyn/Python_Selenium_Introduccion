#Test_case
from selenium import webdriver
import undetected_chromedriver as uc #No  detecta el selenium  pip install undetected-chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_functions import get_element, set_element


import time

#1) Open Web Browser(Chrome/firefox/IE).
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

#2) Open URL https://admin-demo.nopcommerce.com/login
driver.get("https://admin-demo.nopcommerce.com/login")

#3) Provide Email (admin@yourstore.com).
set_element(driver, By.ID, "Email", "admin@yourstore.com")
set_element(driver, By.ID, "Password", "admin")

#5) Click on Login
loginbtn = get_element(driver, By.CLASS_NAME, 'button-1')
print("\n\n Abemus boton ")

if loginbtn:
    loginbtn.click()
    print("\n\nEl botón de login fue clickeado correctamente.")
else:
    print("\n\nNo se encontró el botón de login.")
print("\n\nEl login btn funciona ")

#6) Esperar a que la página de Dashboard se cargue completamente
try:
    # Espera a que un elemento específico del Dashboard esté presente (puedes cambiarlo según lo que esté disponible en tu página)
    WebDriverWait(driver, 20).until(EC.title_contains("Dashboard"))  # Espera a que el título contenga "Dashboard"
    
    # Captura el título de la página
    act_title = driver.title
    print("\nTítulo actual de la página: ", act_title)
    
    #7) Verificar título de la página: "Dashboard / nopCommerce administration" (Expected)
    exp_title = "Dashboard / nopCommerce administration"
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Test Failed: El título no es el esperado.")
        
except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
    #8) Cerrar el navegador
    time.sleep(2)



driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customers-grid")))

# 7) Seleccionar el primer checkbox de la tabla
first_checkbox = get_element(driver,By.CSS_SELECTOR, "input.mastercheckbox")
first_checkbox.click()

# 8) Mantener el navegador abierto hasta que el usuario presione ENTER
input("Presiona ENTER para cerrar el navegador...")

# 9) Cerrar el navegador correctamente
driver.quit()

