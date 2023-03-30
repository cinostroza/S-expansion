from __future__ import annotations

import enum
import os
from dataclasses import dataclass, field

from . import semigroup as sg

DATA_FILES_LOCATION = "./semigroups/data/order_"


class UnknownSemigroupOrderException(Exception):
    pass


class Order(enum.Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

    @classmethod
    def is_member(cls, member: str) -> bool:
        return member in cls.__members__


@dataclass
class SemigroupLoader:
    order: Order
    file_dict: dict = field(default_factory=dict)
    input_file: str = ""
    data: dict[int: sg.Semigroup] = field(default_factory=dict[int: sg.Semigroup])

    def __init__(self, order: Order):
        self.order = order
        self.file_dict = {
            Order.ZERO: None,
            Order.ONE: None,
            Order.TWO: f'{DATA_FILES_LOCATION}2',
            Order.THREE: f'{DATA_FILES_LOCATION}3',
            Order.FOUR: f'{DATA_FILES_LOCATION}4',
            Order.FIVE: f'{DATA_FILES_LOCATION}5',
            Order.SIX: f'{DATA_FILES_LOCATION}6',
        }
        self.input_file = self.file_dict[order]
        self.data = self.load_data()

    def load_data(self) -> dict[int: sg.Semigroup]:
        data = {}
        if self.order not in self.file_dict:
            print('order_exception')
            raise UnknownSemigroupOrderException
        print(os.getcwd())
        with open(self.input_file, 'r') as f:
            lines = f.read().splitlines()
        order = int(lines[0].split(" ")[-1])
        raw_table = iter(lines)
        while True:
            try:
                row = next(raw_table)
                if len(row) > 1:
                    _id = int(row.split(" ")[0])
                    semigroup_table = []
                    for i in range(order):
                        semigroup_row = []
                        for j in range(order):
                            semigroup_row.append(int(next(raw_table)))
                        semigroup_table.append(semigroup_row)
                    s = sg.Semigroup(order=order, id=_id, table=semigroup_table)
                    data[s.id] = s
            except StopIteration:
                break
        return data

    def get_semigroup(self, _id: int) -> sg.Semigroup:
        s = self.data.get(_id, None)
        if not s:
            raise UnknownSemigroupOrderException
        return s
