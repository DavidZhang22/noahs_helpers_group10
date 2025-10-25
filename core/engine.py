from core.ark import Ark
from core.player import Player
from core.cell import Cell

import core.constants as c


class Engine:
    def __init__(
        self,
        grid: list[list[Cell]],
        ark: Ark,
        helpers: list[Player],
        time: int,
    ) -> None:
        self.grid = grid
        self.ark = ark
        self.helpers = helpers
        self.time = time

        print(f"ark at: {self.ark.position}")

    def run_simulation(self) -> None:
        for time_elapsed in range(self.time):
            is_raining = time_elapsed >= self.time - c.START_RAIN
            print(f"time_elapsed: {time_elapsed}, is_raining: {is_raining}")
