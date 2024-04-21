
from socket import *
import hashlib

def generate_checksum(data):
    return hashlib.md5(data.encode()).hexdigest()

host = gethostname()
port = 5052
addr = (host, port)
format = 'utf-8'

client = socket(AF_INET, SOCK_STREAM)
client.settimeout(10)  # setting a timeout of 5 seconds
client.connect(addr)

sequence_number = 0

while True:
    msg = input("moeda: ")
    if msg == 'exit':
        break
    checksum = generate_checksum(msg)
    message = f"{sequence_number};{msg};{checksum}"
    client.send(message.encode(format))
    
    


    

    # Wait for server ACK
    try:
        server_msg = client.recv(1024).decode(format)
        if server_msg == f"ACK{sequence_number}":
            print("Message received by server.")
            
            server_msg = client.recv(1024)
            server_msg.decode(format)
            print(server_msg)
        
        elif server_msg == f"NACK{sequence_number}":
            print("Transmission error, resending...")
            continue
        sequence_number += 1
    except timeout:
        print("Server response timed out.")
        continue

client.close()
