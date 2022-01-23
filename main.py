from Semigroup import Semigroup

data = {
    0: [1, 0, 2],
    1: [0, 2, 1],
    2: [2, 1, 0]
}

sg = Semigroup(_id=1, data=data)

print(sg.data)
print(sg.is_associative())
print(sg.order)

