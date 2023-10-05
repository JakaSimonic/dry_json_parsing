from dataclasses import dataclass
from typing import Optional, Union

from dataclasses_json import dataclass_json
from flattner_mixin import FlattnerMixin
from model.currency_collection import CurrencyCollection, Currency
from model.origin_of_funds_collection import OriginOfFundsCollection, OriginOfFunds
from model.single import Single

CollectionTypes = Union[CurrencyCollection, OriginOfFundsCollection]
CollectionItems = Union[Currency, OriginOfFunds]


@dataclass_json
@dataclass
class Properties(FlattnerMixin):
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None

    def asflat(self) -> dict:
        return {
            "eburyCountry": self.flatten_single(self.eburyCountry),
            "originOfFunds": self.flatten_collection(self.originOfFunds),
            "currency": self.flatten_collection(self.currency),
        }


with open("fenx-payload.json", "br") as f:
    payload = Properties.from_json(f.read())  # type: ignore
    flat_payload = payload.asflat()

    print(flat_payload)
