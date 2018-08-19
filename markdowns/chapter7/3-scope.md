# Scope

The code below demonstrates masking the built-in constant `pi` by a global
environment variable with the value 3, and retrieving the original value after
clearing it:

```R runnable
pi  # a built-in constant whose value is 3.141593
pi = 3  # redefines variable pi
pi  # .GlobalEnv match
rm(pi)  # removes masking variables
pi  # back to 3.141593
```
