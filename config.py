"""Импорты"""
# import keyring  # для паролей
import os
from datetime import datetime

MODE = 'test'



class Config:
    """Конфигурационный класс"""
    mode = MODE

    #Общие параметры
    url = r'https://www.rambler.ru/'
    robot_name = 'search_on_rambler'
    folder_root = os.path.dirname(os.path.abspath(__file__))
    folder_input = os.path.join(folder_root, 'INPUT')
    folder_output = os.path.join(folder_root, 'OUTPUT')
    folder_logs = os.path.join(folder_root, 'Logs')
    folder_template = os.path.join(folder_root, 'Template')

    # Создаем директории
    [os.makedirs(dir, exist_ok=True) for dir in
     [
         folder_input,
         folder_output,
         folder_logs,
         folder_template
     ]
     ]

    #Выбор типа параметров
    if mode.lower() == 'prod':
        support_email = ''
        browser_path = r''
        driver_path = r''
        load_path = r''
        current_year = ''
        work_date = []
        work_month = []
        log_limit = 50
    elif mode.lower() == 'test':
        template_output = os.path.join(folder_template, 'output.xlsx')
        support_email = 'blackday52@mail.ru'
        driver_path = r'/home/serj52/PycharmProjects/Soft/chromedriver'
        browser_path = r'/opt/google/chrome/google-chrome'
        log_limit = 10