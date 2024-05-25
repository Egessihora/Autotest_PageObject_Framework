# Пример объекта страницы веб-приложения

from base_logic.pages.Base_APP import BasePage
from base_logic.settings import *
from base_logic.locators import *


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://xxx.xxx.xxx.xxx'
        driver.get(base_url)

        self.btn = driver.find_element(*AuthLocators.AUTH_BUTTON_ENTER)

# Методы, которые выполняют взаимодействие с элементами на этой странице
    def btn_click_enter(self):
        """Нажимает на кнопку 'Войти'"""
        self.btn.click()
