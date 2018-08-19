# This is a comment
a = 4  # single statement 
a = 4; b = 3; c = b  # multiple statements

# R has a dynamic type system; you can define a variable without declaring its
# type explicitly and you can change the variable's type in the same session:
a = 3.2
a = "foo"
a <- 4  # another way to assign value

# Here are a few different ways to display the value of a variable:
a = 4
print(a)
a  # same thing
cat(a)  # same thing
# cat can print multiple variables one after the other 
cat("The value of the variable a is: ", a)

# Here are some important commands with short explanations:
x = 3  # assign value 3 to variable x
y = 3 * x + 2  # basic variable assignment and arithmetic
ratio.of.x.and.y = x / y  # divide x by y and assign result
ls()  # list variable names in workspace memory
ls(all.names = TRUE)  # list all variables including hidden ones
ls.str()  # print annotated list of variable names
save.image(file = "file-name")  # save all variables to a file
save(x, y, file = "varFile")  # save specified variables
rm(x, y)  # clear variables x and y from memory
rm(list = ls())  # clear all variables in workspace memory
load("varFile")  # load variables from file back to the workspace
cat(x)
