# Assign the value 13 to $var then read it
$var = 13
$var
## 13

# Assign the value 42 to ${a$b} then read it
${a$b} = 42
${a$b}
## 42

$x = 3
$x.GetType().Name
$x = "hello world"
$x.GetType().Name
## Int32
## String

# Define $t to be of type [DateTime]
[DateTime]$t = (Get-Date) # Use () to evaluate the cmdlet first
$t = "5/23/2016" # Valid conversion from String
$t
$t = "hello world" # Error
## 
## Monday, May 23, 2016 12:00:00 AM
## Cannot convert value "hello world" to type "System.DateTime".
## (truncated for brevity)

# Example: data validation
[ValidateRange(1, 118)][int]$atomicNumber = 1
$atomicNumber = 119 # Error
## The variable cannot be validated because the value 119
## is not a valid value for the atomicNumber variable.
## (truncated for brevity)

# A variable in PowerShell can have a description
Set-Variable Mg -option ReadOnly `
	-description "Magnesium" -value 12
$Mg
$Mg = 13 # Error
## 12
## Cannot overwrite variable Mg because it is read-only
## or constant.
## (truncated for brevity)

# Example: string concatenation
$x = 1
$y = 2
Write-Host ("x = " + $x + ", y = " + $y)
## x = 1, y = 2

# Example: formatting a string
Write-Host "x = $x, y = $y"
## x = 1, y = 2

# Example: escaping
Write-Host "`$x = $x, `$y = $y"
## $x = 1, $y = 2

# Example: literal strings
Write-Host '$x is a variable'
## $x is a variable

# Example: list all variables
$a = 1
# Get the content of the virtual drive (variable:)
dir variable:
## 
## Name                           Value
## ----                           -----
## $                              1
## ?                              True
## ^                              $a
## a                              1
## args                           {}
## ConfirmPreference              High
## (truncated for brevity)

# Example: test for a variable's existence
Test-Path variable:nonexistent
## False

# Example: deleting a variable
Test-Path variable:x
del variable:x
Test-Path variable:x
## True
## False
