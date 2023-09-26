from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass
class Currency:
    buyCurrency: Optional[str] = None
    sellCurrency: Optional[str] = None


@dataclass_json
@dataclass
class CurrencyProperties:
    properties: Optional[Currency] = None


@dataclass_json
@dataclass
class CurrencyCollection:
    collections: Optional[dict[str, CurrencyProperties]] = None
