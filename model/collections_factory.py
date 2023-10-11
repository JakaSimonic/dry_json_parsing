from dataclasses import dataclass, make_dataclass
from dataclasses_json import DataClassJsonMixin, dataclass_json
from typing import Any, Generic, Optional, TypeVar, Type, cast
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds

T = TypeVar("T")


@dataclass_json
@dataclass
class CollectionProperties(Generic[T]):
    properties: Optional[T] = None


@dataclass_json
@dataclass
class FieldCollection(Generic[T]):
    collections: Optional[dict[str, CollectionProperties[T]]] = None


def collection_factory(cls: type[T]) -> type[FieldCollection[T]]:
    name = cls.__name__
    properties_class_name = f"{name}Properties"
    collection_class_name = f"{name}Collections"

    properties_class = make_dataclass(
        properties_class_name,
        [("properties", cls, None)],
        bases=(DataClassJsonMixin,),
    )
    properties_class.__module__ = __name__

    properties_class = cast(type[CollectionProperties[T]], properties_class)

    collection_class = make_dataclass(
        collection_class_name,
        [("collections", dict[str, properties_class], None)],  # type: ignore
        bases=(DataClassJsonMixin,),
    )
    collection_class.__module__ = __name__

    return collection_class
