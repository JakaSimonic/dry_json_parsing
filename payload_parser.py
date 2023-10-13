from dataclasses import dataclass, field
from typing import Optional, Union, List

from dataclasses_json import dataclass_json, config
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds
from model.single import Single

CurrencyLists = Optional[List[Currency]]
OriginOfFundsLists = Optional[List[OriginOfFunds]]

CollectionLists = Union[CurrencyLists, OriginOfFundsLists]

def single(**kwargs):
    def _deserialize(value: dict) -> Optional[Single]:
        if not value:
            raise ValueError("single deserializer does not support None type.")
        return Single(value.get("value"))

    return field(
        default=None,
        metadata=config(
            decoder=_deserialize,
        ),
        **kwargs
    )


def collection(data_type: type, **kwargs):
    def _deserialize(datagroup: dict) -> CollectionLists:
        if not datagroup:
            raise ValueError("collection deserializer does not support None type.")
        collection_items = []
        for _, value in datagroup.get("collections", {}).items():
            item = value.get("properties", {})
            if item:
                collection_items.append(data_type(**item))
        return collection_items

    return field(
        default=None,
        metadata=config(
            decoder=_deserialize,
        ),
        **kwargs
    )


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = single()
    originOfFunds: OriginOfFundsLists = collection(OriginOfFunds)
    currency: CurrencyLists = collection(Currency)


with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())  # type: ignore
    print(payload)
