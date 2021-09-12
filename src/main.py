import pandas as pd
from entities.field import Field
from excel import Excel

def main():
    file_path = '/home/robson/Desktop/test.xlsx'
    excel = Excel(pd, file_path)
    fields = [
        Field('Check List', 'check_list'),
        Field('Anuncio', 'anuncio')
    ]
    excel.replace_columns_name(fields)

main()
