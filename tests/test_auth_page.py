# Пример теста

from base_logic.pages.Auth_page_APP import *


# TEST-XXX
def test_auth_page_open(browser):
    page = AuthPage(browser)
    print(f"\nTEST-XXX \nПроверка успешного открытия главной страницы")
    assert page.get_relative_link() == "/"
