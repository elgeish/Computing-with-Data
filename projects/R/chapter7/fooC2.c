#include <R.h>
#include <Rinternals.h>
#include <Rmath.h>
#include <math.h>

SEXP fooC2(SEXP aR, SEXP  bR)
{ 
  int i, j, n = length(aR);
  double *a = REAL(aR), *b = REAL(bR);
  SEXP Rval = allocVector(REALSXP, n);
  
  for (i = 0; i < n; i++) {
    REAL(Rval)[i] = 0;
    for (j = 0; j < n; j++)
      REAL(Rval)[i] += pow(a[j] + i + 1, b[j]);
  }
  return Rval;
}
