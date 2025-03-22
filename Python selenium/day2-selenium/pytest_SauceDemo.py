import pytest
from SecondCase_pytest import SauceDemo

#Posibles errores

@pytest.fixture
def sauce():
    """Inicializa y devuelve una instancia de SauceDemo."""
    sauce = SauceDemo()
    sauce.open_website()
    yield sauce
    sauce.close_browser()

def test_login(sauce):
    """Prueba de inicio de sesión."""
    sauce.login("standard_user", "secret_sauce")
    assert "inventory" in sauce.driver.current_url  # Verifica si el login fue exitoso

def test_add_product_to_cart(sauce):
    """Prueba de agregar producto al carrito."""
    sauce.login("standard_user", "secret_sauce")
    sauce.add_first_product_to_cart()
    sauce.go_to_cart()
    assert "/cart.html" in sauce.driver.current_url  # Verifica si está en el carrito

def test_complete_purchase(sauce):
    """Prueba de completar compra."""
    sauce.login("standard_user", "secret_sauce")
    sauce.add_first_product_to_cart()
    sauce.go_to_cart()
    sauce.proceed_to_checkout()
    sauce.enter_checkout_info("Juan", "Pérez", "12345")
    success_message = sauce.finish_purchase()
    assert "Thank you for your order!" in success_message  # Verifica la compra exitosa
