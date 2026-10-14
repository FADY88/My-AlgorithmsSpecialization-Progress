from random import randint

def QuickSort(A, start = 0, end = -1):
  if end < 0: end = len(A)
  if end - start < 2: return
  
  # choosing the middle element as pivot or random pivot
  p = randint(start, end - 1)
  # p = (start + end) // 2
  
  # put pivot at the beginning
  A[p], A[start] = A[start], A[p]
  p = A[start]
  i = start + 1
  for j in range(start + 1, end):
    if A[j] < p:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[start], A[i - 1] = A[i - 1], A[start]
  
  QuickSort(A, start, i - 1)
  QuickSort(A, i, end)
  return



# test cases with help from Copilot
def test_quick_sort():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 8, 2, 5, 1, 4, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([3, -1, 0, -3, 2, 1], [-3, -1, 0, 1, 2, 3])
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        QuickSort(input_list)
        assert input_list == expected, f"Test case {i+1} failed: expected {expected}, got {input_list}"
    print("All test cases passed!")

if __name__ == "__main__":
    l = [3, 8, 2, 5, 1, 4, 7, 6]
    print("Original list:", l)
    QuickSort(l)
    print("Sorted list:", l)
    
    test_quick_sort()