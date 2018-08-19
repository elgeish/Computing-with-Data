# Command Prompt - Loop

```cmd
rem Example: a for-loop using a counter
for /L %i in (0, 2, 10) do @echo %i

rem Example: a for-loop using a list
FOR %a IN (eggs milk bread) DO @echo %a

rem Example: a for-loop using a text file
(echo eggs & echo milk & echo bread) > lines.txt
for /f %i in (lines.txt) do @echo %i

rem Example: a for-loop used to load a CSV file
echo eggs,milk,bread > data.csv
for /f "delims=, tokens=1-3" %i in (data.csv) do ^
@echo %i & @echo %j & @echo %k

rem Example: a for-loop using the output of a command
FOR /F "delims==" %i IN ('set') DO @echo %i

rem Example: a for-loop using a back-quoted string
FOR /F "usebackq delims==" %i IN (`set`) DO @echo %i
```
