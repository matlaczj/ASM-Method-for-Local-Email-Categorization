import difflib
import string
import unittest
from typing import List, Tuple


def strip_punctuation(input_string: str) -> str:
    return input_string.translate(str.maketrans("", "", string.punctuation))


def enumerate_and_format_string_list(string_list):
    return "\n".join(f"{i+1}. {string}" for i, string in enumerate(string_list))


def find_closest_match(target, string_list):
    return (difflib.get_close_matches(target, string_list, n=1, cutoff=0) or [None])[0]


def clean_and_split_categories(
    actual_category: str, possible_categories: str
) -> Tuple[str, List[str]]:
    actual_category = actual_category.replace(" ", "").lower()
    possible_categories = (
        possible_categories.replace(" ", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .lower()
        .split(",")
    )
    return actual_category, possible_categories


class TestUtils(unittest.TestCase):
    def test_strip_punctuation(self):
        self.assertEqual(strip_punctuation("Hello, World!"), "Hello World")
        self.assertEqual(strip_punctuation("No. Punctuation!"), "No Punctuation")
        self.assertEqual(strip_punctuation("Punctuation?"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation."), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation,"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation;"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation:"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation!"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation-"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation("), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation)"), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation["), "Punctuation")
        self.assertEqual(strip_punctuation("Punctuation]"), "Punctuation")

    def test_enumerate_and_format_string_list(self):
        self.assertEqual(
            enumerate_and_format_string_list(["apple", "banana", "cherry"]),
            "1. apple\n2. banana\n3. cherry",
        )
        self.assertEqual(enumerate_and_format_string_list([]), "")
        self.assertEqual(enumerate_and_format_string_list(["apple"]), "1. apple")
        self.assertEqual(
            enumerate_and_format_string_list(["apple", "banana"]), "1. apple\n2. banana"
        )
        self.assertEqual(
            enumerate_and_format_string_list(["apple", "banana", "cherry", "durian"]),
            "1. apple\n2. banana\n3. cherry\n4. durian",
        )

    def test_find_closest_match(self):
        self.assertEqual(
            find_closest_match("appel", ["apple", "banana", "cherry"]), "apple"
        )
        self.assertEqual(
            find_closest_match("banana", ["apple", "banana", "cherry"]), "banana"
        )
        self.assertEqual(
            find_closest_match("cherry", ["apple", "banana", "cherry"]), "cherry"
        )

    def test_clean_and_split_categories(self):
        self.assertEqual(
            clean_and_split_categories(
                " Actual Category ", "['Possible Category 1', 'Possible Category 2']"
            ),
            ("actualcategory", ["possiblecategory1", "possiblecategory2"]),
        )
        self.assertEqual(
            clean_and_split_categories(
                "ACTUAL", "['POSSIBLE1', 'POSSIBLE2', 'POSSIBLE3']"
            ),
            ("actual", ["possible1", "possible2", "possible3"]),
        )
        self.assertEqual(
            clean_and_split_categories("actual", "['possible']"),
            ("actual", ["possible"]),
        )


if __name__ == "__main__":
    unittest.main()
