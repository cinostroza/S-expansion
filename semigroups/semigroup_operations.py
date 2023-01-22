from typing import Protocol


class Semigroup(Protocol):
    table: list[list[int]]
    order: int
    id: int

    def operation(self, i: int, j: int) -> int:
        """Performs a semigroup operation according to its multiplication table"""


def is_associative(s: Semigroup) -> bool:
    """This method returns True if the table is associative, false otherwise"""
    for i in range(0, s.order):
        for j in range(0, s.order):
            for k in range(0, s.order):
                if s.operation(i, s.operation(j, k)) != s.operation(s.operation(i, j), k):
                    return False
    return True


def is_commutative(s: Semigroup):
    """determines if a given semigroup is commutative or not"""
    for i in range(0, s.order):
        for j in range(0, s.order):
            if s.operation(i, j) != s.operation(j, i):
                return False
    return True


def find_zero(s: Semigroup) -> int:
    """Finds and returns the Zero element for a given semigroup, if there is no Zeroes, returns -1 instead"""
    is_zero = False
    for i in range(s.order):
        if is_zero:
            return i
        j = 0
        is_zero = True
        while is_zero and j < s.order:
            if s.table[j][i] != i + 1:
                is_zero = False
            j += 1
    if is_zero:
        return s.order
    return -1
