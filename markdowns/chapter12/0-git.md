# Git

```bash
# Example 1 - config
git config --global user.name "John Smith"
git config --global user.email "john@example.com"

# Example 2 - init
# change to parent directory where repository should lie
cd dir_name
# create a new directory representing repository
git init respository_name
# enter directory representng new repository
cd respository_name

# Example 3 - add
touch new_file  # create an empty file
git add new_file  # add new file to staging area
git commit -m "demo commit: adding an empty file new_file"

# Example 4 - status
git status

# Example 5 - another commit
echo 123456 >>! new_file  # add some text to empty file
# commit new version of new_file
git commit -m "added 123456 to file" new_file

# Example 6 - another commit
git commit -a -m "updating multiple files"

# Example 7 - branch
git branch new_branch  # create a new branch
git branch  # list all branches

# Example 8 - rev-parse
git rev-parse master~2 # display SHA-1 codename
git rev-parse --short master~2 # display shortened SHA-1 codename

# Example 9 - reverts to the previous version
git init demo_repos
cd demo_repos
echo 123 > demo_file
git add demo_file
git commit -a -m "adding demo_file containing 123"
echo 456 >>! demo_file
git commit -a -m "adding 456 to demo_file"
cat demo_file
git checkout master~1  # change version to previous version
cat demo_file

# Example 10 - merge
git branch feature1
git checkout feature1 ## Switched to branch 'feature1'
echo abc > feature_file
git add feature_file
git commit -a -m "added feature_file with abc"
git checkout master ## Switched to branch 'master'
git merge feature1  # merge feature1 branch into master
ls  # both files appear in master after the merge

# Example 11 - rebase
git checkout feature1
git rebase master  # rebase master into feature1 branch

# Example 12 - clone
git clone ssh://username@address.com/path/projectName.git

# Example 13 - log
git log | head

# Example 14 - diff
git diff master~1 master | head
```
