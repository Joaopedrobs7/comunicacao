
from socket import *
from getprice import get_coin_price
import hashlib

def generate_checksum(data):
    return hashlib.md5(data.encode()).hexdigest()

host = gethostname()
port = 5050
addr = (host, port)
format = 'utf-8'
print(f'HOST: {host} PORT: {port}')
disconnect_msg = 'disconnect'

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen(5)

while True:
    con, adr = server.accept()
    con.settimeout(5)  # setting a timeout of 5 seconds

    while True:
        try:
            # Receive and decode the client message with sequence number and checksum
            msg = con.recv(1024).decode(format)
            seq, client_msg, received_checksum = msg.split(';')

            # Check if checksum matches
            if generate_checksum(client_msg) == received_checksum:
                print(f"Mensagem recebida corretamente: {client_msg}")
                con.send(f"ACK{seq}".encode(format))
                
                # Fetch and send coin price
                price_response = get_coin_price(client_msg)
                if price_response:
                    price_response = f"${price_response}"
                else:
                    price_response = "Moeda não encontrada."
                con.send(price_response.encode(format))
            else:
                print("Checksum mismatch, requesting retransmission.")
                con.send(f"NACK{seq}".encode(format))
            
            if client_msg == disconnect_msg:
                con.close()
                break
        except timeout:
            print("Client response timed out.")
            continue

server.close()
