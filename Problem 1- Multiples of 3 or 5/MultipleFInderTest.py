import MultipleFinder as mf
import unittest

class TestStringMethods(unittest.TestCase):

    def test_35_boundIs0(self):
        self.assertEqual(mf.sumMultiples(0, [3,5]), 0)

    def test_35_boundIs1(self):
        self.assertEqual(mf.sumMultiples(1, [3,5]), 0)

    def test_35_boundIs9(self):
        self.assertEqual(mf.sumMultiples(9, [3,5]), 14)
    
    def test_35_boundIs10(self):
        self.assertEqual(mf.sumMultiples(10, [3,5]), 23)

    def test_35_boundIs11(self):
        self.assertEqual(mf.sumMultiples(11, [3,5]), 33)

    def test_35_boundIsPrimePlus1(self):
        self.assertEqual(mf.sumMultiples(14, [3,5]), 45)

    def test_23_inclusionExclusionPrincipleSimple(self):
        self.assertEqual(mf.sumMultiples(7, [3,2]), 15)

    def test_23_inclusionExclusionPrinciple(self):
        self.assertEqual(mf.sumMultiples(15, [3,2]), 68)
        # 2, 3, 4, 6, 8, 9, 10, 12, 14 = 68

    def test_35_1000(self):
        answer = mf.sumMultiples(1000, [3,5])
        print(answer)
        self.assertEqual(answer, 233168)

if __name__ == '__main__':
    unittest.main()