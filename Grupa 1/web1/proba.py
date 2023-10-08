import socket 
s = socket.socket()
s.connect(("127.0.0.1",8000))
s.send(b"POST /HTTP/1.1\r\n\r\n......")