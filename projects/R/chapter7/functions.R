# foo is a user-defined function
foo = function(x = 1, y = 2, z = 3) {
    return(x + y + z)
}
foo(10, 20, 30)  # parameter bindings by order
foo(y = 20, x = 10, z = 30)  # (potentially) out of order parameter bindings
foo(x = 10, y = 20, z = 30)  # passing 3 parameters
foo(z = 30)  # x and y are missing and are assigned default values
foo(10)  # in-order parameter binding with last two parameters missing

# myPower(.,.) raises the first argument to the power of the second; the former
# is named bas and has a default value of 10; the latter is named pow and has
# a default value of 2
myPower = function(bas = 10, pow = 2) {
    return(bas ^ pow) # raise base to a power
}
myPower(2, 3)  # 2 is bound to bas and 3 to pow (in-order)
myPower(pow = 3, bas = 2)  # same binding as above (out-of-order parameter names)
myPower(bas = 3)  # default value of pow is used

# R passes variables by value: Changing passed arguments inside a function
# does not modify their respective values in the calling environment
x = 2
myPower2 = function(x) { x = x ^ 2; return(x) }
y = myPower2(x)  # does not change x outside the function
x
y
