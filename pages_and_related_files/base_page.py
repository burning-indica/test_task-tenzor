'''Базовый класс для всех PageObject. Содержит общие методы для работы с WebDriver.'''
import os
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех PageObject. Содержит общие методы для работы с WebDriver."""

    def __init__(self, browser, url):
        """
        Инициализация базовой страницы.
        :param browser: экземпляр webdriver
        :param url: url страницы
        """
        self.browser = browser
        self.url = url

    def open_site(self):
        """
        Открывает страницу по self.url.
        """
        self.browser.get(self.url)

    def change_win(self):
        """
        Переключается на вторую вкладку браузера.
        Используется для перехода на новую вкладку после клика по ссылке.
        """
        new_page = self.browser.window_handles[1]
        self.browser.switch_to.window(new_page)

    def scroll(self, element):
        """
        Прокручивает страницу к переданному элементу.
        Использует execute_script для скролла.
        """
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def findd_element(self, locator, time=10):
        """
        Явное ожидание появления элемента по локатору.
        :param locator: локатор элемента
        :param time: максимальное время ожидания
        """
        WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def findd_elements(self, locator, time=10):
        """
        Явное ожидание появления всех элементов по локатору.
        :param locator: локатор элементов
        :param time: максимальное время ожидания
        """
        WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def element_present(self, how, what):
        """
        Проверяет наличие элемента на странице.
        :param how: тип поиска (By.CSS_SELECTOR и т.д.)
        :param what: значение локатора
        :return: True, если элемент найден, иначе False
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    '''Проверка наличия загруженного плагина по наличию/отсутсвию временного файла'''
    def check_dowload_end(self, path_file, timeout=30):
        """
        Проверяет, завершилась ли загрузка файла (нет .crdownload файлов в папке).
        :param path_file: путь к папке загрузки
        :param timeout: максимальное время ожидания (сек)
        :return: True, если загрузка завершена, иначе False
        """
        sec = 0

        while sec < timeout:
            files = os.listdir(path_file)
            # Проверяем наличие временных файлов загрузки
            if any(file.endswith(".crdownload") for file in files):
                time.sleep(0.2)
                sec += 0.2
            else:
                return True
        return False
