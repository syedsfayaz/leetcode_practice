Given
two
log
files, start
containing
start
records and stop
containing
stop
records, find
the
average
transaction
duration
for a specific IP address.The file format is CSV, with each row containing transaction ID (xid), timestamp, and client IP address.

2022 / 01 / 20: 00:01: 01

Start_log
transaction
ID(xid), timestamp, and client
IP
address

1
10: 00
am
0.0
.0
.0
2
10: 00
am
0.0
.0
.0

Stop_log

transaction
ID(xid), timestamp, and client
IP
address

1
10: 00
pm
0.0
.0
.0

start_time = {"ip1": [duration, duration], "ip2": [duration, duration]}
stop_time = {"ip1": [duration, duration], "ip2": [duration, duration]}

with open(start.log as f):
    for items in f:
        if items[-1] not in start_time:
            start_time[items[-1]] = items[0]
        start_time[items[-1]].append(items[0])

with open(stop.log as f):
    for items in f:
        if items[-1] not in start_time:
            stop_time[items[-1]] = items[0]
        stop_time[items[-1]].append(items[0])


def avg_time(start_time, stop_time):
    for ip_address,
