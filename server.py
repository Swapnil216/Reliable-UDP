"""
Team Members:
Swapnil Agarwal - 2017B3A71343H
Thribhuvan Reddy M - 2017B3A71116H
Arundhan Reddy M - 2017B3A70889H
Uttam Singh - 2017B4A70683H
Srinivas Konduri - 2017B3A70746H
"""

#Importing Libraries and other files
import main
from base64 import b64decode


address = '127.0.0.1'
port = 7080
count = 1
outfile = 'recieved_datafile\\'
clients = {}


def handle(key, message):
    global count
    if key in clients:
        with open(clients[key], 'wb') as f:
            for line in message:
                f.write(b64decode(line))
        print('APPLICATION: received file:')
        print(f' {clients[key]} updated by {key}')
        del clients[key]
    else:
        message = ''.join(message)
        line = '-' * 20
        print('APPLICATION: received extension:')
        print(line)
        print(message)
        print(line)
        print(' from ' + key)
        clients[key] = outfile+key.replace(':', '_')+'_'+str(count)+'.'+message
        count = count + 1


server = main.Server(handle)
server.receive(port)