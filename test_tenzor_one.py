'''Класс с тест-кейсом №1 (бизнес-логика)'''

import time
import allure
from pages_and_related_files.contact_page import ContactsPage
from pages_and_related_files.tenzor_page import TenzPage
from pages_and_related_files.about_page import AboutPage
from pages_and_related_files.locators import (
    MainPageLocators, TenzPageLocators, AboutPageLocators,
)
from pages_and_related_files.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Тестирование сайта Тензор")
@allure.feature("Навигация и контент")
class TestCase1():
    """
    Тест-кейсы для проверки перехода на сайт Тензор, блока 'Сила в людях' и проверки размеров фото.
    """

    @allure.story("Переход на сайт Тензор")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверка перехода на сайт Тензор через баннер:
    1. Открытие главной страницы
    2. Переход в раздел 'Контакты'
    3. Клик по баннеру Тензор
    4. Переключение на новую вкладку
    """)
    def test_open_link(self, browser):
        """
        Проверяет переход на страницу контактов и клик по баннеру Тензор.
        """
        with allure.step("Открытие главной страницы"):
            page = MainPage(
                browser,
                MainPageLocators.MAIN_LINK
            )
            page.open_site()
        
        with allure.step("Переход в раздел 'Контакты'"):
            page.go_to_contacts()
        
        with allure.step("Клик по баннеру Тензор"):
            contacts_page = ContactsPage(browser, browser.current_url)
            contacts_page.click_banner_tenzor()
        
        with allure.step("Переключение на новую вкладку"):
            contacts_page.change_win()

    @allure.story("Проверка блока 'Сила в людях'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка блока 'Сила в людях' и перехода по ссылке:
    1. Открытие страницы Тензор
    2. Проверка наличия блока 'Сила в людях'
    3. Переход по ссылке 'Подробнее'
    4. Проверка URL страницы 'О компании'
    """)
    def test_tenzpage_link(self, browser):
        """
        Проверяет наличие блока 'Сила в людях' и переход по ссылке 'Подробнее'.
        """
        with allure.step("Открытие страницы Тензор"):
            page = TenzPage(browser, TenzPageLocators.TENZ_LINK)
            page.open_site()
        
        with allure.step("Ожидание и проверка блока 'Сила в людях'"):
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(TenzPageLocators.LOCATOR_SILAVLUDAH_BLOCK_TXT)
            )
            page.banner_silavludah()
        
        with allure.step("Переход по ссылке 'Подробнее'"):
            page.about_in_block()
        
        with allure.step("Проверка URL страницы 'О компании'"):
            page = AboutPage(browser, browser.current_url)
            page.url_about_is_right()

    @allure.story("Проверка размеров фотографий")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка размеров фотографий в блоке 'Работаем':
    1. Открытие страницы 'О компании'
    2. Скролл к блоку 'Работаем'
    3. Проверка размеров всех фотографий
    """)
    def test_pic_size(self, browser):
        """
        Проверяет, что все фотографии в блоке 'Работаем' одинакового размера.
        """
        with allure.step("Открытие страницы 'О компании'"):
            page = AboutPage(browser, AboutPageLocators.ABOUT_LINK)
            page.open_site()
        
        with allure.step("Скролл к блоку 'Работаем'"):
            page.search_working_block()
        
        with allure.step("Проверка размеров фотографий"):
            page.pictures_have_same_sizes()

