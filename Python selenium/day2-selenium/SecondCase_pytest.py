import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemo:
    def __init__(self):
        """Inicializa el WebDriver."""
        options = uc.ChromeOptions()
        self.driver = uc.Chrome(options=options)

    def open_website(self):
        """Abre la página de SauceDemo."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Inicia sesión con el usuario y contraseña dados."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def add_first_product_to_cart(self):
        """Añade el primer producto disponible al carrito."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def go_to_cart(self):
        """Navega al carrito."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def proceed_to_checkout(self):
        """Hace clic en el botón de checkout."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def enter_checkout_info(self, first_name, last_name, zip_code):
        """Llena el formulario de checkout."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_purchase(self):
        """Finaliza la compra."""
        self.driver.find_element(By.ID, "finish").click()
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return success_message.text

    def take_screenshot(self, filename="compra_exitosa.png"):
        """Guarda una captura de pantalla."""
        self.driver.save_screenshot(filename)

    def close_browser(self):
        """Cierra el navegador."""
        if self.driver:
            self.driver.quit()
