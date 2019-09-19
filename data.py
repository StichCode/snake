import json


def to_send(data):
    return bytes(json.dumps(data), encoding="utf-8")


def from_send(data):
    return json.loads(data.decode("utf-8"))
