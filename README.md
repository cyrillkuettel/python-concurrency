Server 
===========================
demonstrating multiple concurrency patterns
There are currently three popular approaches to Python concurrency: threads, event 
loops, and coroutines 

Run
========================
```bash
python3 server.py
netcat localhost 25000 # new shell 
netcat localhost 25000 # new shell
```

quick commands: restart
===========================
If you want to restart it.

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
  ~/ kill 4622  
  ~/ python3 server.py        
                                   
```
