import unittest
import avg

class testAvg(unittest.TestCase):
    def test_nums(self):
        nums = [2,3,5,6,7,8,4]
        self.assertEqual(avg.avg(nums), 5)
    def test_char(self):
        nums = [2,3,4,5,'x', 7]
        self.assertFalse(avg.avg(nums), False)
    def test_empty(self):
        nums = []
        self.assertEqual(avg.avg(nums), 1)

if __name__ == "__main__":
    unittest.main()