#!/usr/bin/python3



from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = FileStorage()


class Classes(dict):
    def __fetch__(self, key):
        try:
            return super(Classes, self).__fetch__(key)
        except Exception as e:
            raise Exception("** class doesn't exist **")


models = [BaseModel, User, State, City, Amenity, Place, Review]
classes = Classes(**{x.__name__: x for x in models})

storage.reload()
