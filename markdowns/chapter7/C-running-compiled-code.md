# Running Compiled Code

Consider the code below, which compares two implementations of matrix
multiplication: The first uses R's internal matrix multiplication
and the second implements it through three nested loops,
each containing a scalar multiplication. The first matrix multiplication is
faster by several orders of magnitude even for a relatively small `n`.
The key difference is that the built-in matrix multiplication runs compiled C++
code:

```R runnable
n = 100
nsq = n * n
# generate two random matrices
a = matrix(runif(nsq), nrow = n, ncol = n)
b = matrix(runif(nsq), nrow = n, ncol = n)

system.time(a %*% b)  # built-in matrix multiplication

matMult = function(a, b, n) {
    m = matrix(data = 0, nrow = n, ncol = n)
    for (i in 1:n)
      for (j in 1:n)
          for (k in 1:n)
              m[i, j] = m[i, j] + a[i, k] * b[k, j]
    return(m)
   }
system.time(matMult(a, b, n)) # nested loops implementation
```
