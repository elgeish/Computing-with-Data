# Wildcard Characters

```bash runnable
# removes all non-hidden files in directory ~/tmpFiles
rm ~/tmpFiles/*
# removes all hidden files in ~/tmpFiles
rm ~/tmpFiles/.*
# copies all files in ~/tmpFiles whose names end with .html
# to directory /tmp
cp ~/tmpFiles/*.html /tmp/
# remove all files ending with .c or .o
rm *.[co]
# remove files whose extension is a lower-case character
rm *.[a-z]
```
