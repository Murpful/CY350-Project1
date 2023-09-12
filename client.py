import socket
import time

serverName = 'localhost'
serverPort = 12000

#set up the socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.connect((serverName, serverPort))
#create time string in the format day_of_month hrs:min:sec abbreviated month name year
numberOfPings = 10
numberOfResponses = 0
successRate = 0
MaxRTTime = 0
MinRTTime = 1
AverageRTTime = 0
#send and recieve messages 10 times
for i in range(numberOfPings):
    timeString = time.strftime("%d %H:%M:%S %b %Y", time.localtime())
    message = "Ping " + str(i+1) + " " + timeString
    clientSocket.send(message.encode())
    timeSent = time.time()
    #attempt to recieve message from server
    try:
        modifiedMessage = clientSocket.recv(1024).decode()
        timeRecieved = time.time()
        RTTime = timeRecieved - timeSent
        if RTTime > MaxRTTime:
            MaxRTTime = RTTime
        if RTTime < MinRTTime:
            MinRTTime = RTTime
        AverageRTTime += RTTime
        print('From Server: ', modifiedMessage)
        numberOfResponses += 1
    except:
        print("Ping " + str(i+1) + " No Response")
    #delay for 1 second
    time.sleep(1)
#close the connection
successRate = numberOfResponses/numberOfPings
successRate = successRate*100
AverageRTTime = AverageRTTime/numberOfResponses
print("Number of messages sent: " + str(numberOfPings))
print("Number of messages responded to: " + str(numberOfResponses))
print("Success Rate: " + str(successRate) + "%")
print("Max RTT: " + str(MaxRTTime))
print("Min RTT: " + str(MinRTTime))
print("Average RTT: " + str(AverageRTTime))
clientSocket.close()
