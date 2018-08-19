set.seed(1)  # constant seed for reproducibility
df = data.frame(samples = c(rnorm(200, 1, 1),
                            rnorm(200, 0, 1),
                            rnorm(200, 0, 2)))
df$parameter[1:200]   = "$\\mathcal{N}(1, 1)$"
df$parameter[201:400] = "$\\mathcal{N}(0, 1)$"
df$parameter[401:600] = "$\\mathcal{N}(0, 2)$"
qplot(samples,
      bins = 30,
      facets = parameter~.,
      geom = "histogram",
      main = "Datasets",
      data = df)

# We compute below the qq-plots of these three datasets (y axis)
# vs. a sample drawn from the N(0, 1) distribution (x axis)
ggplot(df, aes(sample = samples)) +
  stat_qq() +
  facet_grid(.~parameter) +
  ggtitle("Quantile-Quantile of Datasets")

# Compare two distributions and show how the $t$-distribution has tails that
# are heavier than the Gaussian N(0, 1) distribution
x_grid = seq(-6, 6, length.out = 200)
df = data.frame(density = dnorm(x_grid, 0, 1))
df$tdensity = dt(x_grid, 1.5)
df$x = x_grid
ggplot(df, aes(x = x, y = density)) +
  geom_area(fill = I("grey")) +
  geom_line(aes(x = x, y = tdensity)) +
  ggtitle("$\\mathcal{N}(0, 1)$ (shaded) and $t$-distribution with 1.5 Degrees of Freedom")

df$samples = rnorm(200, 0, 1)
pm = list(df = 1.5)
ggplot(df, aes(sample = samples)) +
  stat_qq(distribution = qt, dparams = pm) +
  ggtitle("Quantile-Quantile of the Two Distributions Above")
