import unittest
from main import calculate_pi_to_5th_digit


class TestPiCalculation(unittest.TestCase):
    """Test cases for pi calculation to 5th digit."""
    
    def test_pi_to_5th_digit(self):
        """Test that pi is calculated correctly to the 5th decimal place."""
        pi = calculate_pi_to_5th_digit()
        
        # Pi to 5 decimal places is 3.14159
        # Allow a small tolerance for floating-point precision
        self.assertAlmostEqual(pi, 3.14159, places=5)
    
    def test_pi_greater_than_3(self):
        """Test that calculated pi is greater than 3."""
        pi = calculate_pi_to_5th_digit()
        self.assertGreater(pi, 3)
    
    def test_pi_less_than_4(self):
        """Test that calculated pi is less than 4."""
        pi = calculate_pi_to_5th_digit()
        self.assertLess(pi, 4)
    
    def test_pi_in_correct_range(self):
        """Test that pi falls in the expected range around 3.14159."""
        pi = calculate_pi_to_5th_digit()
        self.assertGreater(pi, 3.14)
        self.assertLess(pi, 3.15)


if __name__ == '__main__':
    print("Calculating pi to 5th digit...")
    pi_value = calculate_pi_to_5th_digit()
    print(f"Pi ≈ {pi_value}")
    print(f"Pi to 5 decimal places ≈ {pi_value:.5f}")
    print("\nRunning unit tests...\n")
    
    unittest.main(verbosity=2)
