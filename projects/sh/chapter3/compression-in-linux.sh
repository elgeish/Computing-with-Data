echo "Call me Ishmael.
Some years ago—never mind how long precisely—
having little or no money in my purse," > mobyDick.txt

cat mobyDick.txt | head -n 1 # first line

bzip2 -v mobyDick.txt # compress .txt to .txt.bz2

# first line of compressed file
cat mobyDick.txt.bz2 | head -n 1

# using bzcat to display compressed file
bzcat mobyDick.txt.bz2 | head -n 1

mkdir tmp tmp2
echo "hello" > tmp/hello.txt
# pack all files in tmp/ into a file archive.tar
tar cvf archive.tar tmp/*
# compress the file archive.tar (creating archive.tar.bz2)
bzip2 archive.tar
# uncompress archive.tar.vz2
bunzip2 archive.tar.bz2
# moves archive.tar.bz2 to subdirectory tmp2
mv archive.tar tmp2 
# change current directory to tmp2
cd tmp2
# unpack the tar file archive.tar in current directory
tar xvf archive.tar
