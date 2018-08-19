# Display 0 through 100 percentiles at 0.1 increments
# for the dataset containing 1, 2, 3, 4.
quantile(c(1, 2, 3, 4), seq(0, 1, length.out = 11))

ggplot(mpg, aes("", hwy)) +
  geom_boxplot() +
  coord_flip() +
  scale_x_discrete("") +
  ggtitle("Highway MPG")

# Plot several box plots side-by-side in order to compare data
# corresponding to different values of a factor variable
ggplot(mpg, aes(reorder(class, -hwy, median), hwy)) +
  geom_boxplot() +
  coord_flip() +
  scale_x_discrete("class") +
  ggtitle("Highway MPG by Class")

