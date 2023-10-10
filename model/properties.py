from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from model.currency_collection import CurrencyCollection
from model.origin_of_funds_collection import OriginOfFundsCollection

from model.single import Single


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None
