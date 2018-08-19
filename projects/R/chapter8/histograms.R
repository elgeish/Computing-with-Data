# Using the hist function to show Old Faithful's eruption times
hist(faithful$eruptions, 
     breaks = 20, 
     xlab = "eruption times (min)", 
     ylab = "count", 
     main = "Using hist")

# Old Faithful's waiting time to the next eruption using qplot
qplot(x = waiting, 
      data = faithful, 
      binwidth = 3, 
      main = "Using qplot - Waiting Time to Next Eruption (min)")

# The same histogram but using ggplot this time
ggplot(faithful, aes(x = waiting)) + geom_histogram(binwidth = 1) +
      ggtitle("Using ggplot - Waiting Time to Next Eruption (min)")

# Histograms can show density where the height of each bin times its width
# equals the count of samples falling in the bin divided by the total count
ggplot(faithful, aes(x = waiting, y = ..density..)) + 
      geom_histogram(binwidth = 4) +
      ggtitle("Using ggplot to Show Density")
