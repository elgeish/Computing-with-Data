# Displaying Files

```bash runnable
echo 'Feb  5 08:01:24 chance rsyslogd: [origin software="rsyslogd"' > /var/log/syslog.1
echo 'Feb  6 07:35:01 chance anacron[7614]: Updated timestamp for' >> /var/log/syslog.1

head -1 /var/log/syslog.1  # first line
tail -1 /var/log/syslog.1  # last line
# count number of messages (first column is number of lines)
wc /var/log/syslog.1
# count number of messages on Feb 6
grep "Feb  6" /var/log/syslog.1 | wc
cat /var/log/syslog.1 | grep "Feb  6" | wc # same as above
```
