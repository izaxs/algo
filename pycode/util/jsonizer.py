from __future__ import annotations
import json
from typing import Type, Optional
from collections import namedtuple

class Point:
    def __init__(self, x: int, y: int, next: Optional[Point] = None):
        self.x = x
        self.y = y
        self.next = next

class User():
  def __init__(self, input):
      self.__dict__.update(input)

class PointEncoder(json.JSONEncoder):
    def default(self, obj):
            return [obj.x, obj.y]

def encode_default(obj: object):
    # class based object is not serializable by default
    json_str = json.dumps(obj)
    print(json_str)
    return json_str

def encode_by_dict(obj: object):
    json_str = json.dumps(obj.__dict__)
    print(json_str)
    return json_str

def encode_by_lambda(obj: object):
    json_str = json.dumps(obj, default=lambda o: o.__dict__)
    print(json_str)
    return json_str

def encode_encoder(obj: object, encoder: Type[json.JSONEncoder]):
    json_str = json.dumps(obj, cls=encoder)
    print(json_str)
    return json_str

def encode_to_file(obj: object):
    with open("data.json", "w") as f:
        json.dump(obj, f)

def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj

def decode_with_class(json_str: str, cls: Type[object]):
    data = json.loads(json_str, object_hook=cls)
    print(data)
    print(type(data))

def decode_with_namedtuple(json_str: str, name: str):
    def decoder(input: dict):
        nt = namedtuple(name, input.keys())
        return nt(**input)
    data = json.loads(json_str, object_hook=decoder)
    print(data)
    print(type(data))
    return data

def decode_with_namedtuple_lambda(json_str: str, name: str):
    data = json.loads(json_str, object_hook=lambda d: namedtuple(name, d.keys())(*d.values()))
    print(data)
    print(type(data))
    return data

if __name__ == '__main__':
    p = Point(1, 2)
    p.next = Point(3, 4)
    p.next.next = Point(5, 6)
    # encode_default(p)
    # encode_encoder(p, PointEncoder)
    s = encode_by_lambda(p)
    decode_with_namedtuple(s, "Point")
    decode_with_namedtuple_lambda(s, "Point")