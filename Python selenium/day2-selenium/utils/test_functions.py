from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element(driver, by, valor, tiempo=10):
    return WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located((by, valor))
    )


def set_element(driver, by, valor, texto, tiempo=10):
    elemento = get_element(driver, by, valor, tiempo)
    elemento.clear()
    elemento.send_keys(texto)
