from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json
from deserializers import collection, single
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[str] = single()
    originOfFunds: list[OriginOfFunds] = collection(OriginOfFunds)
    currency: list[Currency] = collection(Currency)


with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())  # type: ignore
    print(payload)
