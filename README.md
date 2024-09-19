Examples for Session 2 of Software Testing

Explanation:

    Import unittest: We import the unittest module for creating test cases.

    Create a test class: We define a class TestPalindrome that inherits from unittest.TestCase.

    Define test methods: Each test method represents a specific test scenario. The methods are named using the pattern test_* to indicate that they are test methods.

    Use assertions: Inside each test method, we use assertion methods from unittest.TestCase (e.g., assertTrue, assertFalse) to check the expected outcome.

    Test various scenarios: The tests cover cases like:

        Empty string

        Single character

        Palindrome word

        Non-palindrome word

        Palindrome with spaces

        Palindrome with punctuation

        Case insensitivity

        Non-alphanumeric characters

        Palindrome with numbers

        Non-palindrome with numbers

        Really Bad input (3 cases) wrong types, None, etc. Also illustrates how to test for expected exceptions.

    Run the tests: Finally, we use unittest.main() to execute the test suite. This will run all the test methods and report the results.
 