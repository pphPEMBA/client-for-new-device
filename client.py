import time
import sys
import socket
import os
import ctypes

s = socket.socket()
s_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_.connect(("8.8.8.8", 80)) 
host = s_.getsockname()[0]

with open("/home/slaved1/MYPROJECTS/.confidentional/DISMIS-core/System_services/.middleware/port_num.txt",'r') as p_num:
    port_num = p_num.read()
    p_num.close()

port = int(port_num)
s.connect((host, port))
print("")
print(" Connected to server ")

command = s.recv(1024)
command = command.decode()


if command == "shutdown":
    print("")
    print("Shutdown command")
    s.send("Command recieved".encode())
    print('Successful controlling Slave')
    #os.system("poweroff")
        