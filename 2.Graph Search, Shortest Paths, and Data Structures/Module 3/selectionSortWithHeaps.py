import unittest, math

# Minimum heap class that holds numbers
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
    while self.hasParent(index) and self.parent(index) > self.items[index]:
      self.swap(index, self.parentIndex(index))
      index = self.parentIndex(index)
  
  def heapifyDown(self, index = 0):
    while self.hasLeftChild(index):
      smallerChildIndex = self.leftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
        smallerChildIndex = self.rightChildIndex(index)
      
      if self.items[index] < self.items[smallerChildIndex]:
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


class TestShortestPaths(unittest.TestCase):
    def test1(self):
        l = [64, 15, 3, 71, 88, 59, 57, 8, 61, 65]
        expected = sorted(l)
        self.assertEqual(SelectionSort(l), expected)

    def test2(self):
        l = [14, 21, 20, 39, 77, 84, 100, 13, 65, 56]
        expected = sorted(l)
        self.assertEqual(SelectionSort(l), expected)

    def test3(self):
        l = [37, -38, -19, 23, -1, -47, -38, -11, 36, -30]
        expected = sorted(l)
        self.assertEqual(SelectionSort(l), expected)

    def test4(self):
        l = [-28, -25, 13, 1, 39, 32, 2, 1, -47, -4]
        expected = sorted(l)
        self.assertEqual(SelectionSort(l), expected)

# selection sort normally is O(n**2) but after using min heap
# it's O(log n)
def SelectionSort(l):
  h = MinHeap(l)
  l_sorted = []
  while len(h):
    l_sorted.append(h.poll())
  return l_sorted

if __name__ == '__main__':
  l = [1, 9, 2, 13, 10, 5, 3, 15, 14, 11, 21, 7, 6, 4, 17, 16, 24, 28, 23, 12, 22, 27, 30, 8, 20, 26, 19, 31, 18, 25, 29]
  h = MinHeap(l)
  print(h)
  
  unittest.main()
