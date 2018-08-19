# Bash - Pipes

The following example shows a piped combination of the `echo` command,
and the `wc` command, which prints the number of lines, words, and characters
in its input:

```bash runnable
echo a sentence with 8 words and 42 characters
# count lines, words, characters in the following sentence
echo a sentence with 8 words and 42 characters | wc
# feed the output of the piped combination above to another wc command
echo a sentence with 8 words and 42 characters | wc | wc
# and so on
echo a sentence with 8 words and 42 characters | wc | wc | wc
```
