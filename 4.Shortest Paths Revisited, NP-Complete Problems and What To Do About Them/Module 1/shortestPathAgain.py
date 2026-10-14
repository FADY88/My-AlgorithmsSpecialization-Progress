import unittest
# here we go again with the shortest path problem
# this time we will use the Bellman-Ford algorithm to solve it while allowing negative weights
# but no negative cycles

# input is a graph G and a source node s
# G = {node: [(neighbor, weight), ...], ...}

# I got help from Copilot to write this code
def bellman_ford(G, s):
  """
  G: Dictionary representing the graph {node: [(neighbor, weight), ...], ...}
  V: Number of vertices
  source: The starting node for shortest path computation
  """
  # Initialize distances: INF for all except source
  INF = float('inf')
  A = {node: INF for node in G}
  A[s] = 0
  B = {s: []} # shortest path from s to node (should not be in real implementation)
  # Relax all edges V-1 times
  finished = False
  for _ in range(len(G) - 1):
    if finished: break
    finished = True
    for u in G:  # For each node u
      for v, w in G[u]:  # For each neighbor v of u
        if A[u] != INF and A[u] + w < A[v]:
          finished = False
          A[v] = A[u] + w
          B[v] = B[u] + [v]
  # Check for negative cycles
  for u in G:  # For each node u
    for v, w in G[u]:  # For each neighbor v of u
      if A[u] != INF and A[u] + w < A[v]:
        return f"Graph contains a negative cycle involving {u} -> {v}"
  # print(B)
  return A



# let's test it
class TestShortestPaths(unittest.TestCase):
    def test_main(self):
        G =  {"s": [("v", 2), ("x", 4)],
              "v": [("w", 2), ("x", 1)],
              "x": [("t", 4)],
              "w": [("t", 2)],
              "t": []}
        s = "s"
        expected = {'s': 0, 'v': 2, 'x': 3, 'w': 4, 't': 6}
        self.assertEqual(bellman_ford(G, s), expected)
    
    def test_main2(self):
        G =  {0: [(1, 6), (2, 7)],
              1: [(2, 8), (3, 5), (4, -4)],
              2: [(3, -3)],
              3: [(4, 9)],
              4: []}
        s = 0
        expected = {0: 0, 1: 6, 2: 7, 3: 4, 4: 2}
        self.assertEqual(bellman_ford(G, s), expected)
        
    def test_single_node(self):
        G = {1: []}
        s = 1
        expected = {1: 0}
        self.assertEqual(bellman_ford(G, s), expected)

    def test_two_nodes(self):
        G = {1: [(2, 1)], 2: []}
        s = 1
        expected = {1: 0, 2: 1}
        self.assertEqual(bellman_ford(G, s), expected)

    def test_multiple_nodes(self):
        G = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: []}
        s = 1
        expected = {1: 0, 2: 1, 3: 3}
        self.assertEqual(bellman_ford(G, s), expected)

    def test_disconnected_graph(self):
        G = {1: [(2, 1)], 2: [], 3: [(4, 1)], 4: []}
        s = 1
        expected = {1: 0, 2: 1, 3: float('inf'), 4: float('inf')}
        self.assertEqual(bellman_ford(G, s), expected)
    
    def test_negative_cycle(self):
        G = {1: [(2, 1)], 2: [(3, -5), (5, 2)], 3: [(4, 3)], 4: [(2, 1)], 5: []}
        s = 1
        expected = "Graph contains a negative cycle involving 2 -> 3"
        self.assertEqual(bellman_ford(G, s), expected)

if __name__ == "__main__":
  G =  {"s": [("v", 2), ("x", 4)],
              "v": [("w", 2), ("x", 1)],
              "x": [("t", 4)],
              "w": [("t", 2)],
              "t": []}
  s = "s"
  print(bellman_ford(G, s))
  unittest.main()