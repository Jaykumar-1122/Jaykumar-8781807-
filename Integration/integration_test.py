import unittest
from integration_test import km_to_miles

class TestKmToMiles(unittest.TestCase):
    def test_positive_input(self):
        self.assertAlmostEqual(km_to_miles(1), 0.621371, places=6)
        self.assertAlmostEqual(km_to_miles(10), 6.21371, places=5)
        self.assertAlmostEqual(km_to_miles(100), 62.1371, places=4)

    def test_zero_input(self):
        self.assertEqual(km_to_miles(0), 0)

    def test_negative_input(self):
        self.assertAlmostEqual(km_to_miles(-1), -0.621371, places=6)
        self.assertAlmostEqual(km_to_miles(-10), -6.21371, places=5)
        self.assertAlmostEqual(km_to_miles(-100), -62.1371, places=4)

if __name__ == '__main__':
    unittest.main()
