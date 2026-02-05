#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models"""
    
    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """String representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update timestamp"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert to dictionary"""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
