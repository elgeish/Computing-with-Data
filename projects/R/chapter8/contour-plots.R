x_grid = seq(-1, 1, length.out = 100)
y_grid = x_grid
# Create a dataframe containing all possible combinations of (x, y)
df = expand.grid(x_grid, y_grid)
dim(df) #  number of rows is 100 x 100 - one for each combination
names(df) = c("x", "y")  # modify column names for better labeling
df$z = df$x ^ 2 + df$y ^ 2
head(df)
ggplot(df, aes(x = x, y = y, z = z)) + stat_contour()
