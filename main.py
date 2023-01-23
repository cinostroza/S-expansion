from semigroups.semigroups import Semigroups, Order
from semigroups.semigroup_operations import is_commutative


def run():
    order_3 = Semigroups(Order.THREE)
    for group in order_3.data.values():
        print(f'semigroup of id: {group.id} Associative?: {is_commutative(group)}')
    print(order_3.data)


if __name__ == '__main__':
    run()
