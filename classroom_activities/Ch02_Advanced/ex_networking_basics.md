_This is based heavily on https://docs.python.org/3/library/socket.html#example_

We'll start by setting up a basic client and server:

- The server will wait to receive a message, and then will display it
- The client will transmit a message.

## Step 1: Local test

Name this "basic_net_server.py":

```python3
import socket

print("Ready to receive a client connection.")
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    print(data.decode())
    conn.close()
```

Name this "basic_net_client.py":

```python3
import socket

HOST = 'localhost'
PORT = 50007              # The same port as used by the server
print("About to connect...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello, world'.encode("UTF"))
    print("Message sent.")
```

The server must be run first. You may be accustomed to using the VS Code "Run" button, which works well when running a single Python program, but is not as helpful when running multiple Python programs.

Instead, I recommend that you use the following method:

1. Open two terminals
2. cd into the directory that has the python files
3. In one terminal: `python3 basic_net_server.py`
4. In the other terminal: `python3 basic_net_client.py`

## Step 2: To someone else's computer

Find out your ip address by running `ip a` in the terminal.

It will look like this: `192.168.xxx.xxx`

Change the "localhost" on the **client** to be the ip address of someone else, and test it again.

Example:

```python3
HOST = '192.168.3.4'
```

## Step 3: Using `input` and making the communication bidirectional

Updated server:

```python3
import socket

print("Ready to receive a client connection.")
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr, 'and waiting for a message')
    while True:
        data = conn.recv(1024)
        print(data.decode())
        mymessage = input("What say? ")
        conn.sendall(mymessage.encode("UTF"))
        ## Notice that we do need to run `conn.close()` at some point.
```

Updated client:

```python3
import socket

HOST = 'localhost'
PORT = 50007              # The same port as used by the server
print("About to connect...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mymessage = input("What say? ")
        s.sendall(mymessage.encode("UTF"))
        print("Message sent. Awaiting reply:")
        data = s.recv(1024)
        print(data.decode())
```


## Retrying a client connection:


```python3
import socket
import time


waitTime = 2
HOST = "127.0.0.1"
PORT = 5000
ADDR = (HOST, PORT)
sock = socket.socket(AF_INET, SOCK_STREAM)
sock.settimeout(0)

print("about to connect...")
while True:
    try:
        sock.connect(ADDR)
        break
    except BlockingIOError:
        print(f"connection failed. Trying again after {waitTime} seconds.")
        time.sleep(waitTime)
print("connected.")
sock.close()
print("closed.")
```
