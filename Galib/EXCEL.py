"""Импорты"""
import os
from traceback import print_tb, print_exc
import sys
# from Galib.EXСEPTION_HANDLER import ExcelopenError, ExcelwriteError, ExcelsaveError
import openpyxl


class Excel:
    def __init__(self, input_file=''):
        self.input_file = input_file
        self.wb = openpyxl.load_workbook(input_file)
        self.sheet = self.wb['Лист1']
        self.end_column = self.sheet.max_column
        self.end_row = self.sheet.max_row

    def writer(self, name_column, value):
        """Сохраняет значение в нужный столбец"""
        for column in range(1, self.end_column + 1):
            value_column = self.sheet.cell(row=1, column=column).value
            if name_column in value_column:
                self.sheet.cell(row=self.end_row + 1, column=column).value = value
                self.wb.save(self.input_file)
                break

