import os
import pandas as pd
from business_selenium import Website
from Galib.EXCEL import Excel
from config import Config as cfg


class Business:
    def __init__(self):
        self.web = Website(cfg)
        self.excel = Excel()

    def main_process(self):
        if os.listdir(cfg.folder_input):
            print('В папке INPUT есть новые файлы')
            for file in os.listdir(cfg.folder_input):
                if self.excel.check_record(file):
                    print(f'В файле {file} есть записи')
                    data = self.create_dataframe(file)
                    self.web.work_with_site(data)

                else:
                    print(f'В файле {file} нет записей. Перехожу к следующему')
                    continue
            print('Все файлы обработаны')
        else:
            print('В папке INPUT нет новых файлов')

    def create_dataframe(self, file):
        """"Создание датафрейма"""
        workbook = os.path.join(cfg.folder_input, file)
        dataframe = pd.read_excel(io=workbook, engine='openpyxl', sheet_name='Sheet1', usecols=['NAMEMAT'])
        # Создаем словарь из список [{'col':'row1'},{'col':'row'}]
        data = dataframe.to_dict(orient='records')
        return data



if __name__ == "__main__":
    # lg = Log().set()
    bus = Business()
    bus.main_process()


