# Unit Tests
import unittest
from palindrome import is_palindrome as function_to_test

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        """Test with an empty string."""
        self.assertTrue(function_to_test(""))

    def test_single_character(self):
        """Test with a single character."""
        self.assertTrue(function_to_test("a"))

    def test_palindrome(self):
        """Test with a palindrome word."""
        self.assertTrue(function_to_test("racecar"))

    def test_non_palindrome(self):
        """Test with a non-palindrome word."""
        self.assertFalse(function_to_test("hello"))

    def test_palindrome_with_spaces(self):
        """Test with a palindrome word with spaces."""
        self.assertTrue(function_to_test("A man a plan a canal Panama"))

    def test_palindrome_with_punctuation(self):
        """Test with a palindrome word with punctuation."""
        self.assertTrue(function_to_test("No 'x' in Nixon"))

    def test_case_insensitive(self):
        """Test case insensitivity."""
        self.assertTrue(function_to_test("RaceCar"))

    def test_non_alphanumeric_characters(self):
        """Test with non-alphanumeric characters."""
        self.assertTrue(function_to_test("madam, I'm Adam!"))

    def test_palindrome_with_numbers(self):
        """Test with a palindrome word with numbers."""
        self.assertTrue(function_to_test("12321"))

    def test_non_palindrome_with_numbers(self):
        """Test with a non-palindrome word with numbers."""
        self.assertFalse(function_to_test("12345"))

    def test_integer_input(self):
        """Test with an integer input."""
        with self.assertRaises(TypeError):
            function_to_test(123)

    def test_boolean_input(self):
        """Test with a boolean input."""
        with self.assertRaises(TypeError):
            function_to_test(True)

    def test_none_input(self):
        """Test with a None input."""
        with self.assertRaises(TypeError):
            function_to_test(None)

if __name__ == '__main__':
    unittest.main()


