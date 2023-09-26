from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import dataclass_json, config


def single(**kwargs):
    def _deserialize(value):
        if not value:
            raise ValueError("single deserializer does not support None type.")
        return value.get("value")

    return field(
        default=None,
        metadata=config(
            decoder=_deserialize,
        ),
        **kwargs
    )


def collection(field_name, **kwargs):
    def _deserialize(datagroup):
        if not datagroup:
            raise ValueError("collection deserializer does not support None type.")
        collection_items = []
        for _, value in datagroup.get("collections", {}).items():
            item = value.get("properties", {}).get(field_name)
            if item:
                collection_items.append(item)
        return collection_items

    return field(
        default=None,
        metadata=config(
            decoder=_deserialize,
        ),
        **kwargs
    )


@dataclass_json
@dataclass
class Properties:
    eburyCountry: Optional[str] = single()
    originOfFundsdatagroup: Optional[list[str]] = collection(field_name="originOfFunds")
    currency: Optional[list[str]] = collection(field_name="currency")


with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())
    print(payload)
