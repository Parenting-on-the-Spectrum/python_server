import unittest
from main import your_function_to_test

class TestYourFunction(unittest.TestCase):
    def test_example(self):
        self.assertEqual(your_function_to_test(2, 3), 5)

if __name__ == '__main__':
    unittest.main()