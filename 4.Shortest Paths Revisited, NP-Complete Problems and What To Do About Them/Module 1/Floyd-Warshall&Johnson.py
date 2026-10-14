import unittest
from shortestPathAgain import bellman_ford
from Dijkstra_Algorithm import Dijkstra
# all-pairs shortest path algorithm
# Floyd-Warshall algorithm

# input is a graph G and a source node s
# G = {node: [(neighbor, weight), ...], ...}

INF = float('inf')

def floyd_warshall(G):
  """
  G: Dictionary representing the graph {node: [(neighbor, weight), ...], ...}
  V: Number of vertices
  source: The starting node for shortest path computation
  """
  # Initialize distances: INF for all except source
  INF = float('inf')
  A = {u: {v: INF for v in G} for u in G}
  for u in G:
    A[u][u] = 0
    for v, w in G[u]:
      A[u][v] = w
  # Relax all edges V-1 times
  for k in G:  # For each node k
    for u in G:  # For each node u
      for v in G:  # For each node v
        A[u][v] = min(A[u][v], A[u][k] + A[k][v])
  return A

# great algorithm
def Johnson(G):
  vertices = list(G.keys())
  t = "tmp"
  G[t] = [] # new vertex
  # remove tmp from the loop
  for v in vertices:
    G[t].append((v, 0)) # new edges with weights 0 to every other vertex
  # one call to bellman-ford to get shortest path from t to every vertex
  lengths = bellman_ford(G, t)
  if type(lengths) is str:
    return lengths
  
  del G[t]
  # reweighting
  for u in G:
    newList = []
    for i in range(len(G[u])):
      newList.append((G[u][i][0], G[u][i][1] + lengths[u] - lengths[G[u][i][0]]))
    G[u] = newList
  # finally the All-Pairs paths using Dijkstra's algorithm
  pairPaths = {v : Dijkstra(G, v) for v in G}
  
  # get rid of pu + pv to get the pairPaths of the original Graph
  for u in pairPaths:
    for v in pairPaths[u]:
      pairPaths[u][v] += - lengths[u] + lengths[v]
  
  return pairPaths

# let's test it
class TestShortestPaths(unittest.TestCase):
  # MY implementation of Dijkstra's algorithm doesn't output unreachable nodes paths as INF
  def test_main(self):
    G =  {"s": [("v", 2), ("x", 4)],
          "v": [("w", 2), ("x", 1)],
          "x": [("t", 4)],
          "w": [("t", 2)],
          "t": []}
    expected = {'s': {'s': 0, 'v': 2, 'x': 3, 'w': 4, 't': 6},
                'v': {'s': INF, 'v': 0, 'x': 1, 'w': 2, 't': 4},
                'x': {'s': INF, 'v': INF, 'x': 0, 'w': INF, 't': 4},
                'w': {'s': INF, 'v': INF, 'x': INF, 'w': 0, 't': 2},
                't': {'s': INF, 'v': INF, 'x': INF, 'w': INF, 't': 0}}
    johnson_expected = {'s': {'s': 0, 'v': 2, 'x': 3, 'w': 4, 't': 6},
                        'v': {'v': 0, 'x': 1, 'w': 2, 't': 4},
                        'x': {'x': 0, 't': 4},
                        'w': {'w': 0, 't': 2},
                        't': {'t': 0}}
    self.assertEqual(floyd_warshall(G), expected)
    self.assertEqual(Johnson(G), johnson_expected)
  
  def test_main2(self):
    G =  {0: [(1, 6), (2, 7)],
          1: [(2, 8), (3, 5), (4, -4)],
          2: [(3, -3)],
          3: [(4, 9)],
          4: []}
    expected = {0: {0: 0, 1: 6, 2: 7, 3: 4, 4: 2},
                1: {0: INF, 1: 0, 2: 8, 3: 5, 4: -4},
                2: {0: INF, 1: INF, 2: 0, 3: -3, 4: 6},
                3: {0: INF, 1: INF, 2: INF, 3: 0, 4: 9},
                4: {0: INF, 1: INF, 2: INF, 3: INF, 4: 0}}
    
    johnson_expected = {0: {0: 0, 4: 2, 3: 4, 1: 6, 2: 7},
                        1: {1: 0, 4: -4, 3: 5, 2: 8},
                        2: {2: 0, 4: 6, 3: -3},
                        3: {3: 0, 4: 9},
                        4: {4: 0}}
    self.assertEqual(floyd_warshall(G), expected)
    self.assertEqual(Johnson(G), johnson_expected)
    
  def test_single_node(self):
    G = {1: []}
    expected = {1: {1: 0}}
    self.assertEqual(floyd_warshall(G), expected)
    self.assertEqual(Johnson(G), expected)

if __name__ == "__main__":
    unittest.main()