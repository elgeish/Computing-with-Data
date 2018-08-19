# Using the curve function
sinc = function(x) {
  return(sin(pi * x) / (pi * x))
}
curve(sinc, -7, +7, main = "Using curve")

# Using plot
s = sort.int(mpg$cty, index.return = T)
#  S$x holds the sorted values of city mpg
#  S$ix holds the indices of the sorted values of city mpg
#  First plot the sorted city mpg values with a line plot
plot(s$x,
     main = "Using plot",
     type = "l", 
     lty = 2, 
     xlab = "sample number (sorted by city mpg)",
     ylab = "mpg")
lines(mpg$hwy[S$ix] ,lty = 1)  # add dashed line of hwy mpg
legend("topleft", c("highway mpg", "city mpg"), lty = c(1, 2))

# Using qplot
x = seq(-2, 2, length.out = 30)
y = x ^ 2
qplot(x, y, geom = "line", main = "Using qplot")
qplot(x, y, geom = c("point", "line"))  # multiple geometries can be present

# Using ggplot
x = seq(-2, 2, length.out = 30)
y = x ^ 2
dataframe = data.frame(x = x, y = y)
ggplot(dataframe, aes(x = x, y = y)) + geom_line() + geom_point() +
  ggtitle("Using ggplot")
