# Command Prompt - Introduction

To start Command Prompt, open the Start menu and search for `cmd`; the search
results should contain an entry for Command Prompt.

```cmd
rem This is a comment
rem The prefix ## indicates an output line
rem The echo command displays its arguments
echo hello world

rem Example: run multiple commands on the same line
echo hello & echo world

rem Example: the dir command
rem The current directory is C:\test
rem The "." entry is a reference to the current directory
rem The ".." entry is a reference to the parent directory
dir

rem Example: specifying options
rem Options are specified using a slash
rem The /b option instrcuts dir to use a bare format
dir /b

rem Example: combining options
rem The /a option instrcuts dir to show all contents
rem The /b option instrcuts dir to use a bare format
dir /a /b

rem Example: sorting the output of dir
rem The /a option instrcuts dir to show all contents
rem The /b option instrcuts dir to use a bare format
rem The /o:s option instrcuts dir to sort by file size
dir /a /b /o:s

rem Example: getting help
rem The /? option instrcuts tree to show its help message
tree /?
help help
```
