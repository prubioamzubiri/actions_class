import unittest
import io
import sys
from main import calculate_sum, create_list, reverse_list, main


class TestMainFunctions(unittest.TestCase):
    
    def test_calculate_sum(self):
        """Test the calculate_sum function"""
        self.assertEqual(calculate_sum(10, 20), 30)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(-5, 5), 0)
        self.assertEqual(calculate_sum(-10, -20), -30)
    
    def test_create_list(self):
        """Test the create_list function"""
        self.assertEqual(create_list(5), [0, 2, 4, 6, 8])
        self.assertEqual(create_list(0), [])
        self.assertEqual(create_list(3), [0, 2, 4])
        self.assertEqual(create_list(1), [0])
    
    def test_reverse_list(self):
        """Test the reverse_list function"""
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1]), [1])
        self.assertEqual(reverse_list([0, 2, 4, 6, 8]), [8, 6, 4, 2, 0])
    
    def test_main_output(self):
        """Test the main function output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        main()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Hello, World!", output)
        self.assertIn("The sum is: 30", output)
        self.assertIn("Created list: [0, 2, 4, 6, 8]", output)
        self.assertIn("Reversed list: [8, 6, 4, 2, 0]", output)
        
        # Verify counting output
        for i in range(5):
            self.assertIn(f"Counting: {i}", output)


if __name__ == "__main__":
    unittest.main()
