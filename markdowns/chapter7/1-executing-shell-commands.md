# Executing Shell Commands

The function `system(command)` executes the given shell command:

```R runnable
# change directory to home directory
setwd("~")  
# display all files in current directory
dir(path = ".", all.files = TRUE)
# execute bash command ls -al (in Linux)
system("ls -al")  
```
