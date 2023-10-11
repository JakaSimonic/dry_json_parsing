from typing import Optional, Union, Callable
from model.currency_collection import CurrencyCollection, Currency
from model.origin_of_funds_collection import OriginOfFundsCollection, OriginOfFunds
from model.single import Single

CollectionParam = Optional[Union[CurrencyCollection, OriginOfFundsCollection]]
CollectionRet = Optional[list[Union[Currency, OriginOfFunds]]]

CollectionCallableType = Callable[[CollectionParam], CollectionRet]
SingleCallableType = Callable[[Optional[Single]], Optional[str]]

MappingCallableType = Union[SingleCallableType, CollectionCallableType]


class FlattnerMixin:
    @classmethod
    def flatten_mapper(cls, field_type: str) -> Optional[MappingCallableType]:
        if "Single" in field_type:
            return cls.flatten_single

        if "Collection" in field_type:
            return cls.flatten_collection

        return None

    @staticmethod
    def flatten_collection(
        collection: CollectionParam,
    ) -> CollectionRet:
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

    @staticmethod
    def flatten_single(single: Optional[Single]) -> Optional[str]:
        if not single:
            return None
        value = single.value

        if not value:
            return None

        return value
