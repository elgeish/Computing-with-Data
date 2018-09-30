# Example 1 - the Animals dataset
library(MASS)
Animals
qplot(brain, body, data = Animals)

# Example 2 - a power transformation
qplot(brain, body, log = "xy", data = Animals)
