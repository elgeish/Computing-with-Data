# show path to file matching command ls
which ls

# display PATH variable (note the current directory is the third
# directory in the list below, denoted by the period notation)
echo $PATH

# add the directory /home/joe/bin to PATH
export PATH=$PATH:/home/joe/bin
echo $PATH
