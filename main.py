import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',2000))
server.listen(4)
print('Working')
client_socket, adress = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)
TmRx ='HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Well Buddy'.encode('utf-8') 
client_socket.send(TmRx.encode('utf-8') + content)
print('Shutdown this shit...')