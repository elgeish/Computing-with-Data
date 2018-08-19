x_grid = seq(-3, 3, length.out = 100)
gaussian = function(x) dnorm(x)
triangular = function(x) {
  ind = abs(x) > 1
  x = 1 - abs(x)
  x[ind] = 0
  return(x)  
}
tricube = function(x) {
  ind = abs(x) > 1
  x = (1 - abs(x)^3)^3 
  x[ind] = 0
  return(x)
}
uniform = function(x) {
  ind = abs(x) > 1
  x = x * 0 + 1/2
  x[ind] = 0
  return(x)
}
df = stack(list("uniform" = uniform(x_grid),
               "triangular" = triangular(x_grid),
               "gaussian" = gaussian(x_grid),
               "tricube" = tricube(x_grid),
               "uniform" = uniform(x_grid / 2) / 2,
               "triangular" = triangular(x_grid / 2) / 2,
               "gaussian" = gaussian(x_grid / 2) / 2,
               "tricube" = tricube(x_grid / 2) / 2))
head(df)  # first six lines
names(df) = c("kernel.value", "kernel.type")
df$x = x_grid
df$h[1:400] = "$h = 1$"
df$h[401:800] = "$h = 2$"
head(df)  # first six lines
qplot(x,
      kernel.value,
      data = df,
      facets = kernel.type~h,
      geom = "line",
      xlab = "$x$",
      ylab = "$K_h(x)$")
