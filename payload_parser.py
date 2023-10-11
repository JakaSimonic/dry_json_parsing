from model.properties import Properties

with open("fenx-payload.json", "br") as f:
    payload = Properties.from_json(f.read())  # type: ignore
    flat_payload = payload.asflat()

    print(flat_payload)
