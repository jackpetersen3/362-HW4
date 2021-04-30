import unittest
import name

class test_name(unittest.TestCase):
    def test_name(self):
        first = "Jack"
        last = "Petersen"
        self.assertEqual(name.name(first, last), "Jack Petersen")
    def test_empty_last(self):
        first = "Jack"
        last = []
        self.assertEqual(name.name(first, last), "Jack Petersen")
    def test_empty_first(self):
        first = []
        last = "Petersen"
        self.assertEqual(name.name(first, last), "Jack Petersen")


if __name__ == "__main__":
    unittest.main()