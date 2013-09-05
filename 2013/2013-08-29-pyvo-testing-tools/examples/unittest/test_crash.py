import unittest
from factory import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car.hit_wall(velocity=120)

    # def tearDown(self): pass

    def test_crash(self):
        self.assertFalse(self.car.is_damaged)

    def test_damage_report(self):
        self.assertEqual(100, self.car.damage)


if __name__ == '__main__':
    unittest.main()
