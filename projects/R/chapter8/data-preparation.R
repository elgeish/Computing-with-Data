vec1 = c("foo", "bar")
vec2 = c(31, 42)
vec3 = c(1, 2)
df = data.frame(name = vec1, ages = vec2, salary = vec3)
df
# You can change column names using the names function
names(df) = c("last.name", "age", "annual.income")
df

x = list(a = c(1, 2), b = c(3, 4), c = c(5, 6))
x
stack(x)  # this dataframe above is ready for graphing

# Plot normal density for different sigma values
x_grid = seq(-8, 8, length.out = 100)
gaussian_function =
    function(x, s) exp(-x ^ 2 / (2 * s ^ 2)) / (sqrt(2 * pi) * s)
df = stack(list("$\\sigma = 1$" = gaussian_function(x_grid, 1),
                "$\\sigma = 2$" = gaussian_function(x_grid, 2),
                "$\\sigma = 3$" = gaussian_function(x_grid, 3),
                "$\\sigma = 4$" = gaussian_function(x_grid, 4)))

names(df) = c("y", "sigma");
df$x = x_grid
head(df) 
qplot(x,
      y,
      color = sigma,
      lty = sigma,
      geom = "line",
      data = df,
      main = "Normal Density for Different $\\sigma$ Values",
      xlab = "$x$",
      ylab = "$f(x)$")
