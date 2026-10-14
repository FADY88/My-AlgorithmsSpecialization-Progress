import unittest, math

# Minimum heap class that holds tuples (node, length)
class MinHeap:
  def __init__(self, list = []):
    self.items = list
    self.heapifyList()
    self.MaxPrintingSize = 2
  
  def ChangePrintingSize(self, newSize):
    self.MaxPrintingSize = newSize
  
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
    while self.hasParent(index) and self.parent(index)[1] > self.items[index][1]:
      self.swap(index, self.parentIndex(index))
      index = self.parentIndex(index)
  
  def heapifyDown(self, index = 0):
    while self.hasLeftChild(index):
      smallerChildIndex = self.leftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index)[1] < self.leftChild(index)[1]:
        smallerChildIndex = self.rightChildIndex(index)
      
      if self.items[index][1] < self.items[smallerChildIndex][1]:
        break
      else:
        self.swap(index, smallerChildIndex)
      index = smallerChildIndex
  
  # heapify the whole list in O(n) time complexity
  def heapifyList(self):
    for i in range(len(self.items) // 2 - 1, -1, -1):
      self.heapifyDown(i)

# with help from ChatGPT
  def __str__(self):
    """Prints the heap in a tree-like structure."""
    if not self.items:
      return "Heap is empty."

    n = len(self.items)
    levels = math.floor(math.log2(n)) + 1  # Calculate number of levels in the heap

    index = 0
    numberSpace = " " * self.MaxPrintingSize
    result = ""
    for level in range(levels):
      num_nodes = 2 ** level  # Number of nodes at this level
      nodes = self.items[index : min(index + num_nodes, n)]  # Get nodes at this level
      spaceCount = 2 ** (levels - level) // 2 - 1
      space = (" " + numberSpace) * spaceCount  # Space formatting for visualization
      result += space
      if not space:
        space = "  " + numberSpace
      
      spaceBetween = space if level + 1 == levels else (space + " ") * 2 + numberSpace
      
      for i in range(len(nodes)):
        result += str(nodes[i]).zfill(self.MaxPrintingSize)
        if i != len(nodes) - 1:
          result += spaceBetween
      result += "\n"
      index += num_nodes
    return result

# graph = {node : [(node, length), ...], ...}
# x: visited nodes, v_x: not visited nodes
# B: shortest path from s to node is not accurate in this implementation
# because each node doesn't know the previous node
def Dijkstra(G, s):
  X = [s]
  A = {s: 0}
  v_x = MinHeap([])
  v = s
  while len(G) > len(X):
    for node, length in G[v]:
      if node not in X:
        v_x.add((node, A[v] + length))
        
    if not len(v_x): break
    while len(v_x):
      w, l = v_x.poll()
      if w not in X: break
    else:
      break
    
    X.append(w)
    A[w] = l
    v = w
  return A


class TestDijkstra(unittest.TestCase):
    def test_single_node(self):
        G = {1: []}
        s = 1
        expected = {1: 0}
        self.assertEqual(Dijkstra(G, s), expected)

    def test_two_nodes(self):
        G = {1: [(2, 1)], 2: []}
        s = 1
        expected = {1: 0, 2: 1}
        self.assertEqual(Dijkstra(G, s), expected)

    def test_multiple_nodes(self):
        G = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: []}
        s = 1
        expected = {1: 0, 2: 1, 3: 3}
        self.assertEqual(Dijkstra(G, s), expected)

    def test_disconnected_graph(self):
        G = {1: [(2, 1)], 2: [], 3: [(4, 1)], 4: []}
        s = 1
        expected = {1: 0, 2: 1}
        self.assertEqual(Dijkstra(G, s), expected)


if __name__ == '__main__':
    G = {0 : [(2, 3), (4, 9)], 1 : [(0, 6), (3, 6), (6, 8)], 2: [(4, 6), (5, 9)], 3: [], 4: [(2, 7), (7, 6)], 5: [(1, 4), (7, 5)], 6: [(4, 5), (5, 7)], 7: []}
    s = 0
    print(Dijkstra(G, s))
    print({0: 0, 2: 3, 4: 9, 5: 12, 7: 15, 1: 16, 3: 22, 6: 24})
    unittest.main()
