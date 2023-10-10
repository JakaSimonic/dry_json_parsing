from dataclasses import fields
from typing import Any, TypeVar
from flattner_mixin import FlattnerMixin
from model.properties import Properties

T = TypeVar("T")


class Flattener(FlattnerMixin):
    def __init__(self, field_type: str):
        self.name = None

        self.flatten_func = self.flatten_mapper(field_type)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if not instance:
            return self

        shadow_instance = instance._instance

        attribute = getattr(shadow_instance, self.name)

        if not self.flatten_func:
            return attribute

        return self.flatten_func(attribute)

    def __set__(self, obj, value):
        raise Exception("Read only!")

    def __delete__(self, obj, value):
        raise Exception("Read only!")


def flat_properties_class_factory(dataclass_instance: Properties) -> Properties:
    def flat_init(self, instance: Properties):
        self._instance = instance

    kwds: dict[str, Any] = {}

    kwds["__init__"] = flat_init
    kwds["__repr__"] = Properties.__repr__

    for field in fields(dataclass_instance):
        filed_type = str(field.type)
        kwds[field.name] = Flattener(filed_type)

    return type("FlatProperties", (), kwds)(dataclass_instance)
