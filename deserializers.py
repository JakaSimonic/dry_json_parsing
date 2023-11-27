from dataclasses import field
from typing import Optional

from dataclasses_json import config

def single(**kwargs):
    def _deserialize(value: dict) -> Optional[str]:
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

def collection(data_type: type, **kwargs):
    def _deserialize(datagroup: dict) -> list:
        if not datagroup:
            raise ValueError("collection deserializer does not support None type.")
        collection_items = []
        for _, value in datagroup.get("collections", {}).items():
            item = value.get("properties", {})
            if item:
                collection_items.append(data_type(**item))
        return collection_items

    return field(
        default=None,
        metadata=config(
            decoder=_deserialize,
        ),
        **kwargs
    )


