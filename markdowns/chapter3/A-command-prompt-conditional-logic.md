# Command Prompt - Conditional Logic

```cmd
rem Example: various comparators
set X=10
IF %X% EQU 10 echo X is 10
set Y=bar
IF NOT %Y%==foo echo Y is not foo
IF NOT a==A echo case-sensitive
IF /i a==A echo now equal

rem Example: other checks
IF NOT DEFINED SOME_VAR echo SOME_VAR is not set
IF NOT EXIST some_file.txt echo.>some_file.txt
IF NOT EXIST some_file.txt (echo.>some_file.txt) ^
ELSE echo file already exists
IF %ERRORLEVEL% EQU 0 echo last command succeeded
```
