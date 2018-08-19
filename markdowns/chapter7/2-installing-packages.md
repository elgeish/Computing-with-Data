# Installing Packages

R features easy installation of both core R and third party packages:

```R
# install package ggplot2
install.packages("ggplot2")
# install package from a particular mirror site
install.packages("ggplot2", repos = "http://cran.r-project.org")
# install a package from source, rather than binary
install.packages("ggplot2", type = "source")
library(ggplot2)  # bring package into scope
# display all datasets in the package ggplot2
data(package = "ggplot2")
installed.packages()  # display a list of installed packages
update.packages()  # update currently installed packages
```
