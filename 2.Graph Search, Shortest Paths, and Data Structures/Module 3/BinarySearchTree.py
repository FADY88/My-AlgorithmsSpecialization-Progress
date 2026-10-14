class TreeNode:
  def __init__(self, key, parent = None, left = None, right = None):
    self.key = key
    self.parent = parent
    self.left = left
    self.right = right
    # augmenting the tree with the size of each node
    # size: how many nodes are reachable + 1 from given node
    self.size = 1 + self.ReachableNodes(self.left) + self.ReachableNodes(self.right)
    self.ParentReference()
  
  def ChangeParent(self, newParent): self.parent = newParent
  
  def ChangeLeft(self, newLeft): self.left = newLeft
  
  def ChangeRight(self, newRight): self.right = newRight

  def HasParent(self): return self.parent != None
  def HasLeft(self): return self.left != None
  def HasRight(self): return self.right != None
  
  def Parent(self): return self.parent
  
  def Left(self): return self.left
  
  def Right(self): return self.right
  
  def Size(self): return self.size
  
  def Key(self): return self.key
  
  def ReachableNodes(self, root):
    if root == None:
      return 0
    else:
      return 1 + self.ReachableNodes(root.Left()) + self.ReachableNodes(root.Right())
  
  def ParentReference(self):
    if self.HasLeft():
      self.Left().ChangeParent(self)
    if self.HasRight():
      self.Right().ChangeParent(self)
  
  # search for some key in a node, return that node if found, false otherwise
  def Search(self, k):
    if self.key == k:
      return self
    elif self.key > k and self.HasLeft():
      return self.left.Search(k)
    elif self.HasRight(): # and self.key < k:
      return self.right.Search(k)
    else:
      return False
  
  def Insert(self, k):
    if self.key > k:
      if self.HasLeft():
        self.left.Insert(k)
      else:
        # edit size 
        self.ChangeLeft(TreeNode(k, self))
        self.IncreaseSize()
    elif self.key <= k:
      if self.HasRight():
        self.right.Insert(k)
      else:
        # edit size 
        self.ChangeRight(TreeNode(k, self))
        self.IncreaseSize()
  
  def IncreaseSize(self):
    self.size += 1
    if self.HasParent():
      self.Parent().IncreaseSize()

  def DecreaseSize(self):
    self.size -= 1
    if self.HasParent():
      self.Parent().DecreaseSize()
  
  def __str__(self):
    string = f"{self.key}, size-> {self.size}: {None if not self.HasLeft() else str(self.Left().Key()).zfill(4)}   :   {None if not self.HasRight() else str(self.Right().Key()).zfill(4)}\n"
    if self.HasLeft():
      string += self.Left().__str__()
    if self.HasRight():
      string += self.Right().__str__()
    return string
  
  def Min(self):
    if not self.HasLeft():
      return self
    else:
      return self.Left().Min()

  def Max(self):
    if not self.HasRight():
      return self
    else:
      return self.Right().Max()
  
  # return the predecessor of k, if k not found or k is the smallest return False
  def Predecessor(self, k):
    node = self.Search(k)
    if not node: return False
    if node.HasLeft():
      return node.Left().Max()
    else:
      while node.HasParent():
        node = node.Parent()
        if node.Key() < k:
          return node
      return False

  # return the successor of k, if k not found or k is the largest return False
  def Successor(self, k):
    node = self.Search(k)
    if not node: return False
    if node.HasRight():
      return node.Right().Min()
    else:
      while node.HasParent():
        node = node.Parent()
        if node.Key() > k:
          return node
      return False
  
  def In_OrderTraversal(self):
    string = ""
    if self.HasLeft():
      string += self.Left().In_OrderTraversal()
    string += "  " + f"{self.Key()}" + "  "
    if self.HasRight():
      string += self.Right().In_OrderTraversal()
    return string.strip()
  
  def Delete(self, k, node = None):
    node = self.Search(k) if node == None else node
    # easy case
    if not (node.HasLeft() or node.HasRight()):
      node = node.Parent()
      if node.HasLeft() and node.Left().Key() == k:
        node.ChangeLeft(None)
        node.DecreaseSize()
        return
      if node.HasRight() and node.Right().Key() == k:
        node.ChangeRight(None)
        node.DecreaseSize()
        return
    # difficult case
    elif node.HasLeft() and node.HasRight():
      pred = self.Predecessor(k)
      pred.key, node.key = node.key, pred.key
      self.Delete(pred.key, pred)
    # medium case
    elif node.HasLeft():
      node.key = node.Left().Key()
      node.left = None
      node.DecreaseSize()
    elif node.HasRight():
      node.key = node.Right().Key()
      node.right = None
      node.DecreaseSize()
  
  def Select(self, i):
    a = 0 if not self.HasLeft() else self.Left().Size()
    if a == i - 1:
      return self.Key()
    elif a >= i:
      return self.Left().Select(i)
    elif a < i - 1 and self.HasRight():
      return self.Right().Select(i - a - 1)
    else: # Not found case
      return False
  
  def Rank(self, k):
    a = 0 if not self.HasLeft() else self.Left().Size()
    if self.Key() == k:
      return a + 1
    elif self.Key() > k and self.HasLeft():
      return self.Left().Rank(k)
    elif self.Key() < k and self.HasRight():
      rank = self.Right().Rank(k)
      if not rank:
        return False
      return a + 1 + rank
    else:
      return False
    

if __name__ == "__main__":
  t = TreeNode(3, None, TreeNode(1, None, None, (TreeNode(2))), TreeNode(5, None, TreeNode(4), None))
  print(t)
  print(t.In_OrderTraversal())
