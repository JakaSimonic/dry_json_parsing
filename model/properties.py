from dataclasses import dataclass, fields
from typing import Any, Optional

from dataclasses_json import dataclass_json
from flattener_descriptor import Flattener

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


def flat_properties_factory(dataclass_instance: Properties) -> Properties:
    def flat_init(self, instance: Properties):
        self._instance = instance

    kwds: dict[str, Any] = {}

    kwds["__init__"] = flat_init
    kwds["__repr__"] = Properties.__repr__

    for field in fields(dataclass_instance):
        filed_type = str(field.type)
        kwds[field.name] = Flattener(filed_type)

    return type("FlatProperties", (), kwds)(dataclass_instance)
