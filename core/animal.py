from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1
    Unknown = 2


class Animal:
    def __init__(self, species_id: int, gender: Gender) -> None:
        self.species_id = species_id
        self.gender = gender
