class DataframeError(Exception):
    """Исключение для метода business.create_dataframe"""
    def __init__(self, text):
        self.txt = text

class Excelcheck_recordError(Exception):
    """Исключение для метода excel.__init__"""
    def __init__(self, text):
        self.txt = text

class ExcelwriteError(Exception):
    """Исключение для метода excel.writer"""
    def __init__(self, text):
        self.txt = text

class ExcelsaveError(Exception):
    """Исключение для метода excel.save_xml"""
    def __init__(self, text):
        self.txt = text

class WebError(Exception):
    def __init__(self, text):
        self.txt = text
