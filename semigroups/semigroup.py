# This is a Python class to represent a Semigroup.
import math
from dataclasses import dataclass, field


@dataclass
class MultiplicationTable:
    table: list = field(default_factory=list)


class Semigroup:
    """This object represents a semigroup of any order
    data must be a 2D array"""

    def __init__(self, _id: int, table: list) -> None:
        self.id = _id
        self.table = table

    def operation(self, a, b):
        return self.table[a][b]

    @property
    def order(self) -> int:
        """This method returns the order of the semigroup"""
        return len(self.table[0])

    def is_associative(self) -> bool:
        """This method returns True if the table is associative, false otherwise"""
        for i in range(0, self.order):
            for j in range(0, self.order):
                for k in range(0, self.order):
                    if self.operation(i, self.operation(j, k)) != self.operation(self.operation(i, j), k):
                        return False
        return True

    def is_commutative(self):
        for i in range(0, self.order):
            for j in range(0, self.order):
                if self.operation(i, j) != self.operation(j, i):
                    return False
        return True

    @property
    def zero(self) -> int:
        """This property sets the zero element of the semigroup, if there are no zeroes, sets it to -1"""
        is_zero = False
        for i in range(self.order):
            if is_zero:
                return i
            j = 0
            is_zero = True
            while is_zero and j < self.order:
                if self.table[j][i] != i + 1:
                    is_zero = False
                j += 1
        if is_zero:
            return self.order
        return -1
