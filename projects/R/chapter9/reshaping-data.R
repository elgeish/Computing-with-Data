# Example 1 - the melt function
library(reshape2)
# toy (wide) dataframe in the reshape2 package
smiths
# columns 2, 3, 4, 5 are measurements, 1 is key
melt(smiths, id = 1)
# columns 3, 4, 5 are measurements, 1,2 are key
melt(smiths, id = c(1, 2))

# Example 2 - the tips dataset
tips$total.bill = tips$total_bill
qplot(total.bill,
      tip,
      facets = sex~time,
      size = I(1.5),
      data = tips)

# Example 2 - analyzing tips and bills
head(tips)  # first six rows
tipsm = melt(tips,
             id = c("sex","smoker","day","time","size"))
head(tipsm)  # first six rows
tail(tipsm)  # last six rows
# Mean of measurement variables broken by sex.
# Note the role of mean as the aggregating function.
dcast(tipsm,
      sex~variable,
      fun.aggregate = mean)
# Number of occurrences for measurement variables broken by sex.
# Note the role of length as the aggregating function.
dcast(tipsm,
      sex~variable,
      fun.aggregate = length)
# Average total bill and tip for different times
dcast(tipsm,
      time~variable,
      fun.aggregate = mean)
# Similar to above with breakdown for sex and time:
dcast(tipsm,
      sex+time~variable,
      fun.aggregate = length)
# Similar to above, but with mean and added margins
dcast(tipsm,
      sex+time~variable,
      fun.aggregate = mean,
      margins = TRUE)
