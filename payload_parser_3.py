from dataclasses import dataclass, fields
from typing import Any, Callable, Optional, TypeVar, Union, Type

from dataclasses_json import dataclass_json
from model.collections_factory import  collection_factory
from model.single import Single
from model.currency_collection import Currency
from model.origin_of_funds_collection import OriginOfFunds
from model.properties import Properties


with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())

    flat_payload: Type[Properties] = FlatProperties(payload)
    print(flat_payload.currency)
