# Soft Links

```bash runnable
touch /tmp/file1 /tmp/file2
ln -s /tmp tmpLink # create a link tmpLink to the directory /tmp
ls /tmp  # display files in /tmp directory
# enter the directory /tmp by referencing the softlink tmpLink
cd tmpLink
ls
```
