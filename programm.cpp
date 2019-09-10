#include <stdio.h>
#include <string.h>
#include <algorithm>
typedef unsigned long long ull_t;
const ull_t SIZE = (1UL << 60);

int main() {
      int arr[SIZE] = {};
      for (ull_t i = 0; i < SIZE; ++i)
        arr[i] = i;
      int last = arr[SIZE - 1];
      puts("Hello");
      return 0;
}