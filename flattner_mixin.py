from typing import Optional, Union, cast
from model.currency_collection import CurrencyCollection, Currency
from model.origin_of_funds_collection import OriginOfFundsCollection, OriginOfFunds
from model.single import Single

CollectionTypes = Union[CurrencyCollection, OriginOfFundsCollection]
CollectionItems = Union[list[Currency], list[OriginOfFunds]]


class FlattnerMixin:
    @staticmethod
    def flatten_collection(
        collection: Optional[CollectionTypes],
    ) -> list:
        collection_items: list = []
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
