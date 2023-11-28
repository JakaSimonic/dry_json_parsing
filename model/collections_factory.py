from dataclasses import make_dataclass

from dataclasses_json import DataClassJsonMixin


COLLECTIONS_SUFFIX = "Collections"


def collection_factory(cls: type) -> type:
    name = cls.__name__
    properties_class_name = f"{name}Properties"
    collection_class_name = f"{name}{COLLECTIONS_SUFFIX}"

    properties_class = make_dataclass(
        properties_class_name,
        [("properties", cls, None)],
        bases=(DataClassJsonMixin,),
    )
    properties_class.__module__ = __name__

    collection_class = make_dataclass(
        collection_class_name,
        [("collections", dict[str, properties_class], None)],  # type: ignore
        bases=(DataClassJsonMixin,),
    )
    collection_class.__module__ = __name__

    return collection_class
