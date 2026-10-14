# I'm not a mathematician so I'll assume that the
# matrices are of equal size and that size is an evan number
# the form of the matrices is as follows: [[1,2],[3,4]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], ...
# if things went good, I'll implement a function that modifies the matrices to be of the form above

def MatrixAdd(x, y):
  main = []
  for i in range(len(x)):
    sub = []
    for j in range(len(x)):
      sub.append(x[i][j] + y[i][j])
    main.append(sub)
  return main

def MatrixSub(x, y):
  main = []
  for i in range(len(x)):
    sub = []
    for j in range(len(x)):
      sub.append(x[i][j] - y[i][j])
    main.append(sub)
  return main

def MatrixMultiplication(x, y):
  # base case
  if len(x) == 2:
    a = x[0][0]
    b = x[0][1]
    c = x[1][0]
    d = x[1][1]
    e = y[0][0]
    f = y[0][1]
    g = y[1][0]
    h = y[1][1]
    return [[a*e+b*g, a*f+b*h],
            [c*e+d*g, c*f+d*h]]
  # split the matrices
  n = len(x)
  mid = n // 2
  a = [x[0][0:mid], x[1][0:mid]]
  b = [x[0][mid:n], x[1][mid:n]]
  c = [x[mid][0:mid], x[mid + 1][0:mid]]
  d = [x[mid][mid:n], x[mid + 1][mid:n]]
  e = [y[0][0:mid], y[1][0:mid]]
  f = [y[0][mid:n], y[1][mid:n]]
  g = [y[mid][0:mid], y[mid + 1][0:mid]]
  h = [y[mid][mid:n], y[mid + 1][mid:n]]
  
  p1 = MatrixMultiplication(a, MatrixSub(f, h))
  p2 = MatrixMultiplication(MatrixAdd(a, b), h)
  p3 = MatrixMultiplication(MatrixAdd(c, d), e)
  p4 = MatrixMultiplication(d, MatrixSub(g, e))
  p5 = MatrixMultiplication(MatrixAdd(a, d), MatrixAdd(e, h))
  p6 = MatrixMultiplication(MatrixSub(b, d), MatrixAdd(g, h))
  p7 = MatrixMultiplication(MatrixSub(a, c), MatrixAdd(e, f))
  
  s1 = MatrixAdd(MatrixSub(MatrixAdd(p5, p4), p2), p6)
  s2 = MatrixAdd(p1, p2)
  s3 = MatrixAdd(p3, p4)
  s4 = MatrixSub(MatrixSub(MatrixAdd(p1, p5), p3), p7)
  
  ans = []
  for i in range(mid):
    ans.append(s1[i] + s2[i])
  for i in range(mid):
    ans.append(s3[i] + s4[i])
  
  return ans


import unittest

# def MatrixMultiplication(A, B):
#     # Assuming A and B are square matrices of the same size
#     n = len(A)
#     C = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 C[i][j] += A[i][k] * B[k][j]
#     return C

class TestMatrixMultiplication(unittest.TestCase):
    def test_2x2_matrices(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        result = MatrixMultiplication(A, B)
        self.assertEqual(result, expected)

    def test_4x4_matrices(self):
        A = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        B = [
            [16, 15, 14, 13],
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ]
        expected = [
            [80, 70, 60, 50],
            [240, 214, 188, 162],
            [400, 358, 316, 274],
            [560, 502, 444, 386]
        ]
        result = MatrixMultiplication(A, B)
        self.assertEqual(result, expected)

    def test_identity_matrix(self):
        A = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        B = [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
        expected = [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
        result = MatrixMultiplication(A, B)
        self.assertEqual(result, expected)

    def test_zero_matrix(self):
        A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        result = MatrixMultiplication(A, B)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()