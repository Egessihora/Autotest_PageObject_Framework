# Пример объекта страницы веб-интерфейса администратора

import os
import time

from base_logic.pages.Base_APP import BasePage
from base_logic.settings import *
from base_logic.locators import *


class AdminInterface(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(base_url + ':' + admin_port)

