import unittest, math

# edited version of BinarySearchTree from course 2 module 3 in Algorithms
class CodeTree:
  def __init__(self, left = None, right = None, label = None, frequency = None):
    self.label = label
    self.left = left
    self.right = right
    if frequency == None:
      self.frequency = self.left.Freq() + self.right.Freq()
    else:
      self.frequency = frequency
    # self.codeTable = {}
  
  def Label(self): return self.label
  
  def Left(self):  return self.left
  
  def Right(self): return self.right
  
  def Freq(self):  return self.frequency
  
  # I'm really proud of this method
  def Codes(self):
    def storeCodes(root, code = ""):
      if root.Label() != None:
        dictOfCode[root.Label()] = code
      else:
        storeCodes(root.Left(), code + "0")
        storeCodes(root.Right(), code + "1")
    
    dictOfCode = {}
    storeCodes(self)
    return dictOfCode



# Minimum heap class that holds CodeTrees
class MinHeap:
  def __init__(self, list = []):
    self.items = list
    self.heapifyList()
    # printing may code some issues due to printing class location
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
    while self.hasParent(index) and self.parent(index).Freq() > self.items[index].Freq():
      self.swap(index, self.parentIndex(index))
      index = self.parentIndex(index)
  
  def heapifyDown(self, index = 0):
    while self.hasLeftChild(index):
      smallerChildIndex = self.leftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index).Freq() < self.leftChild(index).Freq():
        smallerChildIndex = self.rightChildIndex(index)
      
      if self.items[index].Freq() < self.items[smallerChildIndex].Freq():
        break
      else:
        self.swap(index, smallerChildIndex)
      index = smallerChildIndex
  
  # heapify the whole list in O(n) time complexity
  def heapifyList(self):
    for i in range(len(self.items) // 2 - 1, -1, -1):
      self.heapifyDown(i)
  
  # with help from ChatGPT
  # printing may code some issues due to printing class location
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

# input : {labels l : frequency f, ...}
# output: {labels l : code c     , ...}
def HuffmanCodes(labels : dict):
  T = MinHeap()
  # populate T with leaves of the tree
  for l, f in labels.items():
    T.add(CodeTree(None, None, l, f))
  
  while len(T) > 1:
    small1 = T.poll()
    small2 = T.poll()
    T.add(CodeTree(small1, small2))
  
  return T.poll().Codes()


class TestHuffmanCodes(unittest.TestCase):
  def test2(self):
    d = {"A" : 60, "B" : 25, "C" : 10, "D" : 5}
    expected = {"A" : "1", "B" : "01", "C" : "001", "D" : "000"}
    self.assertEqual(HuffmanCodes(d), expected)

  def test1(self):
    d = {"A" : 3, "B" : 2, "C" : 6, "D" : 8, "E" : 2, "F" : 6}
    expected = {"A" : "100", "B" : "1010", "C" : "01", "D" : "11", "E" : "1011", "F" : "00"}
    self.assertEqual(HuffmanCodes(d), expected)

  def test3(self):
    d = {"A" : 1, "B" : 1, "C" : 1, "D" : 1}
    expected = {"A" : "00", "B" : "01", "D" : "10", "C" : "11"}
    self.assertEqual(HuffmanCodes(d), expected)

  def test4(self):
    d = {"A" : 7, "B" : 3, "C" : 2, "D" : 6, "E" : 1}
    expected = {"A" : "0", "B" : "110", "C" : "1111", "D" : "10", "E" : "1110"}
    self.assertEqual(HuffmanCodes(d), expected)

  def test5(self):
    d = {"A" : 5, "B" : 9, "C" : 12, "D" : 13, "E" : 16, "F" : 45}
    expected = {"A" : "1100", "B" : "1101", "C" : "100", "D" : "101", "E" : "111", "F" : "0"}
    self.assertEqual(HuffmanCodes(d), expected)


if __name__ == "__main__":
  unittest.main()