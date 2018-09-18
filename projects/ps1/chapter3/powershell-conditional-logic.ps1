"time flies" -like "an arrow"
"fruit flies" -notlike "*lies"
-not ("anything" -match ".*")
Test-Path nonexistent.txt
$?
## False
## False
## False
## False
## True
## 
