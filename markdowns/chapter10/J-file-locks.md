# File Locks

In Java, we will use the `java.nio.channels.FileLock` class to demonstrate
how to use it as a mutex that protects a critical section; this time around,
only a single process can be inside said critical section:

@[]({"project": "java", "stubs": ["chapter10/file-locks.java", "chapter10/run-file-locks-example.sh"], "command": "./run-three-in-parallel chapter10/file-locks"})
