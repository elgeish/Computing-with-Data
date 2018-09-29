# modifying the class path in bash, using : as separator 
# (period corresponds to current directory)
export CLASSPATH=/home/joe/classes:/home/jane/classes:.

# alternatively, the class path can be passed as an 
# argument to java
java -cp /home/joe/classes:/home/jane/classes:. program.java
