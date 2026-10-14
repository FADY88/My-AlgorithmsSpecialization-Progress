def test_mergeSort():
    # Test case 1: Basic input
    assert MergeSort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9], "Failed on basic input"

    # Test case 2: Already sorted array
    assert MergeSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Failed on already sorted input"

    # Test case 3: Reverse sorted array
    assert MergeSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Failed on reverse sorted input"

    # Test case 4: Array with duplicates
    assert MergeSort([3, 3, 2, 3]) == [2, 3, 3, 3], "Failed on array with duplicates"

    # Test case 5: Array with negative numbers
    assert MergeSort([-1, -3, -2, 0, 2]) == [-3, -2, -1, 0, 2], "Failed on array with negative numbers"

    # Test case 6: Empty array
    assert MergeSort([]) == [], "Failed on empty input"

    # Test case 7: Single element array
    assert MergeSort([42]) == [42], "Failed on single element input"

    # Test case 8: Mixed positive and negative numbers
    assert MergeSort([-10, 0, 5, -3, 8]) == [-10, -3, 0, 5, 8], "Failed on mixed positive and negative input"

    # Test case 9: Large input
    import random
    large_input = random.sample(range(-10000, 10000), 1000)  # 1000 unique random integers
    assert MergeSort(large_input) == sorted(large_input), "Failed on large input"

    # Test case 10: Array with floating-point numbers
    assert MergeSort([3.1, 2.4, -1.0, 4.5]) == [-1.0, 2.4, 3.1, 4.5], "Failed on floating-point numbers"

    print("All test cases passed!")


def MergeSort(arr):
  n = len(arr)
  if n < 2: return arr
  h = n//2
  a = MergeSort(arr[0: h])
  b = MergeSort(arr[h: n])
  sorted = []
  i, j = 0, 0
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      sorted.append(a[i])
      i += 1
    else:
      sorted.append(b[j])
      j += 1
  if i == len(a):
    sorted = sorted + b[j:]
  else:
    sorted = sorted + a[i:]
    
  return sorted

# Run tests
test_mergeSort()