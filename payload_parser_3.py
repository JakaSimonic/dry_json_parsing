from dataclasses import dataclass, fields
from typing import Any, Callable, Optional, TypeVar, Union

from dataclasses_json import dataclass_json
from model.collections_factory import COLLECTIONS_TYPES
from model.single import Single


CurrencyCollection, Currency = COLLECTIONS_TYPES["Currency"]
OriginOfFundsCollection, OriginOfFunds = COLLECTIONS_TYPES["OriginOfFunds"]

FlattenType = Callable[
    [Union[Any, Single]], Optional[Union[str, list[Any]]]
]


class Flattener:
    def __init__(self, flatten: FlattenType):
        self.flatten = flatten
        self.name = None
        self.instance = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if not instance:
            return self

        inner_instance = instance.instance

        attribute = getattr(inner_instance, self.name)
        return self.flatten(attribute)


def flatten_collection(collection: Any) -> Optional[list[Any]]:
    if not collection:
        return None
    collections = collection.collections

    if not collections:
        return None

    collection_items = []
    for _, value in collections.items():
        item = value.properties
        if item:
            collection_items.append(item)

    return collection_items


def flatten_single(single: Single) -> Optional[str]:
    if not single:
        return None
    value = single.value

    if not value:
        return None

    return value


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None


def flat_properties_class_factory():
    def flat_init(self, instance: Properties):
        self.instance = instance

    kwds = {"__init__": flat_init}
    for field in fields(Properties):
        type_name = str(field.type)
        if "Single" in type_name:
            func = flatten_single
        if "Collection" in type_name:
            func = flatten_collection
        if func:
            kwds[field.name] = Flattener(func)

    return type("FlatProperties", (), kwds)


FlatProperties = flat_properties_class_factory()

with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())

    flat_payload = FlatProperties(payload)
    print(flat_payload.currency)
