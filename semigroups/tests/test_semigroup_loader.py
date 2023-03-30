import unittest
from semigroups.semigroup import Semigroup

from semigroups.semigroup_loader import Order, SemigroupLoader


class TestSemigroupLoader(unittest.TestCase):

    def test_loads_order_two(self):
        """Asserts that semigroups of order 2 are correctly loaded"""
        order_2 = SemigroupLoader(Order.TWO)
        self.assertEqual(order_2.order, Order.TWO)
        self.assertIn(1, order_2.data.keys())
        self.assertIn(4, order_2.data.keys())
        self.assertNotIn(5, order_2.data.keys())
        for key, semigroup in order_2.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(2, semigroup.order)
            self.assertEqual(2, len(semigroup.table))

    def test_loads_order_three(self):
        """Asserts semigroups of order 3 are correctly loaded"""
        order_3 = SemigroupLoader(Order.THREE)
        self.assertEqual(order_3.order, Order.THREE)
        self.assertIn(1, order_3.data.keys())
        self.assertIn(18, order_3.data.keys())
        self.assertNotIn(19, order_3.data.keys())
        for key, semigroup in order_3.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(3, semigroup.order)
            self.assertEqual(3, len(semigroup.table))

    def test_loads_order_four(self):
        """Assert semigroups of order 4 are correctly loaded"""
        order_4 = SemigroupLoader(Order.FOUR)
        self.assertEqual(order_4.order, Order.FOUR)
        self.assertIn(1, order_4.data.keys())
        self.assertIn(126, order_4.data.keys())
        self.assertNotIn(127, order_4.data.keys())
        for key, semigroup in order_4.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(4, semigroup.order)
            self.assertEqual(4, len(semigroup.table))

    def test_loads_order_five(self):
        """Assert semigroups of order 5 are correctly loaded"""
        order_5 = SemigroupLoader(Order.FIVE)
        self.assertEqual(order_5.order, Order.FIVE)
        self.assertIn(1, order_5.data.keys())
        self.assertIn(1160, order_5.data.keys())
        self.assertNotIn(1161, order_5.data.keys())
        for key, semigroup in order_5.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(5, semigroup.order)
            self.assertEqual(5, len(semigroup.table))

    def test_loads_order_six(self):
        """Assert semigroups of order 6 are correctly loaded"""
        order_6 = SemigroupLoader(Order.SIX)
        self.assertEqual(order_6.order, Order.SIX)
        self.assertIn(1, order_6.data.keys())
        self.assertIn(15973, order_6.data.keys())
        self.assertNotIn(15974, order_6.data.keys())
        for key, semigroup in order_6.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(6, semigroup.order)
            self.assertEqual(6, len(semigroup.table))

    @unittest.skip("Semigroups of order 7 not loaded yet.")
    def test_loads_order_seven(self):
        """Assert semigroups of order 7 are correctly loaded"""
        order_7 = SemigroupLoader(Order.SEVEN)
        self.assertEqual(order_7.order, Order.SEVEN)
        self.assertIn(1, order_7.data.keys())
        self.assertIn(15973, order_7.data.keys())
        self.assertNotIn(15974, order_7.data.keys())
        for key, semigroup in order_7.data.items():
            self.assertIsInstance(semigroup, Semigroup)
            self.assertEqual(key, semigroup.id)
            self.assertEqual(6, semigroup.order)
            self.assertEqual(6, len(semigroup.table))
    
