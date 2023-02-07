_This is based heavily on https://docs.python.org/3/library/socket.html#example_

We'll start by setting up a basic client and server:

- The server will wait to receive a message, and then will display it
- The client will transmit a message.

The server must be run first. If you've been using the VS Code "Run" button, 
I recommend that you instead use the terminal to run the programs directly, since
the run button works strangely for cases when you're running two programs 
simultaneously.

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
