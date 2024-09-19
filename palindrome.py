def is_palindrome(word):
    """
    Checks whether a word is a palindrome.

    Args:
    word: The word to check.

    Returns:
    True if the word is a palindrome, False otherwise.
    """

    # Convert the word to lowercase and remove non-alphanumeric characters.
    word = "".join(char.lower() for char in word if char.isalnum())

    # Check if the word is the same forwards and backwards.
    return word == word[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))  # False
    print("Expecting True False above")
    