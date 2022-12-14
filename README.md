Server 
===========================
This are some concurrency experiments with sockets. By a large part inspired (read: copied) from the phenomenal talk: [David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://youtu.be/MCs5OvhV9S4)

There are currently three popular approaches to Python concurrency: threads, event 
loops, and coroutines. Threads are widely known, other options not so much. 

Run Development
========================
```bash
python3 server.py
netcat localhost 25000 # new shell 
netcat localhost 25000 # new shell
```

Or, load test the server a bit:
```bash
python3 server.py
python3 perf2.py  # new shell
```
# Common Issues
## quick commands: restart
In case you get `[Errno 48] Address already in use`, a quick way to restart is to 
just kill the process:


```console
Traceback (most recent call last):
  File "/Users/hslu-n0004890/PYTHON_CONCURRENCY_FROM_THE_GROUND_UP/server.py", line 37, in <module>
    fib_server(("", 25000))
  File "/Users/hslu-n0004890/PYTHON_CONCURRENCY_FROM_THE_GROUND_UP/server.py", line 12, in fib_server
    sock.bind(address)
OSError: [Errno 48] Address already in use

```
Just restart the server:
```console
  ~/ ps aux | grep server.py   
                               
<username>     4622   0.0  0.0 34135432   7552 s003  S+   11:22PM   0:00.04 python3 server.py
  ~/ kill -9 4622  
  ~/ python3 server.py        
                                   
```
