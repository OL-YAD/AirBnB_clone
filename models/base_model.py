#!/usr/bin/python3
""" BaseModel class """


import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ save method """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict method """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                dict_repr[key] = value
        return dict_repr

    def do_update(self, args):
        """ Updates an instance based on the class name and id """

        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")

    def __str__(self):
        """ __str__ method """
        class_name = self.__class__.__name__
        return("[{}] ({}) {}".format(class_name, self.id, self.__dict__))


class BaseModelEncoder(JSONEncoder):
    """JSON"""
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
