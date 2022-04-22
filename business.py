import os
import sys
import pandas as pd
from business_selenium import Website
from Galib.EXCEL import Excel
from config import Config as cfg
from datetime import datetime
import shutil
from Galib.EXСEPTION_HANDLER import Excelcheck_recordError, ExcelsaveError, ExcelwriteError, DataframeError
from traceback import print_tb, print_exc


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
                    input = self.create_dataframe(file)
                    output = os.path.join(cfg.folder_template,
                                          f'output {datetime.now().strftime("%d.%m.%Y %H-%M")}.xlsx')
                    shutil.copyfile(cfg.template_output, output)
                    self.web.work_with_site(input, output)
                else:
                    print(f'В файле {file} нет записей. Перехожу к следующему')
                    continue
            print('Все файлы обработаны')
        else:
            print('В папке INPUT нет новых файлов')

    def create_dataframe(self, file):
        """"Создание датафрейма"""
        try:
            workbook = os.path.join(cfg.folder_input, file)
            dataframe = pd.read_excel(io=workbook, engine='openpyxl', sheet_name='Sheet1', usecols=['NAMEMAT1', 'NAMEZP'])
            # Создаем словарь из список [{'col':'row1'},{'col':'row'}]
            data = dataframe.to_dict(orient='records')
            return data
        except Exception:
            print_exc(limit=2, file=sys.stdout)
            raise DataframeError(f'Ошибка в создании dataframe. Проверьте столбцы в {file}')



if __name__ == "__main__":
    # lg = Log().set()
    bus = Business()
    bus.main_process()


