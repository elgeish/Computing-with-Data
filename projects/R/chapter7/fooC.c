#include <R.h>
#include <math.h>

void fooC(double* a, double* b, int* n, double* result) {
  int i, j;
  for (i = 0; i < (*n); i++) {
    result[i] = 0;
    for (j = 0; j < (*n); j++)
      result[i] += pow(a[j] + i + 1, b[j]);
  }
}
