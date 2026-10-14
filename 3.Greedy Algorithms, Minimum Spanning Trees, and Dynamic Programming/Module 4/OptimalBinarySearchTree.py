# I used CoPilot to help me write this code.
# I did not fully test it but it looks fine.
# Maybe I will return to it in the future.

# Optimal binary search tree
# input: list of tuples (key, frequency)
# output: cost of optimal binary search tree

def OptimalBinarySearchTree(keys):
  n = len(keys)
  # DP Array
  A = [[0] * n for _ in range(n)]
  for i in range(n):
    A[i][i] = keys[i][1]
  for s in range(1, n):
    for i in range(n - s):
      j = i + s
      A[i][j] = min(A[i][k - 1] + A[k + 1][j] for k in range(i, j))
      A[i][j] += sum(keys[k][1] for k in range(i, j + 1))
  return A[0][n - 1]

if __name__ == "__main__":
  keys = [("x", 0.8), ("y", 0.1), ("z", 0.1)]
  print(OptimalBinarySearchTree(keys)) # 1.3