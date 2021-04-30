import unittest
import cube

class testCube(unittest.TestCase):
    def test_int(self):
        self.assertEqual(cube.cube(3), 27)
    def test_neg(self):
        self.assertEqual(cube.cube(-1), 1)
    def test_char(self):
        self.assertEqual(cube.cube('x'), 1)

if __name__ == "__main__":
    unittest.main()