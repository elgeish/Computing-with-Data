# Test Hooks - Part II

To properly test the use of the timestamp, we follow the dependency inversion
principle again here and a test hook to set an instance of the `Clock` abstract
class we use for generating the creation timestamp:

@[]({"project": "java", "stubs": ["chapter11/test-hooks-part-ii.java"], "command": "./test chapter11/test-hooks-part-ii"})
