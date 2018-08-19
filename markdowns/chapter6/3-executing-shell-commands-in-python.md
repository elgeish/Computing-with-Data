# Executing Shell Commands

Shell commands can be executed from within Python using the function
`system("shell command")`, which is defined in the module `os`. A newer
alternative to `os.system` that provides much more flexible functionality is
the `call` function, which is defined in the `subprocess` module:

```python runnable
import os
os.system("ls -al")  # call shell command ls -al

import subprocess as sp
sp.call(["ls", "-al"])
```
