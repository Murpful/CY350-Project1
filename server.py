import socket
import random
import time
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message from: ", clientAddress, ": ", message.decode())
    modifiedMessage = message.decode()
    #change ping to pong
    modifiedMessage = modifiedMessage.replace("Ping", "Pong")
    #drop 1/3 of the packets and send the modified message
    if random.randint(1,3) != 1:
        #delay for a random amount of time between 0 and 1 seconds
        time.sleep(random.random())
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

