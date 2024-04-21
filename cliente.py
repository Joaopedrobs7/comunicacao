from socket import*


host = gethostname()
port = 5050
addr = host,port
format = 'utf-8'


client = socket(AF_INET,SOCK_STREAM)
client.connect(addr)

while 1:
    #manda msg pro servidor
    msg = input("moeda: ")
    client.send(msg.encode(format))
    
    #recebe msg do servidor e printa
    server_msg = client.recv(1024)
    server_msg = server_msg.decode(format)
    print(server_msg)
    
