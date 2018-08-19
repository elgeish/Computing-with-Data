# The R code below graphs log(x) as a function of x
curve(log, from = 0, to = 1000, xlab = 'x', 
      ylab = 'log(x)', main = 'The logarithm function')

print(3 ^ -800, digits = 22) # underflow
print(log(3 ^ -800), digits = 22) # log of underflow
print(-800 * log(3), digits = 22) # avoiding underflow using the log-scale

# Addition, when using the log-scale, replaces multiplication
print(3 ^ -600 * 3 ^ -100 * 3 ^ 150, digits = 22) # underflow
# Avoid underflow and return results in the log-scale
print(log(3) * (-600 - 100 + 150), digits = 22)
# Avoid underflow and return results in original scale
print(exp(log(3) * (-600 - 100 + 150)), digits = 22)
