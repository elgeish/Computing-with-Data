# this is a comment
# the prefix ## indicates an output line
# the echo command displays its arguments
# three commands separated by a semicolon
echo hello world; echo hello; echo world

# Example: the -n flag
echo hello; echo world; echo -n hello; echo -n world

# Example: combining flags
# cat concatenates and prints files
# -e displays $ at the end of each line
# -n displays the line number
# "cat -en" and "cat -e -n" are equivalent
cat -en hello.txt

# Example: named arguments
# this launched another bash program that runs
# the commandspecified by the -c option then quits
bash -c "ls"

# Example: the man command
man echo

# Example: the version command
man --version
ls --version
