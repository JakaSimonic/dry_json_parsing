from model.properties import flat_properties_factory
from model.properties import Properties

with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())  # type: ignore

    flat_payload = flat_properties_factory(payload)
    print(flat_payload.currency)
