# Moving, Copying, and Removing Files and Directories

```bash runnable
touch file1 /tmp/file1
mkdir ~/tmpFiles

# copy file1 in current dir to file2 in current dir
cp file1 file2  
# copy file1 in /tmp to file2 in ~
cp /tmp/file1 ~/file2  
# rename file1 as file2 in current dir
mv file1 file2  
# move file1 in /tmp to file2 in ~
mv /tmp/file1 ~/file2  
# remove file2 in home dir
rm ~/file2  
# removes directory tmpFiles and all its contents
rm -R ~/tmpFiles 
# same as above but avoids calling an aliased version of rm
\rm -R ~/tmpFiles
```
