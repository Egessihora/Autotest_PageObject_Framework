# Пример теста

from base_logic.pages.Main_page_APP import *


# TEST-XXX
def test_main_page_open(browser):
    page = MainPage(browser)
    print(f"\nTLS_GW-001 \nПроверка успешного открытия главной страницы")
    assert page.get_relative_link() == "/"
