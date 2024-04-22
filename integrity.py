import hashlib

def integrity_check(data,received_checksum):
    
    checksum = hashlib.md5(data.encode()).hexdigest()
    if checksum == received_checksum:
        return True
    else:
        return False
    