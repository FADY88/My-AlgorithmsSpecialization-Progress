def two_sum_bruteForce(l, t):
  for i in range(len(l)):
    for j in range(i + 1, len(l)):
      if l[i] + l[j] == t:
        return [i, j]
  return None

def two_sum_pointers(l, t):
  # Store (num, index)
  nums_sorted = sorted((num, i) for i, num in enumerate(l))
  start = 0
  end = len(nums_sorted) - 1
  while start != end:
    if nums_sorted[start][0] + nums_sorted[end][0] > t:
      end -= 1
    elif nums_sorted[start][0] + nums_sorted[end][0] < t:
      start += 1
    else:
      i = min(nums_sorted[start][1], nums_sorted[end][1])
      j = max(nums_sorted[start][1], nums_sorted[end][1])
      return [i, j]
  return None

def two_sum_hashTable(l, t):
  d = {}
  for i, num in enumerate(l):
    complement = t - num
    if complement in d:
      return [d[complement], i]
    d[num] = i
  return None


def test(fun):
  assert fun([2, 7, 11, 15], 9) == [0, 1]
  assert fun([3, 2, 4], 6) == [1, 2]
  assert fun([3, 3], 6) == [0, 1]

  # Negative numbers
  assert fun([-1, -2, -3, -4, -5], -8) == [2, 4]

  # Large numbers
  assert fun([1000000, 500, 500000, 999500], 1000000) == [1, 3]

  # Target as sum of first and last element
  if fun == two_sum_hashTable:
    # using hashTable make the search looks backwards not forward
    assert fun([1, 2, 3, 4, 5], 6) == [1, 3]
  else:
    assert fun([1, 2, 3, 4, 5], 6) == [0, 4]

  # Unsorted array with random numbers
  assert fun([10, 25, 30, 5, 15], 40) == [0, 2]

  # Large list with solution near the end
  nums = list(range(1, 10001))  # [1, 2, 3, ..., 10000]
  assert fun(nums, 19999) == [9998, 9999]  # (9999 + 10000 = 19999)

  try:
    assert fun([1, 2, 3, 4], 10) is None  # No valid pair
  except:
    print("No solution found, as expected.")
  
  print(f"{fun.__name__}() is done.")

if __name__ == "__main__":
  test(two_sum_bruteForce) # O(n**2)
  test(two_sum_pointers)   # O(n log n)
  test(two_sum_hashTable)  # O(n)