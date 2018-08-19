echo hello >> output.txt
echo world >> output.txt
cat output.txt

# create a text file and then print it in uppercase
echo this is a text file > a.txt
tr "a-z" "A-Z" < a.txt

# convert text file to a sorted list of distinct words
# annotated with their count
echo this file is a text file > b.txt
tr < b.txt -cs "[:alpha:]" "\n" | sort | uniq -c

tr < b.txt -d ' ' # remove all white spaces
