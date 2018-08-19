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
