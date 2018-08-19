dyn.load("chapter7/fooC.so")  # load the compiled C code
a = seq(0, 1, length = 10)
b = seq(0, 1, length = 10)
c = rep(0, times = 10)
x = .C("fooC", a, b, as.integer(10), c)  # calls the fooC function
x[[4]]  # the 4th element contains the result

fooR = function(a, b, n) {
    result = rep(0, times = n)
    for (i in 1:n)
        for (j in 1:n)
            result[i] = result[i] + (a[j] + i) ^ b[j]
    return(result)
}
fooR(a, b, 10)

sizes = seq(10, 1000, length = 10)
rTime = rep(0, 10)
cTime = rTime
i = 1
for (n in sizes) {
    a = seq(0, 1, length = n)
    b = seq(0, 1, length = n)
    c = rep(0, times = n)
    cTime[i] = system.time(.C("fooC", a, b, as.integer(n), c))
    rTime[i] = system.time(fooR(a, b, n))
    i = i + 1
}

df = stack(list(C = cTime, R = rTime))
names(df) = c("system.time", "language")
df$size = sizes
# plot run time as a function of array size for R and .C implementations
qplot(x = size,
      y = system.time,
      lty = language, 
	  color = language, 
      data = df,
      size = I(1.5), 
	  geom = "line", 
      xlab = "array size", 
	  ylab = "computation time (sec)")
