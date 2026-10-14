# Input: n items. Each has a value:
# - Value vi (nonnegative)
# - Size wi (nonnegative and integral)
# - Capacity W (a nonnegative integer)
# Output: A which is a subset of S that maximizes the sum of its values
# while respecting the following
# the weights sum of A <= W
# running time: O(nW)
# Space complexity: O(nW)

def PathReconstruct(w, a, weights):
  selected_items = []
  for i in range(len(weights), 0, -1):
    if a[i][w] != a[i - 1][w]:
      selected_items.append(weights[i - 1])
      w -= weights[i - 1][1]
  
  return selected_items

# weights = [(value, weight), ...]
# weights = [(3, 4), (2, 3), (4, 2), (4, 3)]
def Knapsack(w, weights):
  n = len(weights)
  if n == 0:
    return (0, [])
  
  # DP Array
  A = [[0] * (w + 1) for _ in range(n + 1)]
  
  for i in range(1, n + 1):
    for x in range(w + 1):
      if x < weights[i - 1][1]:
        A[i][x] = A[i - 1][x]
      else:
        A[i][x] = max(A[i - 1][x], A[i - 1][x - weights[i - 1][1]] + weights[i - 1][0])
  
  return (A[n][w], PathReconstruct(w, A, weights)) # The last element is the Knapsack solution

# Example usage
weights = [(3, 4), (2, 3), (4, 2), (4, 3)]
print(Knapsack(6, weights))

if __name__ == "__main__":
  assert Knapsack(6, [(3, 4), (2, 3), (4, 2), (4, 3)]) == (8, [(4, 3), (4, 2)]), "test 1 failed"

  test_cases = [
    (5, [(3, 2), (4, 3), (5, 4), (6, 5)], (7, [(4, 3), (3, 2)])),
    # Basic case (example from our discussion)
    (6, [(3, 4), (2, 3), (4, 2), (4, 3)], (8, [(4, 3), (4, 2)])),

    # Single-element list
    (5, [(10, 5)], (10, [(10, 5)])),

    # Two elements (pick the larger one)
    (5, [(3, 2), (5, 3)], (8, [(5, 3), (3, 2)])),
    (3, [(3, 2), (5, 3)], (5, [(5, 3)])),

    # Three elements (choosing non-adjacent max)
    (6, [(3, 2), (10, 4), (5, 3)], (13, [(10, 4), (3, 2)])),

    # Longer sequence with a clear choice
    (10, [(1, 1), (2, 2), (9, 3), (4, 4), (5, 5)], (16, [(4, 4), (9, 3), (2, 2), (1, 1)])),

    # All increasing weights (should pick every second element)
    (12, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], (12, [(5, 5), (4, 4), (2, 2), (1, 1)])),

    # Alternating high and low values
    (15, [(10, 5), (1, 1), (10, 5), (1, 1), (10, 5)], (30, [(10, 5), (10, 5), (10, 5)])),
    (15, [(5, 5), (1, 1), (6, 6), (1, 1), (7, 7), (1, 1), (8, 8)], (15, [(7, 7), (1, 1), (6, 6), (1, 1)])),

    # Edge case: All elements are the same
    (14, [(7, 7), (7, 7), (7, 7), (7, 7)], (14, [(7, 7), (7, 7)])),

    # Edge case: Empty list
    (0, [], (0, [])),
  ]
  
  for (w, l, expected) in test_cases:
    assert Knapsack(w, l) == expected, f"test: {w}, {l} failed, expected: {expected}, Got: {Knapsack(w, l)}"
  
  print(f"{len(test_cases)} tests ran\nWell Done")