# Vectors, Arrays, Lists, and Dataframes

Vectors, arrays, lists, and dataframes are collections that hold multiple scalar values:

```R runnable
# c() concatenates arguments to create a vector
x = c(4, 3, 3, 4, 3, 1)  
x
length(x)
2 * x + 1  # element-wise arithmetic
# Boolean vector (default is FALSE)
y = vector(mode = "logical", length = 4)
y
# numeric vector (default is 0)
z = vector(length = 3, mode = "numeric")
z
q = rep(3.2, times = 10) # repeat value multiple times
q
w = seq(0, 1, by = 0.1)  # values in [0,1] in 0.1 increments
w
# 11 evenly spaced numbers between 0 and 1
w = seq(0, 1, length.out = 11)
w
# create an array of booleans reflecting whether condition holds
w <= 0.5
any(w <= 0.5) # is it true for some elements?
all(w <= 0.5) # is it true for all elements?
which(w <= 0.5) # for which elements is it true?
w[w <= 0.5] # extracting from w entries for which w<=0.5
subset(w, w <= 0.5) # an alternative with the subset function
w[w <= 0.5] = 0 # zero out all components smaller or equal to 0.5
w

# Arrays are multidimensional generalizations of vectors
z = seq(1, 20,length.out = 20)  # create a vector 1, 2, ..., 20
x = array(data = z, dim = c(4, 5))  # create a 2-d array
x
x[2, 3]  # refer to the second row and third column
x[2, ]  # refer to the entire second row
x[-1, ]  # all but the first row - same as x[c(2, 3, 4), ]
y = x[c(1, 2), c(1, 2)]  # 2x2 top left sub-matrix
2 * y + 1  # element-wise operation
y %*% y  # matrix product (both arguments are matrices)
# inner product (both vectors have the same dimensions)
x[1, ] %*% x[1, ]
t(x)  # matrix transpose
outer(x[, 1], x[, 1])  # outer product
rbind(x[1, ], x[1, ])  # vertical concatenation
cbind(x[1, ], x[1, ])  # horizontal concatenation

# Multidimensional arrays
m = matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2)
m
m[3]  # counting by columns A[3] = A[1, 2]

# Lists are ordered collections which permit positions to hold variables
# of different types
x = list(name = "John", age = 55, no.children = 2, children.ages = c(15, 18))
names(x)  # displays all position names
x[[2]]  # second element
x[2]  # list containing second element
x$name  # value in list corresponding to name
x["name"]  # same thing
x$children.ages[2]  # same as L[[4]][2]

# Smaller arrays are extended as needed
a = c(1, 2)
b = c(10, 20, 30, 40, 50)
a + b
b[7] = 70
b

# A dataframe is  an ordered sequence of lists sharing the same signature
vecn = c("John Smith", "Jane Doe")
veca = c(42, 45)
vecs = c(50000, 55000)
df = data.frame(name = vecn, age = veca, salary = vecs)
df
names(df) = c("NAME", "AGE", "SALARY")  # modify column names
df
```
