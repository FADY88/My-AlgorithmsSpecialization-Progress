# a really good example of applying the dynamic programming paradigm
# Input: g gap cost, m mismatch cost, x and y strings:
# Output: the alignment cost of the two strings


def Alignment(g, m, x, y):
  x = x.upper()
  y = y.upper()
  lenX = len(x)
  lenY = len(y)
  
  def misMatch(s1, s2):
    return m if s1 != s2 else 0
  # DP Array
  A = [[0] * (lenY + 1) for _ in range(lenX + 1)]
  for i in range(1, lenX + 1):
    A[i][0] = i * g
  for j in range(1, lenY + 1):
    A[0][j] = j * g

  
  
  
  for i in range(1, lenX + 1):
    for j in range(1, lenY + 1):
      A[i][j] = min(A[i - 1][j - 1] + misMatch(x[i-1], y[j-1]),
                    A[i - 1][j] + g,
                    A[i][j - 1] + g)
  
  i, j, a, b = lenX, lenY, "", ""
  while i > 0 or j > 0:
    if i > 0 and j > 0 and A[i][j] == A[i - 1][j - 1] + misMatch(x[i-1], y[j-1]):
      y_j = y[j - 1].lower() if misMatch(x[i-1], y[j-1]) else y[j - 1]
      a, b = x[i-1] + a, y_j + b
      i, j = i - 1, j - 1
    elif j > 0 and A[i][j] == A[i][j - 1] + g:
      a, b = "-" + a, y[j-1] + b
      j -= 1
    else:
      a, b = x[i-1] + a, "-" + b
      i -= 1
  
  return (A[lenX][lenY], a, b) # The last element is the score solution

# Example usage
print(Alignment(2, 1, "GATTACA", "CTGACT"))
print(Alignment(2, 2, "AGGGCT", "AGGCA"))
print(Alignment(2, 2, "AGGGCT", "AGGGCT"))
print(Alignment(2, 2, "AGGGCT", ""))
print(Alignment(2, 2, "", "AGGGCT"))

if __name__ == "__main__":
  test_cases = [
    # Basic case with one mismatch and one gap
    (2, 1, "AGT", "ACT", (1, "AGT", "AcT")),

    # Perfect match (no penalty)
    (2, 1, "AGT", "AGT", (0, "AGT", "AGT")),

    # 2 mismatches
    (2, 1, "AGT", "CGA", (2, 'AGT', 'cGa')),

    # One sequence is a subset of the other (introduces gaps)
    (2, 1, "AGT", "AG", (2, 'AGT', 'AG-')),

    # Different lengths with gaps
    (2, 1, "AGT", "AGTT", (2, 'AG-T', 'AGTT')),

    # Completely different characters, longer strings
    (2, 1, "GATTACA", "CTGACT", (5, 'GATTACA', '-cTgACt')),

    # Single-character match
    (2, 1, "A", "A", (0, "A", "A")),

    # Single-character mismatch
    (2, 1, "A", "T", (1, "A", "t")),

    # One string empty (all gaps)
    (2, 1, "AGT", "", (6, "AGT", "---")),

    # Both strings empty
    (2, 1, "", "", (0, "", ""))
]


  
  for (g, m, s1, s2, expected) in test_cases:
    assert Alignment(g, m, s1, s2) == expected, f"test: {(g, m, s1, s2)} failed, expected: {expected}, Got: {Alignment(g, m, s1, s2)}"
  
  print(f"{len(test_cases)} tests ran\nWell Done")
  