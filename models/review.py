#!/usr/bin/python3
""" Review Class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
