# Example: the seq command
seq 1 5
echo seq 1 5
echo `seq 1 5`

# Example: for-loops
for i in `seq 1 5`;  do echo the current number is $i; done
# parentheses start a new sub-shell
for i in `seq 1 5`;  do (echo the current number is $i| wc); done

# Example: while-loops
i=0; while [ $i -lt 5 ]; do  echo $i; let i=i+1; done

# Example: until-loops
i=0; until [ $i -ge 5 ]; do echo $i; let i=i+1; done
