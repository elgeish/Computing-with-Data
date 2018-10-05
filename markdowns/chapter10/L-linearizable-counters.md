# Linearizable Counters

We can create a znode for our counter and use Curator to commit a dummy
transaction:

@[]({"project": "java", "stubs": ["chapter10/linearizable-counters.java"], "command": "./run-with-zookeeper chapter10/linearizable-counters"})
