from typing import Any, Optional, Union, Callable
from model.single import Single
from enum import Enum


CollectionCallableType = Callable[[Any], list]
SingleCallableType = Callable[[Optional[Single]], Optional[str]]

MappingCallableType = Union[SingleCallableType, CollectionCallableType]


class FlattnerType(Enum):
    NONE = 1
    COLLECTION = 2
    SINGLE = 3


class FlattnerMixin:
    @classmethod
    def flatten_mapper(
        cls, flattener_type: FlattnerType
    ) -> Optional[MappingCallableType]:
        if flattener_type is FlattnerType.SINGLE:
            return cls.flatten_single

        if flattener_type is FlattnerType.COLLECTION:
            return cls.flatten_collection

        return None

    @staticmethod
    def flatten_collection(collection: Any) -> list:
        collection_items = []

        if not collection:
            return collection_items
        collections = collection.collections

        if not collections:
            return collection_items

        for _, value in collections.items():
            item = value.properties
            if item:
                collection_items.append(item)

        return collection_items

    @staticmethod
    def flatten_single(single: Optional[Single]) -> Optional[str]:
        if not single:
            return None
        value = single.value

        if not value:
            return None

        return value
