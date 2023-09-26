from dataclasses import dataclass
from typing import Any, Optional, Type, Union

from dataclasses_json import dataclass_json
from model.collections_factory import COLLECTIONS_TYPES
from model.single import Single

CurrencyCollection, Currency = COLLECTIONS_TYPES["Currency"]
OriginOfFundsCollection, OriginOfFunds = COLLECTIONS_TYPES["OriginOfFunds"]


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None

    @staticmethod
    def flatten_collection(
        collection: Any,
    ) -> Optional[list[Any]]:
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

    def asflat(self) -> dict:
        return {
            "eburyCountry": self.flatten_single(self.eburyCountry),
            "originOfFunds": self.flatten_collection(self.originOfFunds),
            "currency": self.flatten_collection(self.currency),
        }


with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read()).asflat()

    print(payload)
