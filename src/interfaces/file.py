from typing import List
from abc import ABC, abstractmethod
from entities.field import Field

class File(ABC):
    @abstractmethod
    def __init__(self, pandas, path: str):
        pass

    @abstractmethod
    def replace_columns_name(self, fields: List[Field]):
        pass
