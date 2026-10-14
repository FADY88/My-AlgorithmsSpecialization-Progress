# the representation of graphs and the implementation of graph search algorithms
# graph with nodes [1, 2, 3, 4] and edges [(1, 2), (1, 3), (2, 3), (3, 4)]
# will be represented as a dictionary {1: [2, 3], 2: [3], 3: [4], 4: []}

# Breadth-first search on graph G and start node s
# if want to search for some node x, take it as an argument
# if if v == x: return True
def BFS(G, s):
  explored = [s]
  q = [s]
  while len(q):
    v = q.pop(0)
    for w in G[v]:
      if w not in explored:
        explored.append(w)
        q.append(w)
  return explored

def test_BFS():
  G = {1: [2, 3], 2: [3], 3: [4], 4: []}
  G2 =  {1 : [2, 3],
        2 : [1, 4],
        3 : [1, 4, 5],
        4 : [2, 3, 5, 6],
        5 : [3, 4, 6],
        6 : [4, 5]}
  assert BFS(G, 1) == [1, 2, 3, 4], "Test case 1 failed"
  assert BFS(G, 2) == [2, 3, 4], "Test case 2 failed"
  assert BFS(G, 3) == [3, 4], "Test case 3 failed"
  assert BFS(G, 4) == [4], "Test case 4 failed"
  assert BFS(G2, 1) == [1, 2, 3, 4, 5, 6], "Test case 5 failed"
  assert BFS(G2, 4) == [4, 2, 3, 5, 6, 1], "Test case 6 failed"
  print("All Breadth-first search test cases passed!")

# returns the shortest path from s to x, false if x do not exist
# works only in case of same weight edges, 
# otherwise it will return the path with least number of edges
def shortestPath(G, s, x):
  explored = [s]
  q = [s]
  d = {s : 0}
  while len(q):
    v = q.pop(0)
    if v == x:
      return d[v]
    for w in G[v]:
      if w not in explored:
        explored.append(w)
        q.append(w)
        d[w] = d[v] + 1
  return False

def test_shortestPath():
  G =  {1 : [2, 3],
        2 : [1, 4],
        3 : [1, 4, 5],
        4 : [2, 3, 5, 6],
        5 : [3, 4, 6],
        6 : [4, 5]}
  assert shortestPath(G, 1, 6) == 3, "Test case 1 failed"
  assert shortestPath(G, 2, 5) == 2, "Test case 2 failed"
  assert shortestPath(G, 3, 6) == 2, "Test case 3 failed"
  assert shortestPath(G, 1, 1) == 0, "Test case 4 failed"
  assert shortestPath(G, 6, 1) == 3, "Test case 5 failed"
  assert shortestPath(G, 6, 8) == False, "Test case 6 failed"
  print("All shortestPath test cases passed!")

# returns list of nodes, each in different component of the graph
def undirectedConnectivity(G : dict):
  # it may output unreachable parts of the same component as
  # different component if it takes directed graph, to correct it
  # convert the directed graph to undirected one first
  explored = []
  components = []
  for i in G:
    if i not in explored:
      components.append(i)
      explored += BFS(G, i)
  return components

def test_undirectedConnectivity():
  G =  {1 : [3, 5], 2 : [4], 3 : [1, 5], 4 : [2], 5 : [1, 3, 7, 9],
        6 : [8, 10], 7 : [5], 8 : [6, 10], 9 : [5], 10 : [6, 8]}
  assert undirectedConnectivity(G) == [1, 2, 6], "Test case 1 failed"
  G[7].append(2)
  assert undirectedConnectivity(G) == [1, 6], "Test case 2 failed"
  G[2].append(6)
  assert undirectedConnectivity(G) == [1], "Test case 3 failed"
  print("All undirectedConnectivity test cases passed!")

# depth-first search on graph G and start node s
# if want to search for some node x, take it as an argument
# if if v == x: return True
def DFS(G, s):
  explored = []
  q = [s]
  while len(q):
    v = q.pop()
    explored.append(v)
    # reverse G[v] if want the same sequence as the recursive version
    for w in G[v]:
      if w not in explored and w not in q:
        q.append(w)
  return explored

def test_DFS():
  G = {1: [2, 3], 2: [3], 3: [4], 4: []}
  G2 =  {1 : [2, 3],
        2 : [1, 4],
        3 : [1, 4, 5],
        4 : [2, 3, 5, 6],
        5 : [3, 4, 6],
        6 : [4, 5]}
  assert DFS(G, 1) == [1, 3, 4, 2], "Test case 1 failed"
  assert DFS(G, 2) == [2, 3, 4], "Test case 2 failed"
  assert DFS(G, 3) == [3, 4], "Test case 3 failed"
  assert DFS(G, 4) == [4], "Test case 4 failed"
  assert DFS(G2, 1) == [1, 3, 5, 6, 4, 2], "Test case 5 failed"
  assert DFS(G2, 4) == [4, 6, 5, 3, 1, 2], "Test case 6 failed"
  print("All depth-first search(iterative) test cases passed!")

# Recursive version of Depth-first search
def DFS_R(G, s, explored = None):
  if explored is None:
    explored = []
  explored.append(s)
  for v in G[s]:
    if v not in explored:
      DFS_R(G, v, explored)
  return explored

def test_DFS_R():
  G = {1: [2, 3], 2: [3], 3: [4], 4: []}
  G2 =  {1 : [2, 3],
        2 : [1, 4],
        3 : [1, 4, 5],
        4 : [2, 3, 5, 6],
        5 : [3, 4, 6],
        6 : [4, 5]}
  assert DFS_R(G, 2) == [2, 3, 4], "Test case 2 failed"
  assert DFS_R(G, 1) == [1, 2, 3, 4], "Test case 1 failed"
  assert DFS_R(G, 3) == [3, 4], "Test case 3 failed"
  assert DFS_R(G, 4) == [4], "Test case 4 failed"
  assert DFS_R(G2, 1) == [1, 2, 4, 3, 5, 6], "Test case 5 failed"
  assert DFS_R(G2, 4) == [4, 2, 1, 3, 5, 6], "Test case 6 failed"
  print("All depth-first search(recursion) test cases passed!")

# returns topological sorting of the nodes in graph
# applied only on acyclic directed graphs, we need sink vertex
# sink vertex = node that doesn't point to any other nodes
def topologicalSort(G: dict):
  # Straightforward solution
  if not G: return []
  
  sink = None
  for v in G:
    if not G[v]:
      sink = v
      del G[v]
      break
  if sink is None:
    raise ValueError("Graph is not acyclic")
  for v in G:
    if sink in G[v]:
      G[v].remove(sink)
  return topologicalSort(G) + [sink]

def test_topologicalSort():
    G = {1: [2, 3], 2: [3], 3: [4], 4: []}
    assert topologicalSort(G) == [1, 2, 3, 4], "Test case 1 failed"
    G2 = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert topologicalSort(G2) == [1, 3, 2, 4], "Test case 2 failed"
    G3 = {1 : [2, 3],
          2 : [4],
          3 : [5],
          4 : [3, 5, 6],
          5 : [6],
          6 : []}
    assert topologicalSort(G3) == [1, 2, 4, 3, 5, 6], "Test case 3 failed"
    G4 = {1 : [3, 5], 2 : [4], 3 : [5], 4 : [], 5 : [7, 9],
          6 : [10], 7 : [9], 8 : [6, 10], 9 : [], 10 : []}
    assert topologicalSort(G4) == [8, 6, 10, 1, 3, 5, 7, 9, 2, 4], "Test case 4 failed"
    print("All topological sort test cases passed!")

def topologicalSort2(G: dict):
  # the slick and fancy solution
  def DFS_R(G, s, explored = None):
    if explored is None:
      explored = []
    explored.append(s)
    for v in G[s]:
      if v not in explored:
        DFS_R(G, v, explored)
    nonlocal n # that's a new thing
    OrderedNodes[n] = s
    n -= 1
    return explored
  explored = []
  n = len(G)
  OrderedNodes = [0] * n
  n -= 1
  for v in G:
    if v not in OrderedNodes:
      DFS_R(G, v, explored)
  return OrderedNodes

def test_topologicalSort2():
    G = {1: [2, 3], 2: [3], 3: [4], 4: []}
    assert topologicalSort2(G) == [1, 2, 3, 4], "Test case 1 failed"
    G2 = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert topologicalSort2(G2) == [1, 3, 2, 4], "Test case 2 failed"
    G3 = {1 : [2, 3],
          2 : [4],
          3 : [5],
          4 : [3, 5, 6],
          5 : [6],
          6 : []}
    assert topologicalSort2(G3) == [1, 2, 4, 3, 5, 6], "Test case 3 failed"
    G4 = {1 : [3, 5], 2 : [4], 3 : [5], 4 : [], 5 : [7, 9],
          6 : [10], 7 : [9], 8 : [6, 10], 9 : [], 10 : []}
    assert topologicalSort2(G4) == [8, 6, 10, 2, 4, 1, 3, 5, 7, 9], "Test case 4 failed"
    print("All topological sort(fancy version) test cases passed!")

# return list of leader nodes of Strongly Connected Components in directed graphs
# if applied on undirected graph will work like undirectedConnectivity()
def SCC(G: dict):
  # 1. Let G_rev = reversed G
  G_rev = reverseGraph(G)
  
  def DFS_R(G, i, explored): # remove the None part since it's not used
    explored.append(i)
    for v in G[i]:
      if v not in explored:
        DFS_R(G, v, explored)
    newOrder.append(i)
    return explored
  # 2. Run DFS-Loop on G_rev to get the magical ordering
  newOrder = []
  explored = []
  for v in G_rev:
    if v not in explored:
      DFS_R(G_rev, v, explored)
  # 3. Run DFS-Loop on G to discover the SCCs one by one
  order = newOrder[::-1]
  explored.clear()
  newOrder.clear()
  scc = []
  for v in order:
    if v not in explored:
      DFS_R(G, v, explored)
      scc.append(newOrder[::-1])
      newOrder.clear()
  return scc

def reverseGraph(G):
  G_rev = {}
  for v in G:
    G_rev[v] = []
  for v in G:
    for u in G[v]:
      G_rev[u].append(v)
  return G_rev

def test_reverseGraph():
    G = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [3, 7]}
    G_rev = reverseGraph(G)
    expected_G_rev = {1: [7], 2: [5], 3: [9], 4: [1], 5: [8], 6: [3, 8], 7: [4, 9], 8: [2], 9: [6]}
    assert G_rev == expected_G_rev, "Test case 1 failed"
    G = {1 : [4], 2 : [8], 3 : [6], 4 : [7], 5 : [2], 6 : [9], 7 : [1], 8 : [5, 6], 9 : [3, 7]}
    G_rev = reverseGraph(G)
    assert G_rev == {1: [7], 2: [5], 3: [9], 4: [1], 5: [8], 6: [3, 8], 7: [4, 9], 8: [2], 9: [6]}, "test case 2 failed"
    print("All reverseGraph test cases passed!")

def test_SCC():
  G = {1 : [4], 2 : [8], 3 : [6], 4 : [7], 5 : [2], 6 : [9], 7 : [1], 8 : [5, 6], 9 : [3, 7]}
  assert SCC(G) == [[1, 4, 7], [9, 3, 6], [8, 5, 2]], "Test case 1 failed"
  G = {0 : [2], 1 : [0, 3], 2 : [1], 3 : [4], 4 : []}
  assert SCC(G) == [[4], [3], [0, 2, 1]], "Test case 2 failed"
  G = {1 : [2], 2 : [3, 4], 3 : [1, 8, 9], 4 : [5, 6], 5 : [7], 6 : [5], 7 : [6], 8 : [9], 9 : [10, 11],
      10 : [7, 8], 11 : [6, 10]}
  assert SCC(G) == [[5, 7, 6], [10, 8, 9, 11], [4], [1, 2, 3]], "Test case 3 failed"
  print("All Strongly Connected Components test cases passed!")

if __name__ == "__main__":
  test_BFS()
  test_shortestPath()
  test_undirectedConnectivity()
  test_DFS()
  test_DFS_R()
  test_topologicalSort()
  test_topologicalSort2()
  print("The grand finale of this module")
  test_SCC()
  test_reverseGraph()
  print("that was hard, around 10 hours of continuous work to finish the algorithms of this module")