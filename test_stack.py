import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  
  def setUp(self):
    self.stack = Stack()
  
  def testEmptyStack(self):
    self.assertEqual(self.stack.is_empty(), True)

  def testNotEmptyStack(self):
    self.stack.push(10)
    self.assertEqual(self.stack.is_empty(), False)

  def testSizeStack(self):
    self.stack.push(10)
    self.stack.push(20)
    self.stack.push(30)
    self.assertEqual(self.stack.size, 3)

  def testPushPopStack(self):
    self.stack.push(10)
    self.stack.push(20)
    self.stack.push(30)
    result = self.stack.pop()
    result = self.stack.pop()
    self.assertEqual(20, result)

  def testEmptyStackException(self):
    self.stack.push(10)
    result = self.stack.pop()
    with self.assertRaises(Exception):
      result = self.stack.pop()