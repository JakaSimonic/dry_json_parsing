from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from model.collections_factory import collection_factory
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds
from model.single import Single

CurrencyCollection = collection_factory(Currency)
OriginOfFundsCollection = collection_factory(OriginOfFunds)


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None  # type: ignore
    currency: Optional[CurrencyCollection] = None  # type: ignore
