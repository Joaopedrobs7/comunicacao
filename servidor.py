
from socket import *
from getprice import get_coin_price
import hashlib
import sys

def generate_checksum(data):
    return hashlib.md5(data.encode()).hexdigest()

host = gethostname()
port = 5050
addr = (host, port)
format = 'utf-8'
print(f'HOST: {host} PORT: {port}')
disconnect_msg = 'exit'

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen(5)

while True:
    con, adr = server.accept()
    con.settimeout(10)  # setting a timeout of 5 seconds

    while True:
        try:
            # Receive and decode the client message with sequence number and checksum
            msg = con.recv(1024).decode(format)

            if msg == disconnect_msg:
                print("fechando servidor..")
                server.shutdown(SHUT_RDWR)
                server.close()
                sys.exit(1)


            seq, client_msg, received_checksum = msg.split(';')

            # Check if checksum matches
            if generate_checksum(client_msg) == received_checksum:
                print(f"Message received by client: {client_msg}")
                con.send(f"ACK{seq}".encode(format))
                
                # Fetch and send coin price
                price_response = get_coin_price(client_msg)
                if price_response:
                    price_response = f"${price_response}"
                    
                else:
                    price_response = 'Moeda nao encontrada.'
                con.send(price_response.encode(format))
                
            else:
                print("Checksum mismatch, requesting retransmission.")
                con.send(f"NACK{seq}".encode(format))
            
            
        except timeout:
            print("Client response timed out.")
            continue


