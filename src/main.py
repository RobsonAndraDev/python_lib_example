from typing import List
from enum import Enum
import pandas as pd
from entities.field import Field
from excel import Excel

class FileType(Enum):
    EXCEL = 0
    CSV   = 1
    TXT   = 2

class FileDatabase():
    def __init__(self, file_type: FileType):
        self.file_type = file_type

    def run(self, file_path: str, fields: List[Field]):
        database = self.launch_file(file_path)
        database.replace_columns_name(fields)

    def launch_file(self, file_path: str):
        if self.file_type == FileType.EXCEL:
            return Excel(pd, file_path)

        if self.file_type == FileType.CSV:
            pass

        if self.file_type == FileType.TXT:
            pass


