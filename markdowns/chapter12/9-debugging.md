# Debugging

```R
# Example 1
foo2 = function(i) {
  a = i + 1;
  b = a + 1;
  browser();
  a = b + 1;
  return(b)
}
foo2(3)

# Example 2
foo3 = function(i) {
  a = i + 1;
  b = a + 1;
  a = b + 1;
  return(b)
}
debug(foo3)
foo3(1)
undebug(foo3)

# Example 3
# start profiling
Rprof("diagonsisFile.out")
A = runif(1000)  # generate a vector of random numbers in [0,1]
B = runif(1000)  # generate another random vector
C = eigen(outer(A,B))
Rprof(NULL)  # end profiling
summaryRprof("diagonsisFile.out")
```
