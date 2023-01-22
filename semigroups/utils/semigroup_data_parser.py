from dataclasses import dataclass, field


@dataclass(slots=True)
class Semigroup:
    order: int = 0
    table: list = field(default_factory=list[list[int]])
    id: int = 0

    def operation(self, i: int, j: int) -> int:
        return self.table[i][j]


@dataclass
class DataProcessor:
    data: list[Semigroup] = field(default_factory=list[Semigroup])

    def __int__(self, input_file: str = "", output_file: str = ""):
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self) -> None:
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
                    s = Semigroup(order=order, id=_id, table=semigroup_table)
                    self.data.append(s)
            except StopIteration:
                break


def run():
    dp = DataProcessor()
    dp.input_file = "../data/order_3"
    dp.load_data()
    print(dp.data)


if __name__ == "__main__":
    run()
