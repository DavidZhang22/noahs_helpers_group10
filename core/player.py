from abc import ABC, abstractmethod

from core.animal import Animal


class Player(ABC):
    def __init__(self, arkX: int, arkY: int):
        self.arkPosition = (arkX, arkY)
        self.position = (float(arkX), float(arkY))
        self.flock: list[Animal] = []

    @abstractmethod
    def run(self) -> None:
        pass
