# This is a Python class to represent a Semigroup.
import pandas as pd


class Semigroup:
    """This object represents a semigroup of any order
    data must be a dictionary or 2D json representing the multiplication table of the dictionary
    id is the unique identificator of the semigroup, order is the order"""

    def __init__(self, _id, order, data):
        self.id = _id
        self.data = pd.DataFrame.from_dict(data=data)
        self.order = order

    # a + (b + c) = (a + b) +c

    def operation(self, a, b):
        return self.data.iloc[a, b]

    def is_associative(self):
        for i in range(0, self.order):
            for j in range(0, self.order):
                for k in range(0, self.order):
                    if self.operation(i, self.operation(j, k)) != self.operation(self.operation(i, j), k):
                        return False
        return True

    def get_order(self):
        pass
