from socket import *
from getprice import *

host = gethostname()


port = 5050
addr = host,port
format = 'utf-8'
print(f'HOST: {host} PORT: {port}')
disconnect_msg = 'disconnect'


server = socket(AF_INET,SOCK_STREAM)

server.bind(addr)
server.listen(5)

while 1:
    con , adr = server.accept()
    while 1:
        #recebe decodifica e printa msg do cliente
        msg = con.recv(1024)#1024bytes
        msg = msg.decode(format)
        print(f'Mensagem recebida: {msg}')
        
        #manda msg pro cliente
        server_msg = str(get_coin_price(msg))
        #server_msg = input("preco: ")
        print("Enviando Preco ao cliente..")
        
        if server_msg!= 'None':
            server_msg = '$' + server_msg
            server_msg = con.send(server_msg.encode(format))
        else:
            server_msg = 'Moeda não encontrada.'
            server_msg = con.send(server_msg.encode(format))


        
        if msg == disconnect_msg:
            con.close()
            server.close()
