# Example: read a text file line by line using a for-loop
f = open("mobydick.txt", "r")  # open file for reading
words = []
for line in f: # iterate over all lines in file
  words += line.split()  # append the list of words in line
f.close()

# Example: the with statement
with open("mobydick.txt") as f:  # "rt" is the default mode
  words = [word for line in f for word in line.split()]

# Example: writing to a file
with open("output.txt", "w") as f:
  f.write("first line\n")
  f.writelines(["second line\n", "third line\n"])

with open("output.txt") as f:
  print(f.read())
