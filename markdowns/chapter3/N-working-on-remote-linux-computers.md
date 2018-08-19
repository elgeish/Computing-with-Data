# Working on Remote Linux Computers

```bash
ssh joe@server1.domain.com

# copy file /home/joe/file1 from server1.domain.com 
# (authenticating as user joe) to local home directory
scp joe@server1.domain.com/home/joe/file1 ~/
# copy entire home directory (including sub-directories)
# on server1.domain.com to local ~/tmp
scp -R joe@server1.domain.com/home/joe/* ~/tmp/
# copy local files ~/file2.* to home directory on remote computer
scp ~/file2.* joe@server1.domain.com/home/joe/
```
