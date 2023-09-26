from dataclasses import make_dataclass
from dataclasses_json import DataClassJsonMixin
from typing import Optional


def collection_factory(name, fields):
    properties_class_name = f"{name}Properties"
    collection_class_name = f"{name}Collections"

    class_fileds = [(field, Optional[str], None) for field in fields]
    nested_class = make_dataclass(name, class_fileds, bases=(DataClassJsonMixin,))
    nested_class.__module__ = __name__

    properties_class = make_dataclass(
        properties_class_name,
        [("properties", Optional[nested_class], None)],
        bases=(DataClassJsonMixin,),
    )
    properties_class.__module__ = __name__

    collection_class = make_dataclass(
        collection_class_name,
        [("collections", Optional[dict[str, properties_class]], None)],
        bases=(DataClassJsonMixin,),
    )
    collection_class.__module__ = __name__

    return collection_class, nested_class


COLLECTIONS_TYPES = {
    "Currency": collection_factory("Currency", ["buyCurrency", "sellCurrency"]),
    "OriginOfFunds": collection_factory("OriginOfFunds", ["originOfFunds"]),
}
