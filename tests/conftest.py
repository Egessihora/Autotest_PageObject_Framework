import pytest
from selenium import webdriver


# Инициализация браузера и его закрытие по окончанию тестов
@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()  # инициализируем браузер
    driver.maximize_window()
    yield driver
    #
    # if request.node.rep_call.failed:
    #     # Make the screen-shot if test failed:
    #     try:
    #         driver.screenshot('screenshots/' + str() + '.png')
    #
    # except:
    #         pass
    print("\nquit browser")
    driver.quit()  # закрываем браузер
