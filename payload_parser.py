from flattener_descriptor import FlatProperties
from model.properties import Properties

with open("fenx-payload.json") as f:
    payload = Properties.from_json(f.read())  # type: ignore

    flat_payload = FlatProperties(payload)
    print(flat_payload)
