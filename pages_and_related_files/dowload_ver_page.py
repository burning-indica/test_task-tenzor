'''PageObject для страницы загрузки плагина.'''

import time
import re
import os

from .base_page import BasePage
from .locators import DownloadSabyLocators

class DownloadFiles(BasePage):
    """PageObject для страницы загрузки плагина. Содержит методы для проверки загрузки и размера файла."""

    def size_web_file_info(self):
        """
        Проверяет, что размер скачанного файла совпадает с указанным на сайте.
        1. Находит кнопку/ссылку для скачивания и извлекает размер из текста.
        2. Ждёт окончания загрузки файла.
        3. Проверяет размер скачанного файла.
        4. Удаляет файл после проверки.
        """
        # Находим кнопку/ссылку для скачивания
        button4 = self.browser.find_element(*DownloadSabyLocators.LOCATOR_DOWLOAD_HREF_BUTTON)
        # Извлекаем размер из текста кнопки
        buttontxt = "".join(re.findall(r"\d+\.+\d+", button4.text))
        buttonfloat = float(buttontxt)

        # Определяем путь к скачанному файлу
        path_file_dir = os.path.dirname(os.path.abspath(__file__))
        path_file_dir_all = path_file_dir + "\sbisplugin-setup-web.exe"

        # Ждём окончания загрузки файла (нет .crdownload файлов)
        super().check_dowload_end(path_file_dir)
        timeout = 30
        waited = 0
        while not os.path.exists(path_file_dir_all) and waited < timeout:
            time.sleep(0.5)
            waited += 0.5
        if not os.path.exists(path_file_dir_all):
            raise FileNotFoundError(f"Файл {path_file_dir_all} не найден после ожидания загрузки")

        # Проверяем размер файла
        file_info = os.stat(path_file_dir_all)
        file_size = round(file_info.st_size / 1048576, 2)
        print(f"Фактический размер файла: {file_size} МБ, Ожидалось: {buttonfloat} МБ")
        assert file_size == buttonfloat, f'Размер файла ({file_size} МБ) не совпадает с указанным на сайте ({buttonfloat} МБ)'

        # Удаляем файл после проверки
        os.remove(path_file_dir_all)




