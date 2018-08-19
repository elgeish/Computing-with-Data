# Explore all-pairs relationships between city mpg, highway mpg,
# and engine displacement volume
df = mpg[, c("cty", "hwy", "displ")]
plot(df, main = "City MPG vs. Highway MPG vs. Engine Displacement Volume")

# Alternatively, we can use the ggpairs function (from the GGallly package);
# it also displays smoothed histograms of all variables in the diagonal panels
# and the correlation coefficients in the upper triangle
GGally::ggpairs(df)
