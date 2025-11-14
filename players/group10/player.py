from core.action import Action, Obtain, Move
from core.message import Message
from core.player import Player
from core.snapshots import HelperSurroundingsSnapshot
from core.views.player_view import Kind

from core.animal import Animal
from random import random, choice

import math
from collections import defaultdict


class Player10(Player):
    def __init__(
        self,
        id: int,
        ark_x: int,
        ark_y: int,
        kind: Kind,
        num_helpers: int,
        species_populations: dict[str, int],
    ):
        super().__init__(id, ark_x, ark_y, kind, num_helpers, species_populations)

        self.grid = defaultdict(list)
        self.rain = False
        self.messages = []
        self.target = (100000, 100000)
        self.pos = (int(ark_x), int(ark_y))

    def _contains(self, a: Animal, lst: list[Animal]) -> bool:
        return any((a.species_id == b.species_id and a.gender == b.gender) for b in lst)

    def _distance(self, pos1: tuple[float, float], pos2: tuple[float, float]) -> float:
        return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])

    # random move copie d from random player
    def _get_random_move(self) -> tuple[float, float]:
        print("Getting random move")
        old_x, old_y = self.position
        dx, dy = random() - 0.5, random() - 0.5

        while not (self.can_move_to(old_x + dx, old_y + dy)):
            dx, dy = random() - 0.5, random() - 0.5

        return old_x + dx, old_y + dy

    def check_surroundings(self, snapshot: HelperSurroundingsSnapshot) -> int:
        self.sight = snapshot.sight
        self.position = snapshot.position
        # cast to int for grid indexing
        self.pos = (int(snapshot.position[0]), int(snapshot.position[1])) 
        self.rain = snapshot.is_raining
        self.flock = snapshot.flock

        # Update grid with animals in sight (Does not work)
        '''for x in range(-6, 6, 1):
            for y in range(-6, 6, 1):
                if math.hypot(x, y) > 5:
                    continue
                cell_view = self.sight.get_cellview_at(
                    self.pos[0] + x, self.pos[1] + y
                )
                self.grid[(x, y)] = cell_view.animals
        '''
        return 0

    def get_action(self, messages: list[Message]) -> Action | None:
        # Process messages
        for msg in messages:
            if 1 << (msg.from_helper.id % 8) == msg.contents:
                self.messages.append(msg.contents)

        # Noah cannot move
        if self.kind == Kind.Noah:
            return None

        if self.rain or self.is_flock_full():
            if self.position == self.ark_position:
                return None

            # Move towards ark

            return Move(*self.move_towards(*self.ark_position))

        # Try to obtain an animal if present

        cellview = self.sight.get_cellview_at(*self.pos)


        for animal in cellview.animals:
            if not self._contains(animal, self.flock):
                return Obtain(animal)

        # else move random

        while(self._distance(self.pos,  self.target) > 1008):
            self.target = (choice(range(0, 1000)), choice(range(0, 1000)))


        return Move(*self.move_towards(*self.target))
