# A sink records output to the given file.
# To print to both the screen and to a file (tee), use the following variation:
sink(file = "outputFile", split = TRUE)

source("chapter7/foo.R")  # executes R code written in a text file
system("cat outputFile")  # prints what was captured by the sink above
