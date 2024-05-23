# Пример теста

from base_logic.pages.Interfaces_pages import *


# TLS_GW-XXX
def test_admin_interface_page_open(browser):
    page = AdminInterface(browser)
    print(f"\nTLS_GW-001 \nПроверка успешного открытия веб-интерфейса администратора TLS Gateway")
    assert page.get_relative_link()
