set.seed(1)  # constant seed for reproducibility
df = data.frame(replicate(2, sample(0:100, 100, rep = TRUE)))
names(df) = c("col1", "col2")

# Using the plot function from the graphics package
plot(x = df$col1, y = df$col2, xlab = "x", ylab = "y")
title(main = "Using plot")  # add title

# Using the two main functions in ggplot2: qplot and ggplot
qplot(x = col1, y = col2, data = df, geom = "point") + ggtitle("Using qplot")
ggplot(df, aes(x = col1, y = col2)) + geom_point() + ggtitle("Using ggplot")
