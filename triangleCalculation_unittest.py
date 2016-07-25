
import unittest
from triangleCalculation import classifyTriangle as calc

class TriangleTest(unittest.TestCase):

    def test_nottriangle(self):
        self.assertEqual(calc(1, 1, 20), '')
    
    def test_inputs(self):
        self.assertEqual(calc(1, 1, "a"), "")
        self.assertEqual(calc(1, "a", 1), "")
        self.assertEqual(calc("a", 1, 1), "")
    
    def test_isosceles(self):
        self.assertEqual(calc(3, 3, 1), "Isosceles")
        self.assertEqual(calc(3, 3, 2), "Isosceles")
        self.assertEqual(calc(3, 3, 4), "Isosceles")
    
    def test_scalene(self):
        pass
    
    def test_equilateral(self):
        self.assertEqual(calc(1, 1, 1), "Equilateral")
        self.assertEqual(calc(0.1, 0.1, 0.1), "Equilateral")
        self.assertEqual(calc(969486, 969486,969486), "Equilateral") 
    
if __name__ == "__main__":
    unittest.main()