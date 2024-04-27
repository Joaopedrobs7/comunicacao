
from socket import *
import hashlib
import sys

def generate_checksum(data):
    return hashlib.md5(data.encode()).hexdigest() 

host = gethostname()
port = 5051
addr = (host, port)
format = 'utf-8'

client = socket(AF_INET, SOCK_STREAM)
client.settimeout(10)  # setting a timeout of 10 seconds
client.connect(addr)

sequence_number = 0

while True:
    msg = input("moeda: ")
    if msg == 'exit':
        client.send(msg.encode(format))
        client.shutdown(SHUT_RDWR)
        sys.exit(1)
        
        
        
    checksum = generate_checksum(msg)
    message = f"{sequence_number};{msg};{checksum}"
    #message = f"{sequence_number};{msg};{5}" 
    client.send(message.encode(format))
    
    
    


    
    # Wait for server ACK
    try:
        server_msg = client.recv(1024).decode(format)
        if server_msg == f"ACK{sequence_number}":
            print(f"Message received by server.")
            print(server_msg)
            
            server_msg = client.recv(1024)
            server_msg.decode(format)
            print(server_msg.decode())
        
        elif server_msg == f"NACK{sequence_number}":
            print("Transmission error, please resend.")
            print(server_msg)
            continue
        sequence_number += 1
    except timeout:
        print("Server response timed out.")
        continue


