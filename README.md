# python-concurrency

This repository unites several experiments related to concurrency in python. By a large part inspired (read: copied) from this phenomenal talk:

### [David Beazley - Python Concurrency From the Ground Up (Youtube Link)](https://youtu.be/MCs5OvhV9S4)

There are currently three popular approaches to Python concurrency: 
- Threads
- event loops
- coroutines. 

The former being extensively recognized and utilized, whereas the latter alternatives are infrequently observed in their natural habitat. 

## Run Development

```bash
python3 server.py
netcat localhost 25000 # open in new shell 
netcat localhost 25000 # open in new shell
```

Or, load test the server a bit:
```bash
python3 server.py
python3 perf2.py  # new shell
```
