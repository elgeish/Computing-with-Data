#!/bin/bash
cd `dirname "$0"`

# compile and link foo.cpp into an executable file named foo
g++ foo.cpp -o foo

# compile (but do not link) the C++ code in foo.cpp 
# into the object file foo.o
g++ -c foo.cpp -o foo.o
# link the object file foo.o and create an executable file foo
g++ foo.o -o foo

# compile multiple C++ files into a single executable, using the C++11 standard,
# optimized compilation, and linking to the standard mathematical library
g++ -o foo -lm -O3 -std=c++0x foo.cpp
# compile and link to create an executable file foo
g++ -o foo foo.cpp
# run the executable file foo (in the current directory)
./foo
# display value returned by the compiled program
echo $?
