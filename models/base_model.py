#!/usr/bin/python3
""" Comments the module """
import datetime
import uuid
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        v = datetime.datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """Saves the current instance to the storage"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
