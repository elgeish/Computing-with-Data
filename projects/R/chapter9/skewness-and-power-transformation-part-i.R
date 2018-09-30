# Example 1 - the diamonds dataset
head(diamonds)
summary(diamonds)

# Example 2 - the price histogram of a random subset of 1000 diamonds
diamondsSubset = diamonds[sample(dim(diamonds)[1], 1000), ]
qplot(price, data = diamondsSubset)

# Example 3 - a transformed histogram
qplot(log(price), size = I(1), data = diamondsSubset)

# Example 4 - transforming both variables
qplot(carat,
      price,
      size = I(1),
      data = diamondsSubset)
qplot(carat,
      log(price),
      size = I(1),
      data = diamondsSubset)
qplot(log(carat),
      price,
      size = I(1),
      data = diamondsSubset)
qplot(log(carat),
      log(price),
      size = I(1),
      data = diamondsSubset)

# Example 5 - display the original un-transformed variables on logarithmic axes
qplot(carat,
      price,
      log = "xy",
      size = I(1),
      data = diamondsSubset)
