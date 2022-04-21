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
        self.excel = Excel()

    def work_with_site(self, input, output):
        self.web.open_site(site_url=self.config.url, folder_load='')
        for row in input:
            # #Находим окно поиска, вводим строку
            print(f'Ищем {row["NAMEMAT"]}')
            self.web.find_element(r"//input[@class='rui__3QXHo']").send_keys(f"{row['NAMEMAT']} цена")
            # Нажимаем кнопку найти
            self.web.find_element(r"//button[@class='rui__K3edI rui__3Mzuh']").click()
            time.sleep(3)
            #переключаемся на окно с ссылками
            self.web.switch_to_active_tab()
            links = self.web.find_elements("//a[@class='DirectNew__link--3n-k5 Serp__link--1Pmk1 components__delault_link--zPDKq']")
            count_link = 1
            print(f'Число ссылок на сайте {len(links)}')
            for link in links:
                if count_link > 1:
                    break
                time.sleep(3)
                link.click()
                time.sleep(3)
                #Переходим по ссылке
                self.web.switch_to_active_tab()
                #Записываем данные
                self.excel.writer(output, 'Ссылка', self.web.get_url())
                self.excel.writer(output, 'Наименование материала', row['NAMEMAT'])
                self.web.get_screen_shot(self.config.folder_output)
                # переключаемся на окно с ссылками
                self.web.switch_to_active_tab()
                self.web.close_tab()
                count_link += 1
            self.web.switch_to_active_tab()
            self.web.move_to_element(r"//button[@class='rui__K3edI rui__2YVgI']")
            self.web.find_element(r"//button[@class='rui__K3edI rui__2YVgI']").click()


if __name__ == "__main__":
    web = Website(Config)
    # exceldata = [{'NAMEMAT': 'Болт 3М12-6gх35.88.35Х.019'}, {'NAMEMAT': 'Гайка М14-6Н.10.35Х.019'}, ]
    exceldata = [{'NAMEMAT': 'Болт 3М12-6gх35.88.35Х.019'}, ]
    for row in exceldata:
                #Передаем параметры в вебфункцию
                webdata = web.work_with_site(
                    exceldata=row)