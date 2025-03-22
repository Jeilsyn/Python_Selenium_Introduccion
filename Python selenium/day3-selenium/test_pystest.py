import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login(setup):
    setup.find_element(By.ID, "user-name").send_keys("standard_user")
    setup.find_element(By.ID, "password").send_keys("secret_sauce")
    setup.find_element(By.ID, "login-button").click()
    assert "inventory.html" in setup.current_url

