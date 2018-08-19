data = c(-1, 0, 0.5, 1, 2, 5, 5.5, 6)
data_size = length(data)
x_grid = seq(-3, data_size, length.out = 100)
kernel_values = x_grid %o% rep(1, data_size)
f = x_grid * 0
for (i in 1:data_size) {
  kernel_values[, i] = dnorm(x_grid, data[i], 1/6) / data_size
  f = f + kernel_values[, i]
}
plot(x_grid, f, xlab = "$x$", ylab = "$f_h(x)$", type = "l")
for (i in 1:data_size)
    lines(x_grid, kernel_values[, i] / 2, lty = 2)
title("Smoothed Histogram ($h=1/6$)", font.main = 1)

f = x_grid * 0
for(i in 1:data_size) {
  kernel_values[, i] = dnorm(x_grid, data[i], 1/3) / data_size
  f = f + kernel_values[, i]
}
plot(x_grid, f, xlab = "$x$", ylab = "$f_h(x)$", type = "l")
for (i in 1:data_size)
    lines(x_grid, kernel_values[, i] / 2, lty = 2)
title("Smoothed Histogram ($h=1/3$)", font.main = 1)

f = x_grid * 0
for (i in 1:data_size) {
  kernel_values[, i] = dnorm(x_grid, data[i], 1) / data_size
  f = f + kernel_values[, i]
}
plot(x_grid, f, xlab = "$x$" , ylab = "$f_h(x)$", type = "l")
for (i in 1:data_size)
    lines(x_grid, kernel_values[,i] / 2, lty = 2)
title("Smoothed Histogram ($h=1$)", font.main = 1)
