from main import FileType, FileDatabase
from entities.field import Field

file_databe = FileDatabase(FileType.EXCEL)
file_path = '/home/robson/Desktop/test.xlsx'
fields = [
    Field('Check List', 'check_list'),
    Field('Anuncio', 'anuncio')
]
file_databe.run(file_path, fields)