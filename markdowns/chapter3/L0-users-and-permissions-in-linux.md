# Users and Permissions in Linux

```bash runnable
touch file.txt

ls -l file.txt

chmod g+w file.txt # add write permission to group
ls -l file.txt

chmod a+w file.txt # add write permission to all users
ls -l file.txt

chmod a-w file.txt # remove write permission from all users
ls -l file.txt

chown guest file.txt
ls -l file.txt
```
