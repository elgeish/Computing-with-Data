# Modern Interfaces to C Code

The `.Call` function offers a higher degree of flexibility than `.C` in terms
of passing and returning R arrays or dataframes. The example below shows how
to use `.Call` to implement the same functionality as the `.C` example above.
The type `SEXP` represents an R object. The `REAL` macro returns a pointer
to the corresponding memory for reading or writing to it. Here's an example:

@[]({"project": "R", "stubs": ["chapter7/fooC2.c", "chapter7/fooC2.R"], "command": "R CMD SHLIB chapter7/fooC2.c && Rscript chapter7/fooC2.R 2>/dev/null"})
