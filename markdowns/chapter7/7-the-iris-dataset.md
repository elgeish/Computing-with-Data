# The Iris Dataset

The core R package `datasets` contains many interesting and demonstrative
datasets, such as the `iris` dataset, whose first four dimensions are numeric
measurements describing flower geometry and whose last dimension is a string
describing the flower species. The below example explores the `iris` dataset:

```R runnable
library(datasets)
names(iris)  # lists the dimension (column) names
head(iris, 4)  # show first four rows
iris[1,]  # first row
iris$Sepal.Length[1:10]  # sepal length of first ten samples
# allow replacing iris$Sepal.Length with the shorter Sepal.Length
attach(iris, warn.conflicts = FALSE)
mean(Sepal.Length)  # average of Sepal.Length across all rows
colMeans(iris[, 1:4])  # means of all four numeric columns

# extract all rows whose Sepal.Length variable is less than 5 
# and whose species is not setosa
subset(iris, Sepal.Length < 5 & Species != "setosa")
# count number of rows corresponding to setosa species
dim(subset(iris, Species == "setosa"))[1]

# Provides a statistical summary of the different dataframe columns
summary(iris)

# Read text file into dataframe
# df = read.table("irisFile.txt", header = TRUE)  
# same but from Internet location
# df = read.table("http://www.exampleURL.com/irisFile.txt", header = TRUE)

# The following commands require an editor (e.g., Vim)
# edit(iris)  # examine data as spreadsheet
# iris = edit(iris)  # edit dataframe/variable
# newIris = edit(iris)  # edit dataframe/variable but keep original
```
