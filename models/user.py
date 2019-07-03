#!/usr/bin/python3
''' class of User, inherits from BaseModel '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' class to create and manage the user '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
