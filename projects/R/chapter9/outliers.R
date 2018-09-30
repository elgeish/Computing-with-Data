# Example 1 - the Black Monday stock crash on October 19, 1987
library(Ecdat)
data(SP500, package = 'Ecdat')
qplot(r500,
      main = "Histogram of log(P(t)/P(t-1)) for SP500 (1981-91)",
      xlab = "log returns",
      data = SP500)
qplot(seq(along = r500),
      r500,
      data = SP500,
      geom = "line",
      xlab = "trading days since January 1981",
      ylab = "log returns",
      main = "log(P(t)/P(t-1)) for SP500 (1981-91)")

# Example 2 - the R code below removes outliers
original_data = rnorm(20) 
original_data[1] = 1000  
sorted_data = sort(original_data)  
filtered_data = sorted_data[3:18]  
lower_limit = mean(filtered_data) - 5 * sd(filtered_data)  
upper_limit = mean(filtered_data) + 5 * sd(filtered_data)
not_outlier_ind = (lower_limit < original_data) & 
  (original_data < upper_limit)
print(not_outlier_ind)  
data_w_no_outliers = original_data[not_outlier_ind]

# Example 3 - winsorizes data containing an outlier
library(robustHD)
original_data = c(1000, rnorm(10))
print(original_data)
print(winsorize(original_data))
