# Autotest_PageObject_Framework
____
**В корневой директории** расположен файл requirements.txt - список внешних зависимостей

**В директории /basic_logic расположены:**

* locators.py - локаторы web-элементов
* settings.py - исходные статические данные и учётные данные, используемые в проведении тестирования

**В директории /basic_logic/pages расположены:**

* Base_APP.py - необходимые методы для работы с webdriver
* Main_page_APP.py - объект главной страницы приложения

**В директории /tests расположены:**

файл conftest.py - содержит фикстуру для инициализации браузера и закрытия сессии после завершения теста
test_main_page.py - автоматизированные тесты с позитивными сценариями главной страницы

**В директории /tests/screenshots** расположены графические файлы с фиксацией результата тестирования
____

**Тесты настроены на запуск через Run!**
