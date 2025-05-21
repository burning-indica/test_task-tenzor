'''PageObject для страницы 'О компании' (about)'''
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import AboutPageLocators

class AboutPage(BasePage):
    """PageObject для страницы 'О компании'. Содержит методы для проверки раздела 'О компании'."""

    def url_about_is_right(self):
        """
        Проверяет, что текущий URL соответствует https://tensor.ru/about.
        Явно ждёт, пока URL не станет нужным, затем сравнивает.
        """
        url = 'https://tensor.ru/about'
        WebDriverWait(self.browser, 10).until(
            lambda driver: driver.current_url == url
        )
        assert self.browser.current_url == url, f'URL не соответствует: {self.browser.current_url}'

    def search_working_block(self):
        """
        Прокручивает страницу вниз и ждёт появления блока 'Работаем'.
        Скроллит к блоку и проверяет его наличие.
        """
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(AboutPageLocators.LOCATOR_WORKING)
        )
        working_block = self.browser.find_element(*AboutPageLocators.LOCATOR_WORKING)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", working_block)
        assert self.element_present(*AboutPageLocators.LOCATOR_WORKING), 'Нет блока "Работаем"'

    def pictures_have_same_sizes(self):
        """
        Проверяет, что все фотографии в блоке 'Работаем' одинакового размера.
        Сравнивает размеры всех изображений в блоке.
        """
        images = self.browser.find_elements(*AboutPageLocators.LOCATOR_PHOTOS)
        info = [(img.get_attribute("width"), img.get_attribute("height")) for img in images]
        w, h = info[0]
        for idx, (iw, ih) in enumerate(info[1:], 1):
            # Проверяем, что размеры совпадают с первым изображением
            assert (iw, ih) == (w, h), f'Фото №{idx+1} отличается по размеру: {iw}x{ih} (ожидалось {w}x{h})'
