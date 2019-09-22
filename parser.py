from dataclasses import dataclass


@dataclass
# Класс Организация, сожержит информацию об организации
class Company:
    region: str
    city: str
    name: str
    inn: int
    type: str
    industry: str
    address: str
    phone: str
    site: str
    facebook: str
    vkontakte: str
    instagram: str


from math import *


@dataclass
class Point:
    x: float
    y: float
    z: float

    def to_vector(self) -> tuple:
        return self.x, self.y, self.z

    def to_json(self) -> str:
        import json
        return json.dumps({
            'x': self.x,
            'y': self.y,
        })

    def distance(self, other) -> float:
        return sqrt(
            ((other.x - self.x) ** 2) +
            ((other.y - self.y) ** 2) +
            (())
        )
