import unittest
from BinarySearchTree import TreeNode

# FILE: test_BinarySearchTree.py


class TestBinarySearchTree(unittest.TestCase):
  
  def setUp(self):
    self.tree = TreeNode(3, None, TreeNode(1, None, None, TreeNode(2)), TreeNode(5, None, TreeNode(4), None))
  
  def test_search_existing(self):
    self.assertEqual(self.tree.Search(3), self.tree)
    self.assertEqual(self.tree.Search(1).Key(), 1)
    self.assertEqual(self.tree.Search(2).Key(), 2)
    self.assertEqual(self.tree.Search(4).Key(), 4)
    self.assertEqual(self.tree.Search(5).Key(), 5)
  
  def test_search_non_existing(self):
    self.assertFalse(self.tree.Search(0))
    self.assertFalse(self.tree.Search(6))
  
  def test_insert(self):
    print("Insert")
    print(self.tree)
    self.assertEqual(self.tree.In_OrderTraversal(), "1  2  3  4  5")
    self.tree.Insert(6)
    print(self.tree)
    self.assertEqual(self.tree.In_OrderTraversal(), "1  2  3  4  5  6")
    self.assertEqual(self.tree.Search(6).Key(), 6)
    self.tree.Insert(0)
    print(self.tree)
    self.assertEqual(self.tree.In_OrderTraversal(), "0  1  2  3  4  5  6")
    self.assertEqual(self.tree.Search(0).Key(), 0)
    self.tree.Insert(3)  # inserting duplicate
    print(self.tree)
    self.assertEqual(self.tree.In_OrderTraversal(), "0  1  2  3  3  4  5  6")
    self.assertEqual(self.tree.Search(3).Key(), 3)
  
  def test_max(self):
    self.assertEqual(self.tree.Max().Key(), 5)
    self.tree.Insert(6)
    self.assertEqual(self.tree.Max().Key(), 6)
    
  def test_min(self):
    self.assertEqual(self.tree.Min().Key(), 1)
    self.tree.Insert(0)
    self.assertEqual(self.tree.Min().Key(), 0)
  
  def test_predecessor(self):
    self.assertEqual(self.tree.Predecessor(3).Key(), 2)
    self.assertEqual(self.tree.Predecessor(4).Key(), 3)
    self.assertFalse(self.tree.Predecessor(1))
    
  def test_successor(self):
    self.assertEqual(self.tree.Successor(3).Key(), 4)
    self.assertEqual(self.tree.Successor(2).Key(), 3)
    self.assertFalse(self.tree.Successor(5))
  
  def test_delete(self):
    print("Delete")
    print(self.tree)
    self.tree.Delete(3)
    print(self.tree)
    self.assertFalse(self.tree.Search(3))
    self.assertEqual(self.tree.In_OrderTraversal(), "1  2  4  5")
    self.tree.Delete(1)
    print(self.tree)
    self.assertFalse(self.tree.Search(1))
    self.assertEqual(self.tree.In_OrderTraversal(), "2  4  5")
    self.tree.Delete(5)
    print(self.tree)
    self.assertFalse(self.tree.Search(5))
    self.assertEqual(self.tree.In_OrderTraversal(), "2  4")
  
  def test_select(self):
    self.assertEqual(self.tree.Select(1), 1)
    self.assertEqual(self.tree.Select(2), 2)
    self.assertEqual(self.tree.Select(3), 3)
    self.assertEqual(self.tree.Select(4), 4)
    self.assertEqual(self.tree.Select(5), 5)
    self.assertFalse(self.tree.Select(6))
    self.tree.Insert(20)
    self.assertEqual(self.tree.Select(6), 20)
  
  def test_rank(self):
    self.assertEqual(self.tree.Rank(1), 1)
    self.assertEqual(self.tree.Rank(2), 2)
    self.assertEqual(self.tree.Rank(3), 3)
    self.assertEqual(self.tree.Rank(4), 4)
    self.assertEqual(self.tree.Rank(5), 5)
    self.assertFalse(self.tree.Rank(6))
    self.tree.Insert(20)
    self.assertEqual(self.tree.Rank(20), 6)

if __name__ == '__main__':
  unittest.main()