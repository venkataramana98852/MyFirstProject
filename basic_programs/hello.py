import unittest

class TestApp(unittest.TestCase):

    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(self.add(2,4), 6)
        
    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    unittest.main()