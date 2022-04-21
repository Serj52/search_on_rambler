from Galib.SELENIUM import BaseSelenium
import logging as lg
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import os
import time
from Galib.EXCEL import Excel
from config import Config


class Selenium(BaseSelenium):
    def __init__(self):
        super().__init__()

    def exists_by_xpath(self, xpath):
        """Проверяет наличие элемента на странице"""
        try:
            self.find_element(xpath)
            return True
        except NoSuchElementException:
            return False


class Website:
    """Класс для построения бизнес процесса при работе с сайтом"""

    def __init__(self, config):
        self.config = config
        self.web = Selenium()

    def work_with_site(self, exceldata) -> dict or bool:
        self.web.open_site(site_url=self.config.url, folder_load='')
        # #Находим окно поиска, вводим строку
        self.web.find_element(r"//input[@placeholder='Поиск по интернету']").send_keys(f"{exceldata['NAMEMAT']} цена")
        time.sleep(2)
        # Нажимаем кнопку найти
        self.web.find_element(r"//button[@class='rui__K3edI rui__3Mzuh']").click()
        time.sleep(3)
        # переключаемся на окно с ссылками
        self.web.switch_to_active_tab()
        links = self.web.find_elements("//a[@class='DirectNew__link--3n-k5 Serp__link--1Pmk1 components__delault_link--zPDKq']")
        count_link = 1
        print(len(links))
        for link in links:
            # переключаемся на окно с ссылками
            self.web.switch_to_active_tab()
            time.sleep(3)
            link.click()
            time.sleep(3)
            self.web.switch_to_active_tab()
            self.web.get_screen_shot(self.config.folder_output)
            time.sleep(3)
            # переключаемся на окно с ссылками
            self.web.switch_to_active_tab()
            self.web.close_tab()
            time.sleep(2)
            if count_link > 10:
                break
            count_link += 1


if __name__ == "__main__":
    web = Website(Config)
    # exceldata = [{'NAMEMAT': 'Болт 3М12-6gх35.88.35Х.019'}, {'NAMEMAT': 'Гайка М14-6Н.10.35Х.019'}, ]
    exceldata = [{'NAMEMAT': 'Болт 3М12-6gх35.88.35Х.019'}, ]
    for row in exceldata:
                #Передаем параметры в вебфункцию
                webdata = web.work_with_site(
                    exceldata=row)