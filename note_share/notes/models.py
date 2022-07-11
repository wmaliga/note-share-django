from datetime import date
from enum import Enum


# Create your models here.
class NoteType(Enum):
    PRIVATE = 'PRIVATE'
    PUBLIC = 'PUBLIC'


class Note:
    def __init__(self):
        self.id: int
        self.type: NoteType
        self.password: str
        self.title: str
        self.expirationDate: date
        self.data: str

    @staticmethod
    def from_json(json_dict):
        obj = Note()
        obj.id = json_dict['id']
        obj.type = json_dict['type']
        obj.password = json_dict['password']
        obj.title = json_dict['title']
        obj.expirationDate = json_dict['expirationDate']
        obj.data = json_dict['data']
        return obj
