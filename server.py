# server.py
# fibonacci microservice
from socket import *
from threading import Thread
from fib import fib


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        # kind of a one liner thing:
        Thread(target=fib_handler, args=(client,), daemon=True).start()


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        try:
            n = int(req)
            result = fib(n)
            resp = str(result).encode("ascii") + b'\n'
            client.send(resp)
        except ValueError:
            print("nope")

    print("closed")


fib_server(("", 25000))
