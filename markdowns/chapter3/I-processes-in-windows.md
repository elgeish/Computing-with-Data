# Processes in Windows

```cmd
rem Example: start a new window to run a command
start cmd /c "echo poof"

rem Example: start a new window to run a command and pause
start cmd /c "echo poof && pause"

rem Example: start a command without creating a new window
start /b powershell "sleep 1; echo done"

rem Example: query the currently running processes
tasklist /FI "PID eq 4"
```
