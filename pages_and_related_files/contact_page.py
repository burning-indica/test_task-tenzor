'''PageObject для страницы 'Контакты'.'''

import time
from .base_page import BasePage
from .locators import ContactsPageLocators
from .locators import RegionLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class ContactsPage(BasePage):
    """PageObject для страницы 'Контакты'."""

    def click_banner_tenzor(self):
        """
        Кликает по баннеру Тензор на странице контактов.
        Повторяет попытку при StaleElementReferenceException (до 3 раз).
        Используется для перехода на сайт Тензор.
        """
        attempts = 0
        while attempts < 3:
            try:
                # Находим баннер Тензор
                link = self.browser.find_element(*ContactsPageLocators.LOCATOR_TENZOR_BANNER)
                # Кликаем по баннеру
                link.click()
                return
            except StaleElementReferenceException:
                # Если элемент устарел — ждём и пробуем снова
                time.sleep(0.5)
                attempts += 1
        # Если не удалось кликнуть — выбрасываем исключение
        raise Exception('Не удалось кликнуть по баннеру Тензор из-за StaleElementReferenceException')

    def region_in_contacts(self):
        """
        Проверяет, что регион возле заголовка 'Контакты' соответствует ожидаемому.
        Использует явное ожидание появления текста региона.
        """
        region_text = WebDriverWait(self.browser, 10).until(
            lambda d: d.find_element(*RegionLocators.LOCATOR_REGION).text
        )
        # Проверяем, что регион совпадает с ожидаемым
        assert region_text == 'Костромская обл.', f'Регион не верный: {region_text}'

    def region_in_contacts_button(self):
        """
        Открывает список регионов и выбирает Камчатский край.
        Использует явное ожидание кликабельности региона.
        """
        # Кликаем по кнопке выбора региона
        regions_button = self.browser.find_element(*RegionLocators.LOCATOR_REGION_BUTTON)
        regions_button.click()
        # Ждём, пока нужный регион станет кликабельным
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(RegionLocators.LOCATOR_REGION_KAMCHATKA)
        )
        # Кликаем по Камчатскому краю
        other_region = self.browser.find_element(*RegionLocators.LOCATOR_REGION_KAMCHATKA)
        other_region.click()

    def region_contacts_block(self):
        """
        Проверяет наличие блока партнёров на странице.
        """
        # Ищем блок партнёров
        regions_partners_block = self.browser.find_element(*RegionLocators.LOCATOR_REGION_PARTNERS_BLOCK)
        # Проверяем, что блок найден
        assert regions_partners_block, 'Нет блока партнеров'

    def check_and_save_info_regions(self):
        """
        Сохраняет информацию о регионе, url, title и списке партнёров.
        :return: список [регион, url, title, [партнёры]]
        """
        region_ms = []
        # Получаем текст региона через явное ожидание с обработкой StaleElementReferenceException
        attempts = 0
        while attempts < 3:
            try:
                region_text = WebDriverWait(self.browser, 10).until(
                    lambda d: d.find_element(*RegionLocators.LOCATOR_REGION).text
                )
                break
            except StaleElementReferenceException:
                time.sleep(0.5)
                attempts += 1
        else:
            raise Exception('Не удалось получить текст региона из-за StaleElementReferenceException')
        region_ms.append(region_text)
        # Сохраняем текущий URL и title
        url_ms = self.browser.current_url
        title_ms = self.browser.title
        region_ms.append(url_ms)
        region_ms.append(title_ms)
        # Получаем список партнёров через явное ожидание с обработкой StaleElementReferenceException
        attempts = 0
        while attempts < 3:
            try:
                partners = WebDriverWait(self.browser, 10).until(
                    lambda d: [el.text for el in d.find_elements(*RegionLocators.LOCATOR_REGION_PARTNERS_NAME)]
                )
                break
            except StaleElementReferenceException:
                time.sleep(0.5)
                attempts += 1
        else:
            raise Exception('Не удалось получить список партнёров из-за StaleElementReferenceException')
        region_ms.append(partners)
        return region_ms

    def check_change_region(self, old_inf, new_inf):
        """
        Проверяет, что после смены региона изменились регион, url, title и список партнёров.
        Сравнивает старую и новую информацию по каждому полю.
        """
        for i in range(len(old_inf)):
            if i == 0:
                # Проверяем, что регион изменился
                assert old_inf[i] != new_inf[i], f'Регион возле заголовка "контакты" не поменялся: {old_inf[i]} -> {new_inf[i]}'
            elif i == 1:
                # Проверяем, что url изменился
                assert old_inf[i] != new_inf[i], f'URL страницы не изменился: {old_inf[i]} -> {new_inf[i]}'
            elif i == 2:
                # Проверяем, что title изменился
                assert old_inf[i] != new_inf[i], f'title вкладки не поменялся: {old_inf[i]} -> {new_inf[i]}'
            elif i == 3:
                # Проверяем, что список партнёров изменился
                assert old_inf[i] != new_inf[i], f'Список партнеров не поменялся: {old_inf[i]} -> {new_inf[i]}'




