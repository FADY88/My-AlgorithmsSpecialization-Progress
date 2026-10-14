import unittest

# Dijkstra's Shortest Path algorithm
# graph = {node : [(node, length), ...], ...}
def ShortestPaths(G, s):
    X = [s]
    A = {s: 0}
    B = {s: []}
    while len(G) > len(X):
        newNode = None
        length = 0
        path = []
        for v in X:
            # loop over tuples of (node w, length l)
            for w, l in G[v]:
                if w not in X:
                    tmp = A[v] + l
                    if length == 0 or tmp < length:
                        length = tmp
                        newNode = w
                        path = B[v] + [w]
        
        if newNode == None: break
        X.append(newNode)
        A[newNode] = length
        B[newNode] = path

    return X, A, B

class TestShortestPaths(unittest.TestCase):
    def test_single_node(self):
        G = {1: []}
        s = 1
        expected_X = [1]
        expected_A = {1: 0}
        expected_B = {1: []}
        self.assertEqual(ShortestPaths(G, s), (expected_X, expected_A, expected_B))

    def test_two_nodes(self):
        G = {1: [(2, 1)], 2: []}
        s = 1
        expected_X = [1, 2]
        expected_A = {1: 0, 2: 1}
        expected_B = {1: [], 2: [2]}
        self.assertEqual(ShortestPaths(G, s), (expected_X, expected_A, expected_B))

    def test_multiple_nodes(self):
        G = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: []}
        s = 1
        expected_X = [1, 2, 3]
        expected_A = {1: 0, 2: 1, 3: 3}
        expected_B = {1: [], 2: [2], 3: [2, 3]}
        self.assertEqual(ShortestPaths(G, s), (expected_X, expected_A, expected_B))

    def test_disconnected_graph(self):
        G = {1: [(2, 1)], 2: [], 3: [(4, 1)], 4: []}
        s = 1
        expected_X = [1, 2]
        expected_A = {1: 0, 2: 1}
        expected_B = {1: [], 2: [2]}
        self.assertEqual(ShortestPaths(G, s), (expected_X, expected_A, expected_B))

if __name__ == '__main__':
    unittest.main()
