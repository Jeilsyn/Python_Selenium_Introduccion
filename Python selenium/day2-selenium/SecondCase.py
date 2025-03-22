#Second Case Manejo de formularios  
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
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "customers-grid")))

# Seleccionar el primer checkbox de la tabla
first_checkbox = driver.find_element(By.CSS_SELECTOR, "input.mastercheckbox")
first_checkbox.click()

# Mantener el navegador abierto para ver cambios
input("Presiona ENTER para cerrar el navegador...")
driver.quit()