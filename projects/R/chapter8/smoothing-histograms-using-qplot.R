qplot(x = c(2, 3, 6, 7),
      y = ..density..,
      geom = c("density"),
      kernel = "gaussian",
      adjust = 0.05,
      main = "adjust = 0.05",
      xlab = "$x$",
      ylab = "$f_h(x)$",
      xlim = c(0, 9))

# Increasing the value of h causes more overlap
qplot(x = c(2,3,6,7),
      y = ..density..,
      geom = c("density"),
      kernel = "gaussian",
      adjust = 0.2,
      main = "adjust = 0.2",
      xlab = "$x$",
      ylab = "$f_h(x)$",
      xlim = c(0, 9))

# Increasing the value of h further aggregates the four peaks
# into two, each responsible for a corresponding pair of nearby points
qplot(x = c(2, 3, 6, 7),
      y = ..density..,
      geom = c("density"),
      kernel = "gaussian",
      adjust = 0.5,
      main = "adjust = 0.5",
      xlab = "$x$",
      ylab = "$f_h(x)$",
      xlim = c(0, 9))

# Finally, further increasing the value of h results in a histogram
# with very wide bins in which all points fall in the same bin
qplot(x = c(2, 3, 6, 7),
      y = ..density..,
      geom = c("density"),
      kernel = "gaussian",
      adjust = 10,
      main = "adjust = 10",
      xlab = "$x$",
      ylab = "$f_h(x)$",
      xlim = c(0, 9))
