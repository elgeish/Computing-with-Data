# Visualize the relationship between city mpg and engine displacement
# for different classes of vehicles
ggplot(mpg, aes(displ, cty)) + geom_point() +
  facet_wrap(~class)

# The facet argument is helpful when we want to arrange the sub-plots 
# in a specific order; below, we add new dataframe columns with more appropriate
# names for better labeling
mtcars$amf[mtcars$am==0] = "automatic"
mtcars$amf[mtcars$am==1] = "manual"
mtcars$vsf[mtcars$vs==0] = "flat"
mtcars$vsf[mtcars$vs==1] = "V-shape"

qplot(x = wt,
      y = mpg,
      facets = .~amf,
      data = mtcars,
      main = "MPG vs. Weight by Transmission")

qplot(x = wt,
      y = mpg,
      facets = vsf~.,
      data = mtcars,
      main = "MPG vs. Weight by Engine") +
  stat_smooth(se = FALSE)

qplot(x = wt,
      y = mpg,
      data = mtcars,
      facets = vsf~amf,
      main = "MPG vs. Weight by Transmission and Engine")
