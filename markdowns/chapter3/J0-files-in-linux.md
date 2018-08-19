# Files in Linux

```bash runnable
cd /  # change current directory to top-most directory
pwd  # display current path

cd /home  # change directory using absolute path
pwd  # display current path

mkdir /home/joe
cd joe  # change directory using relative path
pwd  # display current path

mkdir /home/jane
cd ../jane  # change directory using relative path
pwd  # display current path

# display the size of the disk drive and amount of used and 
# available space using abbreviations such as Gi for Gigabyte
df -h ~/
du -sh ~/
```
