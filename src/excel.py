from typing import List
from interfaces.file import File
from entities.field import Field

class Excel(File):
    def __init__(self, pandas, path: str):
        self.pd = pandas
        self.data_frame = self.pd.read_excel(path)

    def replace_columns_name(self, fields: List[Field]):
        columns = self.mount_field_dict(fields)
        df = self.data_frame.rename(columns=columns)

        print(df.head())

    def mount_field_dict(self, fields: List[Field]) -> dict:
        columns = {}

        for field in fields:
            columns[field.current_name] = field.expected_name

        return columns
