from dataclasses_json import dataclass_json
from model.collections_factory import  collection_factory
from model.single import Single
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds
from dataclasses import dataclass, fields
from typing import Optional

CurrencyCollection = collection_factory(Currency)
OriginOfFundsCollection = collection_factory(OriginOfFunds)

@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None
