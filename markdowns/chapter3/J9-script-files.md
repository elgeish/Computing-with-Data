# Script Files

```bash runnable
echo '#!/usr/bin/env bash
echo this is a bash script file that accepts two arguments
echo $1 $2' > printTwoArgs

chmod a+x printTwoArgs  # add executable permission to scriptFile
./printTwoArgs one two  # executing script by listing its path
```
