from typing import Any, Optional, Union, Callable
from model.collections_factory import COLLECTIONS_SUFFIX
from model.single import Single

CollectionCallableType = Callable[[Any], list]
SingleCallableType = Callable[[Optional[Single]], Optional[str]]

MappingCallableType = Union[SingleCallableType, CollectionCallableType]


class FlattnerMixin:
    @classmethod
    def flatten_mapper(cls, field_type: str) -> Optional[MappingCallableType]:
        if Single.__name__ in field_type:
            return cls.flatten_single

        if COLLECTIONS_SUFFIX in field_type:
            return cls.flatten_collection

        return None

    @staticmethod
    def flatten_collection(
        collection: Any,
    ) -> list:
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
