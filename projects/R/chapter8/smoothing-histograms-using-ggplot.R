ggplot(faithful, aes(x = waiting, y = ..density..)) +
  geom_histogram(alpha = 0.3, bins = 30) +
  geom_density(size = 1.5, color = "red")
