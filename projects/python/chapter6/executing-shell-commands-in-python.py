import os
os.system("ls -al")  # call shell command ls -al

import subprocess as sp
sp.call(["ls", "-al"])
