import unittest

# Kruskal's minimum spanning tree algorithm
# graph G = {1 : [(node, weight), ...], ...}
# Minimum Spanning Tree (MST): is a subset of the edges of a connected,
# undirected graph that connects all the vertices with the most negligible possible total weight of the edges
# the function will output list of edges "tuples" [(node, node, length), ...]

# source of UnionFind class: ChatGPT
class UnionFind:
    def __init__(self, vertices = []):
        self.parent = {v:v for v in vertices}  # Maps each vertex to its parent
        self.rank =   {v:0 for v in vertices}  # Stores rank of each vertex

    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:  # Merge only if they are in different sets
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # Increase rank if equal

    def connected(self, x, y):
        """Check if two vertices are in the same set"""
        return self.find(x) == self.find(y)

    def add(self, x):
        """Dynamically add a vertex if it's not already present"""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1


def KruskalMST(G : dict):
  seen = set()
  edges = []
  for v in G:
    for u, w in G[v]:
      if u not in seen:
        edges.append((v, u, w))
  # sort according to weight of each edge
  edges.sort(key=lambda x: x[2])
  mst = []
  uf = UnionFind(G.keys())
  for n1, n2, w in edges:
    if not uf.connected(n1, n2):
      uf.union(n1, n2)
      mst.append((n1, n2, w))
  return mst


class TestMST(unittest.TestCase):
  def test_main(self):
    G =  {1 : [(2, 1), (3, 7)],
          2 : [(1, 1), (3, 5), (5, 6), (5, 3)],
          3 : [(1, 7), (2, 5), (5, 6)],
          4 : [(2, 4), (5, 2)],
          5 : [(2, 3), (3, 6), (4, 2)]}
    expected = [(1, 2, 1), (4, 5, 2), (2, 5, 3), (2, 3, 5)]
    self.assertEqual(KruskalMST(G), expected)
  
  def test_simple(self):
    G =  {"A" : [("B", 1), ("C", 3), ("D", 4)],
          "B" : [("A", 1), ("C", 2)],
          "C" : [("B", 2), ("A", 3), ("D", 5)],
          "D" : [("A", 4), ("C", 5)]}
    expected = [("A", "B", 1), ("B", "C", 2), ("A", "D", 4)]
    self.assertEqual(KruskalMST(G), expected)
  
  def test_single_node(self):
    G = {1: []}
    expected = []
    self.assertEqual(KruskalMST(G), expected)

  def test_two_nodes(self):
    G = {1: [(2, 1)], 2: [(1, 1)]}
    expected = [(1, 2, 1)]
    self.assertEqual(KruskalMST(G), expected)

  def test_multiple_nodes(self):
    G = {1: [(2, 1), (3, 4)], 2: [(1, 1), (3, 2)], 3: [(1, 4), (2, 2)]}
    expected = [(1, 2, 1), (2, 3, 2)]
    self.assertEqual(KruskalMST(G), expected)

  def test_disconnected_graph(self):
    G = {1: [(2, 1)], 2: [(1, 1)], 3: [(4, 1)], 4: [(3, 1)]}
    expected = [(1, 2, 1), (3, 4, 1)]
    self.assertEqual(KruskalMST(G), expected)
  
  def test_complicated(self):
    G =  {0: [(1, 9), (2, 5)],
          1: [(0, 9), (2, 9), (6, 3)],
          2: [(0, 5), (1, 9), (4, 9)],
          3: [],
          4: [(2, 9), (6, 7)],
          5: [(6, 7)],
          6: [(1, 3), (4, 7), (5, 7)],
          7: []}
    expected = [(1, 6, 3), (0, 2, 5), (4, 6, 7), (5, 6, 7), (0, 1, 9)]
    self.assertEqual(KruskalMST(G), expected)

  def test_more_complicated(self):
    G =  {0: [(1, 4), (7, 8)],
          1: [(0, 4), (2, 8), (7, 11)],
          2: [(1, 8), (3, 7), (5, 4), (8, 2)],
          3: [(2, 7), (4, 9), (5, 14)],
          4: [(3, 9), (5, 10)],
          5: [(2, 4), (3, 14), (4, 10), (6, 2)],
          6: [(5, 2), (7, 1), (8, 6)],
          7: [(0, 8), (1, 11), (6, 1), (8, 7)],
          8: [(2, 2), (6, 6), (7, 7)]}
    expected = [(6, 7, 1), (2, 8, 2), (5, 6, 2), (0, 1, 4), (2, 5, 4), (2, 3, 7), (0, 7, 8), (3, 4, 9)]
    self.assertEqual(KruskalMST(G), expected)
  
  
if __name__ == '__main__':
  unittest.main()