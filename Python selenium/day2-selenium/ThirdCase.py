from selenium import webdriver
import undetected_chromedriver as uc  # No detecta el selenium  pip install undetected-chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1) Open Web Browser (Chrome/firefox/IE).
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")  # Usuario
driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Contraseña
driver.find_element(By.ID, "login-button").click()  # Hacer login

print("#1) Open Web Browser(Chrome/firefox/IE).")
# Espera para que la página cargue
time.sleep(2)

# 2. Seleccionar el primer producto (por ejemplo, el que está en la lista)
product = driver.find_element(
    By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory"
)
product.click()
print("# 2. Seleccionar el primer producto (por ejemplo, el que está en la lista)")

# 3. Agregar el producto al carrito
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

# Esperar un momento para ver el cambio en la interfaz
time.sleep(2)

# 4. Ir al carrito y proceder a la compra
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
time.sleep(2)

# 5. Esperar explícitamente a que el botón de checkout esté presente
checkout_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_button"))
)
checkout_button.click()
time.sleep(2)

# 6. Completar los datos de la compra
driver.find_element(By.ID, "first-name").send_keys("Juan")
driver.find_element(By.ID, "last-name").send_keys("Pérez")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()
time.sleep(2)

# 7. Confirmar la orden
driver.find_element(By.CSS_SELECTOR, ".btn_action.cart_button").click()
time.sleep(2)

# Esperar para que la página cargue el resumen de la compra
time.sleep(2)

# 8. Capturar la pantalla
driver.save_screenshot("compra_exitosa2.png")
time.sleep(2)

# Imprimir un mensaje de éxito
print("Compra realizada y captura de pantalla guardada.")

# Espera para que puedas ver la pantalla
input("Presiona Enter para cerrar...")

# 9. Cerrar el navegador
driver.quit()
