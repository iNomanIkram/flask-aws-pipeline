import unittest

def add(num1,num2):
    return num1 + num2

class TestAdd(unittest.TestCase):

    def test_add(self):
        result = add(10,5)
        self.assertEqual(result,15)

if __name__ == "__main__":
    unittest.main()