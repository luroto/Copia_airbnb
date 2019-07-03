#!/usr/bin/python3
''' Clase model Base '''
import uuid
import datetime
import models


class BaseModel:
    ''' class base for all the models '''
    def __init__(self, *ags, **kags):
        ''' Construtor of instance '''
        if kags:
            for key, value in kags.items():
                if key != '__class__':
                    if key == 'updated_at' or key == 'created_at':
                        value = datetime.datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' method string to print '''
        className = str("[" + self.__class__.__name__ + "] ")
        IdBase = str("(" + self.id + ") ")
        Dict = str(self.__dict__)
        return (className + IdBase + Dict)

    def save(self):
        ''' save the update time '''
        models.storage.save()
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
        ''' function to creat a personal dict '''
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['updated_at'] = self.created_at.isoformat()
        copy_dict['created_at'] = self.updated_at.isoformat()
        return copy_dict
