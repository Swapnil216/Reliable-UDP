"""
Team Members:
Swapnil Agarwal - 2017B3A71343H
Thribhuvan Reddy M - 2017B3A71116H
Arundhan Reddy M - 2017B3A70889H
Uttam Singh - 2017B4A70683H
Srinivas Konduri - 2017B3A70746H
"""

#Importing Libraries and other files
import socket
import hashlib
import time

#Encoding used to encode and decorde the transferred messages
codec = 'utf-8'

#Client Specifications
def makeSegments(message, maxSegmentSize):
    segmentList = list()
    print('length of message is ' + str(len(message)))
    for i in range(0, len(message), maxSegmentSize):
        segmentList.append(message[i:i + maxSegmentSize])
    return segmentList


class Client:
    windowSize = 20
    timeOutValue = 10
    maxSegmentSize = 128

    def __init__(self, windowSize, timeOutValue, maxSegmentSize, portNumber):
        self.windowSize = windowSize
        self.timeOutValue = timeOutValue
        self.maxSegmentSize = maxSegmentSize
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientSocket.bind(('', portNumber))
        self.clientSocket.settimeout(self.timeOutValue)
        print('Client bound! Ready to send!')


    def send(self, message, IPAddress, portNumber):
        highestAckRecieved = 1
        recievedAcks = list()
        base = 1
        nextSequenceNumber = 1
        i = 1
        sentPackets = list()

        segmentList = makeSegments(message, self.maxSegmentSize)
        totalNoOfPackets = len(segmentList)
        start_time = time.time()

        while i <= totalNoOfPackets or len(recievedAcks)<totalNoOfPackets:
            #If total file transfer exceeds 30 sec, the code will timeout and exit
            if start_time-time.time() > 30 :
                print("Taking too much time")
                break

            try:
                if nextSequenceNumber - base < self.windowSize and i<=totalNoOfPackets:
                    checksum = hashlib.md5(segmentList[i - 1]).hexdigest()
                    pkt = str(nextSequenceNumber) + ":;:" + str(totalNoOfPackets) + ":;:" + str(checksum) + ":;:" + \
                        segmentList[i - 1].decode(codec)

                    pkt = pkt.encode(codec)
                    print('Message prepared! Sending!')
                    # print('message data ' + str(pkt))
                    self.clientSocket.sendto(pkt, (IPAddress, portNumber))
                    print('Message sent! Waiting for acknowledgment')
                    sentPackets.append(pkt)
                    nextSequenceNumber = nextSequenceNumber + 1
                    i = i + 1
                    
                response, addr = self.clientSocket.recvfrom(1024)
                print("************************************************************************************")
                print('response received! decoding!')

                response = response.decode(codec)
                print('Decoded response is ' + response)

                if "Bit Error" not in response:
                    ackNumber = int(response)
                    recievedAcks.append(ackNumber)
                    if ackNumber > highestAckRecieved:
                        highestAckRecieved = ackNumber
                    recievedAcks.sort()
                    for b in range(base - 1, len(recievedAcks)):
                        if recievedAcks[b] == b + 1:
                            base = b + 2

            except Exception as e:
                self.clientSocket.sendto(sentPackets[base - 1], (IPAddress, portNumber))

				
        end_time = time.time()
        print("Maximum Segment Size Used: " + str(self.maxSegmentSize) + " bytes")
        print("Total Number of Packets Sent: " + str(totalNoOfPackets))
        print("Total time taken to send message: " + str(end_time-start_time) + " seconds")
        print("************************************************************************************\n")


#Server Specifications
class Server:
    def __init__(self, out):
        self.data_store = {}
        self.out = out


    def handler(self, key, seq, total, val):
        """
        :param key: tuple containing ip-address::port
        :param seq: seq num of pkt
        :param total: size of message
        :param val: message value
        """

        if key not in self.data_store:
            self.data_store[key] = [total]
        else:
            if self.data_store[key][0] != total:
                print('APPLICATION: Malfunctioned up with ' + key)

        if (seq,val) not in self.data_store[key]:
            self.data_store[key].append((seq, val))

        if len(self.data_store[key]) == self.data_store[key][0] + 1:
            output_list = self.data_store[key][1:]
            output_list.sort()
            _, output_list = zip(*output_list)
            self.out('::'.join(map(str, key)), output_list)
            del self.data_store[key]


    def receive(self, portNumber, seqHandler=handler):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.bind(('', portNumber))
        print('Socket bound!')

        while True:
            print('Listening now')
            pkt, addr = serverSocket.recvfrom(1024)
            print('PKT received!')
            pkt = pkt.decode(codec)
            # print('decoded pkt is ' + pkt)
            
            #Extracting the data, along with the payload, from the received packed packet
            sequenceNumber = pkt.split(':;:')[0]
            totalNoOfPackets = pkt.split(':;:')[1]
            checksum = pkt.split(':;:')[2]
            msg = pkt.split(':;:')[3]
            # print('message is ' + msg)
            
            if hashlib.md5(msg.encode(codec)).hexdigest() == checksum:
                print('checksum checks out, sending acknowledgement ' + sequenceNumber)
                serverSocket.sendto(sequenceNumber.encode(codec), addr)
                seqHandler(self, addr, int(sequenceNumber), int(totalNoOfPackets), msg)

            else:
                print('Bit Error encountered!')
                serverSocket.sendto("Bit Error".encode(codec), addr)




