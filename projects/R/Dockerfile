FROM r-base

RUN apt-get -qq update
RUN apt-get -qq install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texinfo
COPY . .
RUN Rscript --no-init-file install-packages.R
