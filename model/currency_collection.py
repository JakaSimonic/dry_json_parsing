from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass
class Currency:
    buyCurrency: Optional[str] = None
    sellCurrency: Optional[str] = None

