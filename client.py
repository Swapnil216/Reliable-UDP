"""
Team Members:
Swapnil Agarwal - 2017B3A71343H
Thribhuvan Reddy M - 2017B3A71116H
Arundhan Reddy M - 2017B3A70889H
Uttam Singh - 2017B4A70683H
Srinivas Konduri - 2017B3A70746H
"""

#Importing Libraries and other files
from pathlib import PurePath
import os
import main
from base64 import b64encode

print("Enter the server address: ")
server_address = input()
server_port = 7080
client_port = 7090
    
    
file = 'data.txt'

client = main.Client(20, 10, 128, client_port)


def process_file(filename):
    with open(filename, 'rb') as f:
        return bytes(f.read())


print('Welcome to the File Sender!')
while True:
    print('Enter path to the file (or type "quit" without quotes to exit):')
    file = input()
    if file.lower() == 'quit':
        break
    _, extension = os.path.split(PurePath(file))
    client.send(extension.encode('utf-8'), server_address, server_port)
    payload = b64encode(process_file(file))
    client.send(payload, server_address, server_port)