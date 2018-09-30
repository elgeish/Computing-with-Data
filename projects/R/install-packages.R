local({r <- getOption("repos")  ## assign default repo
    r["CRAN"] <- "http://cran.r-project.org"
    options(repos=r)
})
install.packages("Ecdat")
install.packages("GGally")
install.packages("ggplot2")
install.packages("ggplot2movies")
install.packages("tikzDevice")
