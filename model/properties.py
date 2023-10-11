from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from flattner_mixin import FlattnerMixin
from model.currency_collection import CurrencyCollection
from model.origin_of_funds_collection import OriginOfFundsCollection
from model.single import Single


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
