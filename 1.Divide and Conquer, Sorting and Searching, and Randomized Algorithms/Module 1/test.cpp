#include <iostream>
// test of returning pointers as arrays and it works like a charm
int* createArray(int size)
{
  int* arr = new int[size];
  for (int i = 0; i < size; i++)
  {
    arr[i] = i;
  }
  return arr;
}

int main()
{
  int *ptr = createArray(5);
  for (int i = 0; i < 10; i++)
  {
    std::cout << ptr[i] << "  ";
  }
  delete ptr;
}