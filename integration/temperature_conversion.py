import unittest
from temperature_conversion import temperature

class TempConversion(unittest.TestCase):
    def test_temperature(self):
        # Test freezing point of water
        self.assertAlmostEqual(temperature(0), 32, places=2)
        # Test boiling point of water
        self.assertAlmostEqual(temperature(100), 212, places=2)
        # Test below freezing point
        self.assertAlmostEqual(temperature(-10), 14, places=2)
        # Test above freezing point
        self.assertAlmostEqual(temperature(25), 77, places=2)

if __name__ == '__main__':
    unittest.main()
