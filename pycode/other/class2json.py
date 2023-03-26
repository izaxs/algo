import json
from json import JSONEncoder
from dataclasses import dataclass

# Frozen dataclass makes it immutable, so it can be used as a key in a dict
@dataclass(frozen=True)
class City:
    __slots__ = ["name", "state"]
    name: str
    state: str

# Better looking
@dataclass(slots=True, frozen=True)
class Address:
    city: City
    street: str
    pin: str

class Employee:
    __slots__ = ["name", "salary", "address"]

    def __init__(self, name: str, salary: int, address: Address):
        self.name = name
        self.salary = salary
        self.address = address

# The best way
@dataclass(slots=True)
class Team:
    name: str
    members: dict[str, Employee]
    titles: list[str]

    def say(self):
        print(self.name)

class Encoder(JSONEncoder):
    def default(self, o): return vars(o)

def encode(o):
    if hasattr(o, '__dict__'): return vars(o)
    d = {}
    for key in o.__slots__: d[key] = getattr(o, key)
    return d

# If __slots__ is not defined, we have to hardcode the all class attributes for the decode mapping
def decode(d: dict) -> object:
    classes = [Team, Employee, Address, City]
    keys = d.keys()
    for c in classes:
        if keys == set(c.__slots__): return c(**d)
    return d

city = City("Alpharetta", "WA")
address = Address(city, "7258 Spring Street", "30004")
employee = Employee("John", 9000, address)
team = Team("Team A", {employee.name: employee}, ["Manager", "Developer", "Tester"])

# teamJSON = Encoder().encode(employee)
# teamJSON = json.dumps(team, cls=Encoder, indent=2)
# teamJSON = json.dumps(team, default=lambda o: vars(o), indent=2)
teamJSON = json.dumps(team, default=encode, indent=2)
teamObject: Team = json.loads(teamJSON, object_hook=decode)
teamObjectJSON = json.dumps(teamObject, default=encode, indent=2)
print(teamObjectJSON)
