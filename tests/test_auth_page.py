# Пример теста

from base_logic.pages.Auth_page_APP import *


# TEST-XXX
def test_auth_page_open(browser):
    print(f"\nTEST-XXX \nПроверка успешного открытия главной страницы")
    page = AuthPage(browser)
    assert page.get_relative_link() == "/"
