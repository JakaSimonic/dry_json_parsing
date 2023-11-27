from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from flattner_mixin import FlattnerMixin
from model.currency_collection import Currency, CurrencyCollection
from model.origin_of_funds_collection import OriginOfFunds, OriginOfFundsCollection
from model.single import Single

@dataclass
class FlatProperties:
    eburyCountry: Optional[str]
    originOfFunds: Optional[list[OriginOfFunds]]
    currency: Optional[list[Currency]]


@dataclass_json
@dataclass
class Properties(FlattnerMixin):
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None

    def asflat(self) -> FlatProperties:
        return FlatProperties(
            eburyCountry=self.flatten_single(self.eburyCountry),
            originOfFunds=self.flatten_collection(self.originOfFunds),
            currency=self.flatten_collection(self.currency),
        )

