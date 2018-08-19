# Interfacing with C Code

For example, consider the task of computing some function given two vectors
`a` and `b` of size `n`. The C code to compute the result appears below
(`fooC.c`); note the presence of the pre-processor directive `include <R.h>`.
You may execute code from `fooC.R` after running the command `R CMD SHLIB fooC.c`; the runnable example below runs that command for you:

@[]({"project": "R", "stubs": ["chapter7/fooC.c", "chapter7/fooC.R"], "command": "R CMD SHLIB chapter7/fooC.c && ./run-with-tikz-viewer chapter7/fooC.R 2>/dev/null"})
