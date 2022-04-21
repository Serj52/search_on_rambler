"""Импорты"""
import os
from traceback import print_tb, print_exc
import sys
# from Galib.EXСEPTION_HANDLER import ExcelopenError, ExcelwriteError, ExcelsaveError
import openpyxl
from config import Config as cfg



class Excel:
    # def __init__(self, input_file=''):
    #     self.input_file = input_file
    #     self.wb = openpyxl.load_workbook(input_file)
    #     self.sheet = self.wb['Лист1']
    #     self.end_column = self.sheet.max_column
    #     self.end_row = self.sheet.max_row
    @staticmethod
    def check_record(file):
        workbook = os.path.join(cfg.folder_input, file)
        wb = openpyxl.load_workbook(workbook)
        sheet = wb['Sheet1']
        if sheet.cell(row=2, column=1).value:
            return True
        else:
            return False

    def writer(self, file, name_column, value):
        """Сохраняет значение в нужный столбец"""
        wb = openpyxl.load_workbook(file)
        sheet = wb['Sheet1']
        column = self.search_column(wb, name_column)
        row = self.end_row(wb, column)
        sheet.cell(row=row, column=column).value = value
        wb.save(file)
        wb.close()
        # for column in range(1, sheet.max_column + 1):
        #     value_column = sheet.cell(row=1, column=column).value
        #     if name_column in value_column:
        #         sheet.cell(row=end_row, column=column).value = value
        #
        #         break

    def end_row(self, file, column):
        wb = file
        sheet = wb['Sheet1']
        row = 2
        while True:
            if sheet.cell(row=row, column=column).value:
                row += 1
                continue
            return row

    def search_column(self, file, column):
        wb = file
        sheet = wb['Sheet1']
        for index in range(1, sheet.max_column + 1):
            value_column = sheet.cell(row=1, column=index).value
            if column in value_column:
                return index




if __name__ == "__main__":
    file = '/home/serj52/PycharmProjects/search_on_rambler/OUTPUT/output.xlsx'
    e = Excel()
    e.writer(file, 'Ссылка', 'https')
    e.writer(file, 'Наименование материала', 'гайка')
    e.writer(file, 'Ссылка', 'https')
    e.writer(file, 'Наименование материала', 'болт')