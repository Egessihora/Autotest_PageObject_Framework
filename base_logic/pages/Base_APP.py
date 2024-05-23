# Базовый класс (шаблон), от которого будут наследоваться все объекты страниц

from base_logic.settings import base_url
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Класс реализует в себе необходимые методы для работы с webdriver. Принимает driver — экземпляр webdriver."""
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(timeout)  # неявное ожидание, по умолчанию на 10 сек.

    def get(self, url):
        """Переходит по указанному uri"""
        self.driver.get(url)

    def get_relative_link(self):
        """Получает адрес текущей страницы"""
        url = urlparse(self.driver.current_url)
        return url.path

    def go_back(self):
        """Имитирует нажатие кнопки 'Назад' в браузере"""
        self.driver.back()

    def refresh(self):
        """Обновляет страницу"""
        self.driver.refresh()

    def find_element(self, locator, time=10):
        """Находит один элемент и возвращает его"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_element_until_to_be_clickable(self, locator, time=10):
        """Ищет элемент в течение 10сек. до тех пока он не станет кликабельным"""
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')

    def screenshot(self, directory='/Bug_screenshots/', file_name='screenshot'):
        """Сохраняет скриншот"""
        self.driver.save_screenshot('/tests/screenshots' + directory + file_name + '.png')
