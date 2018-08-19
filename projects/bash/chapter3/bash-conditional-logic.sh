# Example: if-else statements
a=4 ; b=3 ; if [ $a -eq $b ] ; then echo 1 ; else echo 0 ; fi

# Example: logical operators
a=4 ; b=3 ; [ $a -eq $b ] && echo 1 || echo 0

# Example: brace expansion
echo {b,c}; echo a{b,c}d; echo a{a..m}d
