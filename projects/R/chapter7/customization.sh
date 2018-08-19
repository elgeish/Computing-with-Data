#!/bin/bash
set -e
cp /project/target/chapter7/.Rprofile ~/.Rprofile
Rscript /project/target/chapter7/pi.R
