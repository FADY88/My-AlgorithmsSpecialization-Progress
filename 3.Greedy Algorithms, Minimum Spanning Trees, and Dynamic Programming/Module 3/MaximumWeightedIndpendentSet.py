# A path graph is a type of graph in which all the vertices are arranged in a single straight-line path.
# Each vertex is connected to at most two other vertices, except for the endpoints.
# will be represented here as list of integers represent vertices' weights
# v1 — v2 — v3 — v4 — v5 will be [v1, v2, v3, v4, v5]
def PathReconstruct(a, weights):
  s = []
  i = len(a) - 1
  while i >= 1:
    if i == 1:
      s.append(weights[i])
      i -= 1
    elif a[i - 1] >= a[i - 2] + weights[i]:
      i -= 1
    else:
      s.append(weights[i])
      if i == 2:
        s.append(weights[i - 2])
      i -= 2
  return s

def MWIS(weights):
  n = len(weights)
  if n == 0:
      return (0, [])
  elif n == 1:
      return (weights[0], [weights[0]])
  
  # DP Array
  A = [0] * n
  A[0] = weights[0]
  A[1] = max(weights[0], weights[1])
  
  for i in range(2, n):
    A[i] = max(A[i-1], A[i-2] + weights[i])
  
  return (A[-1], PathReconstruct(A, weights)) # The last element is the MWIS solution

# Example usage
weights = [4, 2, 7, 3, 8]
print(MWIS(weights)) 
print(MWIS([1, 4, 5, 4]))

if __name__ == "__main__":
  assert MWIS([1, 4, 5, 4]) == (8, [4, 4]), "test 1 failed"
  # Output: 15 (selecting w1, w3, w5)
  assert MWIS([4, 2, 7, 3, 8]) == (19, [8, 7, 4]), "test 2 failed"
  
  test_cases = [
    # Basic case (example from our discussion)
    ([4, 2, 7, 3, 8], (19, [8, 7, 4])),

    # Single-element list (trivial MWIS)
    ([10], (10, [10])),

    # Two elements (pick the larger one)
    ([3, 5], (5, [5])),

    # Three elements (choosing non-adjacent max)
    ([3, 10, 5], (10, [10])),
    ([10, 3, 5], (15, [5, 10])),

    # Longer sequence with a clear choice
    ([1, 2, 9, 4, 5], (15, [5, 9, 1])),

    # All increasing weights (should pick every second element)
    ([1, 2, 3, 4, 5, 6], (12, [6, 4, 2])),

    # Alternating high and low values
    ([10, 1, 10, 1, 10], (30, [10, 10, 10])),
    ([5, 1, 6, 1, 7, 1, 8], (26, [8, 7, 6, 5])),

    # Edge case: All elements are the same
    ([7, 7, 7, 7], (14, [7, 7])),

    # Edge case: Empty list
    ([], (0, [])),
  ]
  for (l, expected) in test_cases:
    assert MWIS(l) == expected, f"test {l} failed, expected: {expected}"
  
  print(f"{len(test_cases)} tests ran\nWell Done")