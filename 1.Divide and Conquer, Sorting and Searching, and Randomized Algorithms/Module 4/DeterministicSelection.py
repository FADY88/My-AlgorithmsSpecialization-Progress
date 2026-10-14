from random import randint, sample

# Selection algorithm 
# (returns the ith element of a list after sorting)
# 3-th element of [3, 4, 5, 1, 2, 6, 7, 8, 9, 10] is 3

def medianOfMedians(l, start, end):
  if start == end: return None
  result = []
  five = 0
  for i in range(start, end + 1):
    if five == 5 or i == end:
      result.append(sorted(l[start:i])[five // 2])
      start = i
      five = 0
    five += 1
  return result

# l = [7, 2, 17, 12, 13, 8, 20, 4, 6, 3, 19, 1, 9, 5, 16, 10, 15, 18, 14, 11, 21, 22, 23]
# medianOfMedians(l, 0, len(l))

def DSelect(A, ith, start = 0, end = -1):
  if end < 0: end = len(A)
  if end - start < 2:
    try:
      return A[start]
    except:
      print("ERROR: empty list")
      return
  
  # p = randint(start, end - 1)
  c = medianOfMedians(A, start, end)
  p = DSelect(c, ith // 10, 0, len(c))
  
  # temporary loop for bypass returning p, not the index of p
  for i in range(start, end):
    if A[i] == p:
      p = i
      break
  
  
  # put pivot at the beginning
  A[p], A[start] = A[start], A[p]
  p = A[start]
  i = start + 1
  for j in range(start + 1, end):
    if A[j] < p:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[start], A[i - 1] = A[i - 1], A[start]
  
  j = i - 1 # let j = new index of p
  ith -= 1
  
  if j == ith: return p
  if j > ith : return DSelect(A, ith + 1, start, j)
  if j < ith : return DSelect(A, ith + 1, i, end)


# l = [3, 4, 5, 1, 2, 6, 7, 8, 9, 10]
unsorted_lists = [sample(range(1, 101), 100) for _ in range(20)]
for l in unsorted_lists:
  for _ in range(10):
    i = randint(1, 10)
    x = DSelect(l, i)
    y = sorted(l)
    if x != y[i - 1]:
      print("oops")
      exit(1)

print("well done")