# Processes in Linux - Part II

```bash
# run five jobs sequentially in the foreground
for i in `seq 1 5`; do  (sleep 100) ; done ;

[ hitting CTRL-Z to suspend the job ]

jobs

## [1]+  Stopped                 ( sleep 100 )

bg  # resume process in the background
jobs

## [1]+  Running                 ( sleep 100 ) &

ps  # shows single active process

##   PID TTY           TIME CMD
## 57140 ttys004    0:00.00 sleep 100

# run processes concurrently in the background
# run 5 processes in the background concurrently
for i in `seq 1 5` ; do  (sleep 100 &) ; done ;
ps

##   PID TTY           TIME CMD
## 57148 ttys004    0:00.00 sleep 100
## 57150 ttys004    0:00.00 sleep 100
## 57152 ttys004    0:00.00 sleep 100
## 57154 ttys004    0:00.00 sleep 100
## 57156 ttys004    0:00.00 sleep 100

kill 57148  # kill the first process

ps

##   PID TTY           TIME CMD
## 57150 ttys004    0:00.00 sleep 100
## 57152 ttys004    0:00.00 sleep 100
## 57154 ttys004    0:00.00 sleep 100
## 57156 ttys004    0:00.00 sleep 100

top

## Tasks: 195 total,   2 running, 193 sleeping,   0 stopped,  
## Cpu(s): 69.4%us,  0.3%sy,  0.0%ni, 30.3%id,  0.0%wa,  0.0%hi
## Mem:  99197580k total, 92876600k used,  6320980k free,  
## Swap: 100652028k total,    19548k used, 100632480k free
##
##   PID USER PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+ COMMAND
## 26323 joe  20   0 24.2g 1.2g 9396 S  100  1.3   3546:44 java
## 31696 joe  20   0 24.2g 1.3g 9392 S  100  1.4 874:38.32 java
## 29854 joe  20   0 24.2g 971m 9408 S  100  1.0   1962:39 java
## 29419 joe  20   0 24.2g 992m 9396 S  100  1.0   2204:30 java
```
