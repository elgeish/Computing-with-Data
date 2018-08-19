a = 1:10
c = 0  # compute sum of squares using a for-loop
for (e in a) c = c + e^2
c

sum(a ^ 2) # same operation using vector arithmetic

a = 1:1000000
c = 0
# time comparison with a million elements
system.time(for (e in a) c = c + e ^ 2)
system.time(sum(a ^ 2))

# The sapply function simplifies code but the computational speed-up may not
# apply in the same way as it did above
a = seq(0, 1, length.out = 10)
b = 0
c = 0
for (e in a) {
    b = b + exp(e)
}
b
c = sum(sapply(a, exp))
c
# sapply with an anonymous function f(x) = exp(x ^ 2)
sum(sapply(a, function(x) { return(exp(x ^ 2)) }))
# or simply
sum(sapply(a, function(x) exp(x ^ 2)))
