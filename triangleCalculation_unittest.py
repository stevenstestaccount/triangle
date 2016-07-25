
import unittest
from triangleCalculation import classifyTriangle as calc

class TriangleTest(unittest.TestCase):

    def test_nottriangle(self):
        self.assertEqual(calc(1, 1, 20), 'Invalid')
        self.assertEqual(calc(-1, -1, -1), 'Invalid')
        self.assertEqual(calc(3, 3, 6), 'Invalid')
        
    def test_inputs(self):
        self.assertEqual(calc(1, 1, 'a'), 'Invalid')
        self.assertEqual(calc(1, 'a', 1), 'Invalid')
        self.assertEqual(calc('a', 1, 1), 'Invalid')
        self.assertEqual(calc(1, 1, '1a'), 'Invalid')
        self.assertEqual(calc(1, '1a', 1), 'Invalid')
        self.assertEqual(calc('1a', 1, 1), 'Invalid')
        self.assertEqual(calc('1', '1', '1'), 'Invalid')
        
    def test_isosceles(self):
        self.assertEqual(calc(3, 3, 1), 'Isosceles')
        self.assertEqual(calc(3, 3, 2), 'Isosceles')
        self.assertEqual(calc(3, 3, 4), 'Isosceles')
        self.assertEqual(calc(3, 3, 5.99), 'Isosceles')
        self.assertEqual(calc(3, 3, 5.999999999999999), 'Isosceles', 'boundary one')        
        self.assertEqual(calc(3, 3, 5.9999999999999999), 'Isosceles', 'boundary two')
    
    def test_scalene(self):
        self.assertEqual(calc(9, 13, 14), 'Scalene')
        self.assertEqual(calc(14, 13, 9), 'Scalene')
        self.assertEqual(calc(13, 14, 9), 'Scalene')
    
    def test_equilateral(self):
        self.assertEqual(calc(1, 1, 1), 'Equilateral')
        self.assertEqual(calc(0.1, 0.1, 0.1), 'Equilateral')
        self.assertEqual(calc(969486, 969486,969486), 'Equilateral')
        self.assertEqual(calc(4294967294, 4294967294, 4294967294), 'Equilateral')
        self.assertEqual(calc(4294967295, 4294967295, 4294967295), 'Equilateral')

    
if __name__ == '__main__':
    unittest.main()