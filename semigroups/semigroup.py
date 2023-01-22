# This is a Python class to represent a Semigroup.
from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class Semigroup:
    order: int = 0
    table: list = field(default_factory=list[list[int]])
    id: int = 0

    def operation(self, i: int, j: int) -> int:
        return self.table[i][j]

