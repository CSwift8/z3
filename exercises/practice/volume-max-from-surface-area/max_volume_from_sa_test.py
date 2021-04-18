import unittest
import math
from z3 import *
from max_volume_from_sa_example import *

NUM_DECIMAL_PLACES = 3

def truncate(value, num_decimal_places):
    shifted_value = value * (10 ** num_decimal_places)
    truncated_shifted_value = int(shifted_value)
    return truncated_shifted_value / (10 ** num_decimal_places)

def get_calculus_result(surface_area, precision):
    """
    Optimization result via calculus
    """
    side_length = math.sqrt(surface_area / 3)
    height = .25 * ((surface_area / side_length) - side_length)
    print(f"Expected Volume = {(side_length ** 2) * height}")
    print(f"Expected Surface Area = {(side_length ** 2) + (4 * side_length * height)}")
    return truncate(side_length, precision), truncate(height, precision)

class MaxVolumeFromSurfaceAreaTests(unittest.TestCase):

    def setUp(self):
        # Display rational numbers as decimals instead of fractions
        set_option(rational_to_decimal=True)

        # Set Precision to 5 decimal places of outputted rational numbers
        set_option(precision=NUM_DECIMAL_PLACES)

    def test_small_side_length_int_result(self):
        surface_area = 48
        expected_side_length, expected_height = get_calculus_result(surface_area, NUM_DECIMAL_PLACES)
        side_length, height = max_volume_from_sa(surface_area)
        self.assertEqual(side_length, expected_side_length)
        self.assertEqual(height, expected_height)

    def test_large_side_length_int_result1(self):
        surface_area = 192
        expected_side_length, expected_height = get_calculus_result(surface_area, NUM_DECIMAL_PLACES)
        side_length, height = max_volume_from_sa(surface_area)
        self.assertEqual(side_length, expected_side_length)
        self.assertEqual(height, expected_height)

    def test_large_side_length_int_result2(self):
        surface_area = 243
        expected_side_length, expected_height = get_calculus_result(surface_area, NUM_DECIMAL_PLACES)
        side_length, height = max_volume_from_sa(surface_area)
        self.assertEqual(side_length, expected_side_length)
        self.assertEqual(height, expected_height)

    def test_side_length_float_result(self):
        surface_area = 100
        expected_side_length, expected_height = get_calculus_result(surface_area, NUM_DECIMAL_PLACES)
        side_length, height = max_volume_from_sa(surface_area)
        self.assertEqual(side_length, expected_side_length)
        self.assertEqual(height, expected_height)

if __name__ == "__main__":
    unittest.main() 
