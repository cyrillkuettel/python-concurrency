# Socket type 

AF_INET vs AF_UNIX:
Tldr: Unix sockets are the way to go on local machines.
https://stackoverflow.com/q/21032562/8765729

If you want to communicate with a remote host, then you will probably need an `INET` socket.

The difference is that an `INET` socket is bound to an IP address-port tuple, while a `UNIX` socket is "bound" to a special file on your filesystem. Generally, only processes running on the same machine can communicate through the latter.

So, why would one use a `UNIX` socket? Exactly for the reason above: communication between processes on the same host, being a lightweight alternative to an `INET` socket via loopback.
