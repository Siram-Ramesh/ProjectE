import EvenFibonacci as ef
import unittest

class MultipleFinderTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual(ef.sumEvenFibonacci(0), 0)

    def test_1(self):
        self.assertEqual(ef.sumEvenFibonacci(0), 0)

    def test_2(self):
        self.assertEqual(ef.sumEvenFibonacci(2), 2)

    def test_5(self):
        self.assertEqual(ef.sumEvenFibonacci(5), 2)

    def test_10(self):
        self.assertEqual(ef.sumEvenFibonacci(10), 10)

if __name__ == '__main__':
    unittest.main()