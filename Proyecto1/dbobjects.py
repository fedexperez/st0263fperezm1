from .crobject import Object
from .dbmanage import DBmanage

SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    }, 
    'KEY': {
        'type': 'int',
    }, 
    'VALUE': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    }
}

class DBObjects(DBmanage):

    def __init__(self):
        super().__init__(SCHEMA, 'crobjects')

def save_contact(self, crobject):
        data = [crobject.key, crobject.value]
        return self.insert(data)