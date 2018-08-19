# To create a scatter plot with the graphics package,
# call plot with two dataframe columns
plot(faithful$waiting,
     faithful$eruptions,
     main = "Using plot",
     xlab = "waiting time (min)",
     ylab = "eruption time (min)")

# The arguments pch, col, and cex modify the marker's shape, color, and size
plot(faithful$waiting,
     faithful$eruptions,
     pch = 17,
     col = 2,
     cex = 1.2,
     main = "Specifying pch, col, and cex",
     xlab = "waiting times (min)",
     ylab = "eruption time (min)")

# Distinguish the points based on the value of another dataframe column
plot(mtcars$hp,
     mtcars$mpg,
     pch = mtcars$am,
     cex = 1.2,
     main = "MPG vs. HP by Transmission",
     xlab = "horsepower",
     ylab = "miles per gallon")
legend("topright", c("automatic", "manual"), pch = c(0, 1))

# Using qplot
qplot(x = waiting,
      y = eruptions,
      data = faithful,
      main = "Using qplot - Waiting Times (sec) vs. Eruptions (min)")

# The graph below shows a scatter plot of car weights vs mpg
qplot(x = wt, 
      y = mpg, 
      data = mtcars, 
      main = "Using qplot - MPG vs. Weight (x1000 lbs)")

# Denoting the number of cylinders by size using the size argument
qplot(x = wt,
      y = mpg,
      data = mtcars,
      size = cyl,
      main = "Using qplot with Size - MPG vs. Weight (x1000 lbs) by Cylinder")

# Alternatively, color can be used to encode the number of cylinders
qplot(x = wt,
      y = mpg,
      data = mtcars,
      color = cyl,
      main = "Using qplot with Color - MPG vs. Weight (x1000 lbs) by Cylinder")
