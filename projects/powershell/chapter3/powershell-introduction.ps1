# This is a single-line comment
<#
  This is a block comment...
  It can span multiple lines
#>
# The prefix ## indicates an output line
# The Write-Host cmdlet writes output to a PowerShell host
# Host here refers to the process that's hosing PowerShell
Write-Host hello world
## hello world

Write-Host hello; Write-Host world
## hello
## world

# The first cmdlet below has the NoNewLine switch turned on
Write-Host -NoNewLine hello; Write-Host world
## helloworld

# The separator below is added between printed objects
Write-Host -Separator ", " hello world
## hello, world

# 0..9 creates an array of integers from 0 to 9
# Parentheses are required to evaluate the expression correctly
Write-Host -Separator ";" (0..9)
## 0;1;2;3;4;5;6;7;8;9
# The + operator below concatenates ranges
Write-Host -Separator ";" (0..9 + 8..0)
## 0;1;2;3;4;5;6;7;8;9;8;7;6;5;4;3;2;1;0

# The namespace prefix System is optional in PowerShell
Write-Host -Separator ([IO.Path]::PathSeparator) (0..9)
## 0;1;2;3;4;5;6;7;8;9

[String]::Join([IO.Path]::PathSeparator, 0..9)
## 0;1;2;3;4;5;6;7;8;9

# This is also an example of a multi-line entry
# When an entry is incomplete, you'll see this prompt: >>
# To complete the entry, press Enter after the last input
# Get-Date returns a DateTime object
(Get-Date).
AddDays(1).
ToUniversalTime().
ToLongDateString().
ToUpper()
## FRIDAY, MAY 13, 2016

# Example: comparing data extraction with Command Prompt
## rem ^ allows us to escape special characters
## for /f "tokens=4,5" %i in ('dir c:\test') ^
## do @if exist %j if %i neq ^<DIR^> echo %j %i
## bar.txt 22
## foo.txt 3
## 

# dir is an alias for the Get-ChildItem cmdlet
# The output of dir is piped as input to Select-Object
dir | Select-Object Name, Length
## 
## Name           Length
## ----           ------
## bar.txt            42
## foo.txt             3

# Example: getting help
# The output below is truncated for brevity
Get-Help Out-Null
## 
## NAME
##     Out-Null
## 
## SYNOPSIS
##     Deletes output instead of sending it down the pipeline.
## 
## 
## SYNTAX
##     Out-Null [-InputObject [<PSObject>]] [<CommonParameters>]
## (truncated for brevity)
