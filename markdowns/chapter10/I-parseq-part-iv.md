# ParSeq - Part IV

ParSeq really shines when used to perform asynchronous operations (e.g., I/O)
in parallel, especially in the context of a large-scale system that requires
special consideration for fault tolerance and other design requirements.
Let's take the following code snippet as an example:

@[]({"project": "java", "stubs": ["chapter10/parseq-part-iv.java"], "command": "./run-with-parseq chapter10/parseq-part-iv"})
