import base64

def encrypt_data(data):
    encoded_data = base64.b64encode(data.encode())
    return encoded_data.decode()