#include <iostream>
using namespace std;
void MergeSort(int arr[], int start, int end)
{
  // base case
  if (end - start < 2) {return;}
  int h = (end + start) / 2, k = start, i = 0, j = 0;

  int *a = new int[h - start];
  int *b = new int[end - h];
  MergeSort(arr , start, h);
  MergeSort(arr, h, end);

  for (int i = 0; i < h - start; i++)
  {
    a[i] = arr[start + i];
  }
  for (int i = 0; i < end - h; i++)
  {
    b[i] = arr[h + i];
  }

  while (i < h - start and j < end - h)
  {
    if (a[i] < b[j])
    {
      arr[k] = a[i];
      i++;
    }
    else
    {
      arr[k] = b[j];
      j++;
    }
    k++;
  }

  while (i < h - start)
  {
    arr[k] = a[i];
    i++;
    k++;
  }
  while (j < end - h)
  {
    arr[k] = b[j];
    j++;
    k++;
  }

  delete a, b;
  return;
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Test Case 1
    int arr1[] = {4, 3, 2, 1};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    MergeSort(arr1, 0, size1);
    cout << "Test Case 1: ";
    printArray(arr1, size1);

    // Test Case 2
    int arr2[] = {1, 2, 3, 4, 5};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    MergeSort(arr2, 0, size2);
    cout << "Test Case 2: ";
    printArray(arr2, size2);

    // Test Case 3
    int arr3[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int size3 = sizeof(arr3) / sizeof(arr3[0]);
    MergeSort(arr3, 0, size3);
    cout << "Test Case 3: ";
    printArray(arr3, size3);

    // Test Case 4
    int arr4[] = {5, 3, 8, 5, 2, 2, 9};
    int size4 = sizeof(arr4) / sizeof(arr4[0]);
    MergeSort(arr4, 0, size4);
    cout << "Test Case 4: ";
    printArray(arr4, size4);

    // Test Case 5
    int arr5[] = {42};
    int size5 = sizeof(arr5) / sizeof(arr5[0]);
    MergeSort(arr5, 0, size5);
    cout << "Test Case 5: ";
    printArray(arr5, size5);

    // Test Case 6
    int arr6[] = {};
    int size6 = sizeof(arr6) / sizeof(arr6[0]);
    MergeSort(arr6, 0, size6);
    cout << "Test Case 6: (Empty Array)" << endl;

    // Test Case 7
    int arr7[] = {100, 99, 98, 97, 96, 95, 94, 93, 92, 91};
    int size7 = sizeof(arr7) / sizeof(arr7[0]);
    MergeSort(arr7, 0, size7);
    cout << "Test Case 7: ";
    printArray(arr7, size7);

    // Test Case 8
    int arr8[] = {-3, -1, -7, 4, 2, 0};
    int size8 = sizeof(arr8) / sizeof(arr8[0]);
    MergeSort(arr8, 0, size8);
    cout << "Test Case 8: ";
    printArray(arr8, size8);

    return 0;
}