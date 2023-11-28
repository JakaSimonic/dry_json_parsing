from typing import Optional
from flattner_mixin import FlattnerMixin


class Flattener(FlattnerMixin):
    def __init__(self, field_type: str):
        self.flatten_func = self.flatten_mapper(field_type)

    def __set_name__(self, owner, name: str):
        self.name: str = name

    def __get__(self, instance, owner=None) -> list | Optional[str]:
        if not instance:
            raise Exception("Instance only method!")

        shadow_instance = instance._instance

        attribute = getattr(shadow_instance, self.name)

        if not self.flatten_func:
            return attribute

        return self.flatten_func(attribute)

    def __set__(self, obj, value):
        raise Exception("Read only!")

    def __delete__(self, obj, value):
        raise Exception("Read only!")
