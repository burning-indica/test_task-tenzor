'''Класс с тест-кейсом №2 (бизнес-логика)'''

import time
import allure
from pages_and_related_files.contact_page import ContactsPage
from pages_and_related_files.locators import (
    MainPageLocators, ContactsPageLocators, RegionLocators
)
from pages_and_related_files.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Тестирование сайта Тензор")
@allure.feature("Региональные настройки")
class TestCase2():
    """
    Тест-кейсы для проверки региона и смены региона на странице контактов.
    """

    @allure.story("Проверка региона и блока партнёров")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка корректности определения региона и наличия блока партнёров:
    1. Открытие главной страницы
    2. Переход в раздел 'Контакты'
    3. Проверка региона
    4. Проверка блока партнёров
    """)
    def test_open_link(self, browser):
        """
        Проверяет, что регион на странице контактов определён корректно и есть блок партнёров.
        """
        with allure.step("Открытие главной страницы"):
            page = MainPage(
                browser,
                MainPageLocators.MAIN_LINK
            )
            page.open_site()
        
        with allure.step("Ожидание и переход в раздел 'Контакты'"):
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(MainPageLocators.LOCATOR_CONTACTS_BUTTON)
            )
            page.go_to_contacts()
        
        with allure.step("Проверка региона"):
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(RegionLocators.LOCATOR_REGION)
            )
            contacts_page = ContactsPage(browser, browser.current_url)
            contacts_page.region_in_contacts()
        
        with allure.step("Проверка блока партнёров"):
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(ContactsPageLocators.LOCATOR_TENZOR_BANNER)
            )
            contacts_page.region_contacts_block()

    @allure.story("Смена региона")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка смены региона на 'Камчатский край':
    1. Открытие страницы контактов
    2. Сохранение информации о текущем регионе
    3. Выбор нового региона
    4. Проверка изменения информации
    """)
    def test_change_region(self, browser):
        """
        Проверяет смену региона на 'Камчатский край' и изменение информации на странице.
        """
        with allure.step("Открытие страницы контактов"):
            contacts_page = ContactsPage(browser, ContactsPageLocators.CONTACTS_LINK)
            contacts_page.open_site()
        
        with allure.step("Сохранение информации о текущем регионе"):
            old_inf = contacts_page.check_and_save_info_regions()
        
        with allure.step("Выбор нового региона"):
            contacts_page.region_in_contacts_button()
            WebDriverWait(browser, 10).until(
                lambda d: d.find_element(*RegionLocators.LOCATOR_REGION).text != old_inf[0]
            )
        
        with allure.step("Проверка изменения информации"):
            new_inf = contacts_page.check_and_save_info_regions()
            contacts_page.check_change_region(old_inf, new_inf)

