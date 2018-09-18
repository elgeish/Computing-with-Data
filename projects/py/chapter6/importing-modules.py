import my_vars
# accessing variables in my_vars module
area = my_vars.LENGTH * my_vars.WIDTH

# the following imports the module using an alias
import my_vars as mv
area = mv.LENGTH * mv.WIDTH 

# the following makes the definition x in the current module
# accessible without the need for its prefix
from my_vars import LENGTH, WIDTH
area = LENGTH * WIDTH  

from my_vars import *
area = LENGTH * WIDTH
