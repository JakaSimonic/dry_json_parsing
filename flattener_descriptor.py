from typing import Optional
from flattner_mixin import CollectionRet, FlattnerMixin, FlattnerType
from model.properties import Properties
from model.single import Single
from model.origin_of_funds_collection import OriginOfFunds
from model.currency_collection import Currency



class Flattener(FlattnerMixin):
    def __init__(self, field_type: str):
        self.flatten_func = self.flatten_mapper(field_type)

    def __set_name__(self, owner, name: str):
        self.name: str = name

    def __get__(self, instance, owner=None) -> CollectionRet | Optional[str]:
        if not instance:
            raise Exception("Instance only method!")

        shadow_instance: Properties = instance._instance

        attribute = getattr(shadow_instance, self.name)

        if not self.flatten_func:
            return attribute

        return self.flatten_func(attribute)

    def __set__(self, obj, value):
        raise Exception("Read only!")

    def __delete__(self, obj, value):
        raise Exception("Read only!")

class FlatProperties:
    eburyCountry = Flattener(FlattnerType.SINGLE)
    originOfFunds = Flattener(FlattnerType.COLLECTION)
    currency = Flattener(FlattnerType.COLLECTION)
    
    __repr__ = Properties.__repr__

    def __init__(self, properties_instance: Properties):
        self._instance = properties_instance
