import unittest
from heap import MinHeap

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()
        
    def test_return_min_value(self):
        self.heap.push(4)
        self.heap.push(3)
        self.heap.push(1)
        self.heap.push(5)
        self.assertEqual(self.heap.pop(),1)
        self.assertEqual(self.heap.pop(),3)