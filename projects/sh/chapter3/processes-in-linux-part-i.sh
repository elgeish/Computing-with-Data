touch a.txt; touch b.txt  # create two empty files
tail -f a.txt &  # launch a never-ending background job
jobs  # display current jobs

## [1]+  Running                 tail -f a.txt &

ps  # display current processes launched by current user

##   PID TTY           TIME CMD
## 11185 ttys005    0:00.00 tail -f a.txt

ps -A | head -n 7 # display all running processes (first 7 lines)

##   PID TTY           TIME CMD
##     1 ??         0:10.84 /sbin/launchd
##    10 ??         0:00.79 /usr/libexec/kextd
## (truncated for brevity)

tail -f b.txt &  # launch another never-ending background job
jobs  # displays current jobs

## [1]-  Running                 tail -f a.txt &
## [2]+  Running                 tail -f b.txt &

kill %1  # kill job 1
jobs

## [1]-  Terminated: 15          tail -f a.txt
## [2]+  Running                 tail -f b.txt &

jobs

## [2]+  Running                 tail -f b.txt &

fg  # bring the single current job into foreground

## [CTRL+z keystroke suspends foreground job
## and creates a new prompt]

jobs  # job was suspended by CTRL+z keystroke

## [2]+  Stopped                 tail -f b.txt

bg  # resume single current job in the background
jobs

## [2]+  Running                 tail -f b.txt &
