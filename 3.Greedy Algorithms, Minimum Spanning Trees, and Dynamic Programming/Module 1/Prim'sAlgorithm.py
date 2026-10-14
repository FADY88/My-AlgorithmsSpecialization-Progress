import unittest

# Prim's minimum spanning tree algorithm
# graph G = {1 : [(node, weight), ...], ...}
# Minimum Spanning Tree (MST): is a subset of the edges of a connected,
# undirected graph that connects all the vertices with the most negligible possible total weight of the edges
# the function will output list of edges "tuples" [(node, node, length), ...]

def MST(G : dict, s):
  X = [s]
  mst = []
  while len(G) > len(X):
    newNode = None
    sourceNode = None
    length = 0
    for v in X:
      # loop over tuples of (node w, length l)
      for w, l in G[v]:
        if w not in X:
          if length == 0 or l < length:
            length = l
            newNode = w
            sourceNode = v
        
    if newNode == None: break
    X.append(newNode)
    mst.append((sourceNode, newNode, length))

  return mst

def MSTwithHeap(G : dict, s):
  X = [s]
  mst = []
  v_x = MinHeap([])
  v = s
  while len(G) > len(X):
    for node, length in G[v]:
      if node not in X:
        v_x.add((v, node, length))
    
    if not len(v_x): break
    # else block is executed when loop completes normally (i.e., without encountering a break statement).
    while len(v_x):
      u, w, l = v_x.poll()
      if w not in X: break
    else:
      break
    
    X.append(w)
    mst.append((u, w, l))
    v = w
  
  return mst

class TestMST(unittest.TestCase):
  def test_simple(self):
    G =  {"A" : [("B", 1), ("C", 3), ("D", 4)],
          "B" : [("A", 1), ("C", 2)],
          "C" : [("B", 2), ("A", 3), ("D", 5)],
          "D" : [("A", 4), ("C", 5)]}
    expected = [("A", "B", 1), ("B", "C", 2), ("A", "D", 4)]
    s = "A"
    self.assertEqual(MST(G, s), expected)
    self.assertEqual(MSTwithHeap(G, s), expected)
  
  def test_single_node(self):
    G = {1: []}
    expected = []
    s = 1
    self.assertEqual(MST(G, s), expected)
    self.assertEqual(MSTwithHeap(G, s), expected)

  def test_two_nodes(self):
    G = {1: [(2, 1)], 2: [(1, 1)]}
    expected = [(1, 2, 1)]
    s = 1
    self.assertEqual(MST(G, s), expected)
    self.assertEqual(MSTwithHeap(G, s), expected)

  def test_multiple_nodes(self):
    G = {1: [(2, 1), (3, 4)], 2: [(1, 1), (3, 2)], 3: [(1, 4), (2, 2)]}
    expected = [(1, 2, 1), (2, 3, 2)]
    s = 1
    self.assertEqual(MST(G, s), expected)
    self.assertEqual(MSTwithHeap(G, s), expected)

  def test_disconnected_graph(self):
    G = {1: [(2, 1)], 2: [(1, 1)], 3: [(4, 1)], 4: [(3, 1)]}
    expected = [(1, 2, 1)]
    s = 1
    self.assertEqual(MST(G, s = 1), expected)
    self.assertEqual(MSTwithHeap(G, s = 1), expected)
  
  def test_complicated(self):
    G =  {0: [(1, 9), (2, 5)],
          1: [(0, 9), (2, 9), (6, 3)],
          2: [(0, 5), (1, 9), (4, 9)],
          3: [],
          4: [(2, 9), (6, 7)],
          5: [(6, 7)],
          6: [(1, 3), (4, 7), (5, 7)],
          7: []}
    expected = [(0, 2, 5), (0, 1, 9), (1, 6, 3), (6, 4, 7), (6, 5, 7)]
    s = 0
    self.assertEqual(MST(G, s), expected)
    self.assertEqual(MSTwithHeap(G, s), expected)


# Minimum heap class that holds tuples (node, length)
class MinHeap:
  def __init__(self, list):
    self.items = list
  
  def leftChildIndex(self, parentIndex): return 2 * parentIndex + 1
  def rightChildIndex(self, parentIndex): return 2 * parentIndex + 2
  def parentIndex(self, childIndex): return (childIndex - 1) // 2
  
  def hasLeftChild(self, index): return self.leftChildIndex(index) < len(self.items)
  def hasRightChild(self, index): return self.rightChildIndex(index) < len(self.items)
  def hasParent(self, index): return self.parentIndex(index) >= 0
  
  def leftChild(self, index): return self.items[self.leftChildIndex(index)]
  def rightChild(self, index): return self.items[self.rightChildIndex(index)]
  def parent(self, index): return self.items[self.parentIndex(index)]
  
  def swap(self, indexOne, indexTwo):
    self.items[indexOne], self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]
  
  def __len__(self): return len(self.items)
  
  def peek(self):
    if len(self.items):
      return self.items[0]
    else:
      raise IndexError("Heap is empty")

  def poll(self):
    if not len(self.items):
      raise IndexError("Heap is empty")
    item = self.items[0]
    self.swap(len(self.items) - 1, 0)
    self.items.pop()
    self.heapifyDown()
    return item
  
  def add(self, item):
    """add element to the heap (node, length)"""
    self.items.append(item)
    self.heapifyUp()
  
  def heapifyUp(self):
    index = len(self.items) - 1
    while self.hasParent(index) and self.parent(index)[2] > self.items[index][2]:
      self.swap(index, self.parentIndex(index))
      index = self.parentIndex(index)
  
  def heapifyDown(self):
    index = 0
    while self.hasLeftChild(index):
      smallerChildIndex = self.leftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index)[2] < self.leftChild(index)[2]:
        smallerChildIndex = self.rightChildIndex(index)
      
      if self.items[index][2] < self.items[smallerChildIndex][2]:
        break
      else:
        self.swap(index, smallerChildIndex)
      index = smallerChildIndex



if __name__ == '__main__':
  unittest.main()
