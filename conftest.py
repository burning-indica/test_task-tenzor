import pytest
from selenium import webdriver
import os
#from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome()

    checkRootFolder = os.path.dirname(os.path.abspath(__file__))
    checkRootFolder = checkRootFolder + "\pages_and_related_files"

    if os.path.exists(checkRootFolder + "\sbisplugin-setup-web.exe"): #проверяем нет ли плагина в папке
        os.remove(checkRootFolder + "\sbisplugin-setup-web.exe")      #если есть, удаляем его

    chromeOptions = webdriver.ChromeOptions()

    prefs = {"download.default_directory": checkRootFolder,"download.directory_upgrade": True, 'safebrowsing.enabled' : 'true'}
    chromeOptions.add_argument("--disable-features=InsecureDownloadWarnings")
    chromeOptions.add_argument("--allow-running-insecure-content")
    #chromeOptions.add_argument("--unsafely-treat-insecure-origin-as-secure=http://upadte.saby.ru")
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    print(os.path.dirname(os.path.abspath(__file__)))

    yield driver
    driver.quit()