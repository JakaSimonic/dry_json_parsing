from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from model.currency_collection import CurrencyCollection
from model.origin_of_funds_collection import OriginOfFundsCollection
from model.single import Single
from flattner_mixin import FlattnerType
from flattener_descriptor import Flattener


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[Single] = None
    originOfFunds: Optional[OriginOfFundsCollection] = None
    currency: Optional[CurrencyCollection] = None


class FlatProperties:
    eburyCountry = Flattener(FlattnerType.SINGLE)
    originOfFunds = Flattener(FlattnerType.COLLECTION)
    currency = Flattener(FlattnerType.COLLECTION)

    __repr__ = Properties.__repr__

    def __init__(self, properties_instance: Properties):
        self._instance = properties_instance
