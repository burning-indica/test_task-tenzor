'''PageObject для главной страницы.'''

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import DownloadSabyLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    """PageObject для главной страницы. Содержит методы для работы с главной страницей сайта."""

    def go_to_contacts(self):
        """
        Переходит в раздел 'Контакты' через футер.
        Находит ссылку по локатору и кликает по ней.
        """
        link = self.browser.find_element(*MainPageLocators.LOCATOR_CONTACTS_BUTTON)
        link.click()

    def dowload_saby_ver(self):
        """
        Кликает по кнопке 'Скачать локальные версии' в футере.
        Находит кнопку по локатору и кликает по ней для перехода на страницу загрузки.
        """
        butt = self.browser.find_element(*DownloadSabyLocators.LOCATOR_DOWNLOAD_LOCAL_VER_BUTTON)
        butt.click()

