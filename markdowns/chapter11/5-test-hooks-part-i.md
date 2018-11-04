# Test Hooks - Part I

For example, if we want to record the timestamp at which a reminder is inserted
in the database, we need to control what value is sent to the database
at the time of insertion. The below example shows an incomplete way
of verifying the behavior:

@[]({"project": "java", "stubs": ["chapter11/test-hooks-part-i.java"], "command": "./test chapter11/test-hooks-part-i"})
