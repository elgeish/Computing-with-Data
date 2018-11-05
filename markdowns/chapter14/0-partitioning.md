# Partitioning

To illustrate how this partitioning scheme allows for a balanced cluster
assignment, we used [4450 email addresses](https://github.com/elgeish/Computing-with-Data/blob/master/projects/py/chapter14/enron.txt)
from the [Enron dataset](https://en.wikipedia.org/wiki/Enron_Corpus) to simulate
arbitrary email addresses (keys) and we calculated how they would be assigned
across our 5 clusters using the Python script below:

@[]({"project": "py", "stubs": ["chapter14/partitioning.py"], "command": "python chapter14/partitioning.py"})
