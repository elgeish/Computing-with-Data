# To adjust h (see smoothing histograms), we modify the value of span
qplot(disp,
      mpg,
      data = mtcars,
      main = "MPG vs Eng. Displacement (span = 0.2)") +
  stat_smooth(method = "loess",
              method.args = list(degree = 0),
              span = 0.2,
              se = FALSE)

# Increasing the value of span results in a less wiggly curve
qplot(disp,
      mpg,
      data = mtcars,
      main = "MPG vs Eng. Displacement (span = 1)") +
  stat_smooth(method = "loess",
              method.args = list(degree = 0),
              span = 1,
              se = FALSE)

# Selecting an even larger h results in a nearly constant line
qplot(disp,
      mpg,
      data = mtcars,
      main = "MPG vs Eng. Displacement (span = 10)") +
  stat_smooth(method = "loess",
              method.args = list(degree = 0),
              span = 10,
              se = FALSE)

# Omitting span reverts to a default value
qplot(disp,
      mpg,
      data = mtcars,
      main = "MPG vs Eng. Displacement (default span)") +
  stat_smooth(method = "loess",
              method.args = list(degree = 0),
              se = FALSE)
