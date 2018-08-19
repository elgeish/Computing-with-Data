# Scalar Data Types

Scalar types include numeric, integer, logical, string, dates, and factors:

```R runnable
rm(list = ls())  # clears all variables

a = 3.2; b = 3  # double types
b
typeof(b)  # function returns type of object
c = as.integer(b)  # cast to integer type
c
typeof(c)
c = 3L  # alternative to casting: L specifies integer
d = TRUE
d
e = as.numeric(d)  # casting to numeric
e
f = "this is a string"  # string
f
ls.str()  # show variables and their types

# Factor variables assume values in a predefined set of possible values.
# The code below demonstrates the use of factors in R:
current.season = factor("summer",
          levels = c("summer", "fall", "winter", "spring"),
          ordered = TRUE)  # ordered factor
current.season
levels(current.season)  # display factor levels
my.eye.color = factor(
    "brown",
    levels = c("brown", "blue", "green"),
    ordered = FALSE)  # unordered factor
my.eye.color
```
