#include <iostream>
#include <bits/stdc++.h>
using namespace std;
// code from CoPilot
// void QuickSort (int list[], int left, int right) {
//   if (left < right) {
//     int i = left;
//     int j = right;
//     int pivot = list[(left + right) / 2];
//     while (i <= j) {
//       while (list[i] < pivot) {
//         i++;
//       }
//       while (list[j] > pivot) {
//         j--;
//       }
//       if (i <= j) {
//         int temp = list[i];
//         list[i] = list[j];
//         list[j] = temp;
//         i++;
//         j--;
//       }
//     }
//     QuickSort(list, left, j);
//     QuickSort(list, i, right);
//   }
// }

// My implementation
void QuickSort(int A[], int size, int start = 0, int end = -1) {
  if (end < 0)
    end = size;
  if (end - start < 2)
    return;
  
  // choosing pivot randomly or the middle element
  // int p = (start + end) / 2;
  // srand(time(0));
  // the following line is taken from https://stackoverflow.com/questions/12657962/how-do-i-generate-a-random-number-between-two-variables-that-i-have-stored
  int p = rand() % ((end - 1) - start + 1) + start;
  
  int tmp = A[p];
  A[p] = A[start];
  A[start] = tmp;
  p = A[start];
  int i = start + 1;
  for (int j = i; j < end; j++) {
    if (A[j] < p)
    {
      tmp = A[i];
      A[i] = A[j];
      A[j] = tmp;
      i++;
    }
  }
  tmp = A[start];
  A[start] = A[i - 1];
  A[i -1] = tmp;

  QuickSort(A, i - start, start, i - 1);
  QuickSort(A, end - i, i, end);
}

void test_quick_sort() {
    vector<pair<vector<int>, vector<int>>> test_cases = {
        {{}, {}},
        {{1}, {1}},
        {{2, 1}, {1, 2}},
        {{3, 8, 2, 5, 1, 4, 7, 6}, {1, 2, 3, 4, 5, 6, 7, 8}},
        {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
        {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}},
        {{3, -1, 0, -3, 2, 1}, {-3, -1, 0, 1, 2, 3}},
        {{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}},
        {{1, 3, 2, 3, 1, 2, 3, 1}, {1, 1, 1, 2, 2, 3, 3, 3}},
        {{100, 50, 25, 75, 10, 90, 30, 60}, {10, 25, 30, 50, 60, 75, 90, 100}},
        {{-5, -10, 0, 5, 10, -15, 20, -20}, {-20, -15, -10, -5, 0, 5, 10, 20}}
    };

    for (int i = 0; i < test_cases.size(); i++) {
        vector<int> input_list = test_cases[i].first;
        vector<int> expected = test_cases[i].second;
        QuickSort(input_list.data(), input_list.size());
        assert(input_list == expected && "Test case failed");
    }
    cout << "All test cases passed!" << endl;
}

int main() {
  int list[] = {3, 8, 2, 5, 1, 4, 7, 6};
  int size = sizeof(list) / sizeof(list[0]);
  for (int i = 0; i < size; i++) {
    cout << list[i] << " ";
  }
  cout << endl;
  // QuickSort(list, 0, size - 1);
  QuickSort(list, size);
  for (int i = 0; i < size; i++) {
    cout << list[i] << " ";
  }
  cout << endl;

  test_quick_sort();
  return 0;
}
