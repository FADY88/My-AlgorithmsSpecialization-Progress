def test_InversionCount():
  # Test case 1: Basic input
  assert InversionCount([3, 1, 4, 1, 5, 9, 2, 6, 5]) == ([1, 1, 2, 3, 4, 5, 5, 6, 9], 10), "Failed on basic input"

  # Test case 2: Already sorted array
  assert InversionCount([1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5], 0), "Failed on already sorted input"

  # Test case 3: Reverse sorted array
  assert InversionCount([5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5], 10), "Failed on reverse sorted input"

  # Test case 4: Array with duplicates
  assert InversionCount([3, 3, 2, 3]) == ([2, 3, 3, 3], 2), "Failed on array with duplicates"

  # Test case 5: Array with negative numbers
  assert InversionCount([-1, -3, -2, 0, 2]) == ([-3, -2, -1, 0, 2], 2), "Failed on array with negative numbers"

  # Test case 6: Empty array
  assert InversionCount([]) == ([], 0), "Failed on empty input"

  # Test case 7: Single element array
  assert InversionCount([42]) == ([42], 0), "Failed on single element input"

  # Test case 8: Mixed positive and negative numbers
  assert InversionCount([-10, 0, 5, -3, 8]) == ([-10, -3, 0, 5, 8], 2), "Failed on mixed positive and negative input"

  # Test case 9: Large input
  import random
  large_input = random.sample(range(-10000, 10000), 1000)  # 1000 unique random integers
  assert InversionCount(large_input) == (sorted(large_input), len([1 for i in range(len(large_input)) for j in range(i+1, len(large_input)) if large_input[i] > large_input[j]])), "Failed on large input"

  # Test case 10: Array with floating-point numbers
  assert InversionCount([3.1, 2.4, -1.0, 4.5]) == ([-1.0, 2.4, 3.1, 4.5], 3), "Failed on floating-point numbers"

  print("All test cases passed!")


def InversionCount(arr):
  n = len(arr)
  if n < 2: return arr, 0
  h = n//2
  # l and r are the number of inversions in the left and right halves of the array
  a, l = InversionCount(arr[0: h])
  b, r = InversionCount(arr[h: n])
  sorted = []
  i, j = 0, 0
  while i < len(a) and j < len(b):
    # inversion case
    if a[i] > b[j]:
      sorted.append(b[j])
      j += 1
      l += len(a) - i
    else:
      sorted.append(a[i])
      i += 1
  if i == len(a):
    sorted = sorted + b[j:]
  else:
    sorted = sorted + a[i:]
    
  return sorted, l + r


def test_count_inversions():
    # Test case 1: Basic input
    assert count_inversions([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 10, "Failed on basic input"

    # Test case 2: Already sorted array
    assert count_inversions([1, 2, 3, 4, 5]) == 0, "Failed on already sorted input"

    # Test case 3: Reverse sorted array
    assert count_inversions([5, 4, 3, 2, 1]) == 10, "Failed on reverse sorted input"

    # Test case 4: Array with duplicates
    assert count_inversions([3, 3, 2, 3]) == 2, "Failed on array with duplicates"

    # Test case 5: Array with negative numbers
    assert count_inversions([-1, -3, -2, 0, 2]) == 2, "Failed on array with negative numbers"

    # Test case 6: Empty array
    assert count_inversions([]) == 0, "Failed on empty input"

    # Test case 7: Single element array
    assert count_inversions([42]) == 0, "Failed on single element input"

    # Test case 8: Mixed positive and negative numbers
    assert count_inversions([-10, 0, 5, -3, 8]) == 2, "Failed on mixed positive and negative input"

    # Test case 9: Large input
    import random
    large_input = random.sample(range(-10000, 10000), 1000)  # 1000 unique random integers
    # note: count_inversions do sort the original array
    assert len([1 for i in range(len(large_input)) for j in range(i+1, len(large_input)) if large_input[i] > large_input[j]]) == count_inversions(large_input), "Failed on large input"

    # Test case 10: Array with floating-point numbers
    assert count_inversions([3.1, 2.4, -1.0, 4.5]) == 3, "Failed on floating-point numbers"

    print("All test cases passed!")

# from CharGPT 
# Calculating the number of inversions using a modified merge sort algorithm in O(n logn) time complexity
def count_inversions(arr):
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions, because all elements left to i are greater than arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                j += 1
            k += 1

        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    # Recursive function to count inversions
    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    # Main function call
    n = len(arr)
    temp_arr = [0]*n
    return merge_sort_and_count(arr, temp_arr, 0, n-1)


# Run tests
test_InversionCount()
test_count_inversions()