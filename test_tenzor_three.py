'''Класс с тест-кейсом №3 (бизнес-логика)'''

import time
import allure
from pages_and_related_files.main_page import MainPage
from pages_and_related_files.dowload_ver_page import DownloadFiles

from pages_and_related_files.locators import (
    MainPageLocators, DownloadSabyLocators)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Тестирование сайта Тензор")
@allure.feature("Загрузка файлов")
class TestCase3():
    """
    Тест-кейс для проверки скачивания и проверки размера файла СБИС Плагин.
    """

    @allure.story("Скачивание СБИС Плагин")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверка процесса скачивания СБИС Плагин:
    1. Открытие главной страницы
    2. Переход на страницу загрузки
    3. Скачивание файла
    4. Проверка размера файла
    """)
    def test_link_saby(self, browser):
        """
        Проверяет переход на страницу загрузки, скачивание файла и сравнение размера.
        """
        with allure.step("Открытие главной страницы"):
            page = MainPage(browser, MainPageLocators.MAIN_LINK)
            page.open_site()
        
        with allure.step("Переход на страницу загрузки"):
            page.dowload_saby_ver()
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(DownloadSabyLocators.LOCATOR_DOWLOAD_HREF_BUTTON)
            )
        
        with allure.step("Скачивание файла"):
            linkdowload = DownloadFiles(browser, browser.current_url)
            downlad_link = MainPage(browser, DownloadSabyLocators.LOCATOR_DOWLOAD_LINK_MY_VER)
            downlad_link.open_site()
        
        with allure.step("Проверка размера файла"):
            linkdowload.size_web_file_info()
