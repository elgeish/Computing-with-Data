# Files in Windows

To view the logical volumes, the following query uses WMIC (Windows Management
Instrumentation Command-line) to list the names of logical volumes:

```cmd
wmic logicaldisk get name
## Name
## C:
## D:
## 
```
