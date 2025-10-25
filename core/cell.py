from core.animal import Animal


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.animals: list[Animal] = []

        self.up: Cell | None = None
        self.down: Cell | None = None
        self.left: Cell | None = None
        self.right: Cell | None = None
