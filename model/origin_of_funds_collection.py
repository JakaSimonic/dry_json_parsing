from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class OriginOfFunds:
    originOfFunds: Optional[str] = None


@dataclass_json
@dataclass
class OriginOfFundsProperties:
    properties: Optional[OriginOfFunds] = None


@dataclass_json
@dataclass
class OriginOfFundsCollection:
    collections: Optional[dict[str, OriginOfFundsProperties]] = None
