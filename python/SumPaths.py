#!/usr/bin/env python

import unittest

class TestSumPaths(unittest.TestCase):

  def testSanity(self):
    n1 = Node(value=1)
    self.assertEqual(n1.sumPaths(), 1)

  def testBasic(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    self.assertEqual(n1.sumPaths(), 29)

  def testBigger(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    n1.left.left = Node(3)
    n1.left.right = Node(7)
    self.assertEqual(n1.sumPaths(), 305)

  def testReadMe(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    n1.left.left = Node(3)
    n1.left.right = Node(7)
    n1.left.right.right = Node(9)
    self.assertEqual(n1.sumPaths(), 1637)

  def testExtra(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    n1.left.left = Node(3)
    n1.left.right = Node(7)
    n1.left.right.right = Node(9)
    n1.left.left.right = Node(2)
    self.assertEqual(n1.sumPaths(), 1637 + 1432 - 143)

  def testFull(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    n1.left.left = Node(3)
    n1.left.right = Node(7)
    n1.right.left = Node(2)
    n1.right.right = Node(8)
    self.assertEqual(n1.sumPaths(), 600)

  def testOneToNine(self):
    n1 = Node(value=1)
    n1.left = Node(4)
    n1.right = Node(5)
    n1.left.left = Node(3)
    n1.left.right = Node(7)
    n1.left.right.right = Node(9)
    n1.right.left = Node(2)
    n1.right.right = Node(8)
    n1.right.right.right = Node(6)
    self.assertEqual(n1.sumPaths(), 143 + 1479 + 152 + 1586)
  # Write some more test cases

class Node:
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  #Ran DFS and created new paths as it went along.
  #When no more children the current path is removed- 
  #and its value added to the current total.
  def sumPaths(self):
    # IMPLEMENT ME
    total = 0
    curr = 0
    roads = [""]
    stack = [self]
    while stack:
        #print(stack)
        node = stack.pop()
        val = str(node.value)
        roads[0] = roads[0] + val
        stack.extend(filter(None, [node.right, node.left]))
        if node.right is not None:
          if (node.left is not None):
            new_road = roads[0]
            prev_road = roads.pop(0)  
            roads = [prev_road, new_road] + roads
        if node.right is None and node.left is None:
          #print('enter')
          #print(roads)
          curr = roads.pop(0)
          #print(curr)
          #print(roads)
          total += int(curr) 
    return total
    
if __name__ == "__main__":
  unittest.main()
