'''PageObject для страницы Тензор.'''

from .base_page import BasePage
from .locators import TenzPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TenzPage(BasePage):
    """PageObject для страницы Тензор. Содержит методы для проверки блоков и переходов на tensor.ru."""

    def banner_silavludah(self):
        """
        Проверяет наличие блока 'Сила в людях' и его текст.
        Находит элемент по локатору и сравнивает текст.
        """
        baner = self.browser.find_element(*TenzPageLocators.LOCATOR_SILAVLUDAH_BLOCK_TXT)
        assert baner.text == 'Сила в людях', f'Блок "Сила в людях" отсутствует или текст не совпадает: {baner.text}'

    def about_in_block(self):
        """
        Прокручивает к ссылке 'Подробнее' и кликает по ней.
        Сначала ждёт появления элемента, затем скроллит к нему и кликает.
        """
        # Сначала ждем, пока элемент станет кликабельным
        link = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(TenzPageLocators.LOCATOR_MORE)
        )
        # Прокручиваем к элементу
        super().scroll(link)
        # Дополнительно ждем кликабельности после прокрутки
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(TenzPageLocators.LOCATOR_MORE)
        )
        # Кликаем по элементу
        link.click()


