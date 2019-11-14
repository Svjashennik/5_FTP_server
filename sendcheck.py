import os
import socket

def sendfile(name, who):
    with open(name, 'r') as file:
        for raw in file:
            who.send(raw.encode())
            who.recv(1024)
    who.send('end'.encode())

def checkfile(name, who):
    while True:
        msg = who.recv(1024).decode()
        if msg == 'end':
            break
        else:
            with open (name, 'a') as file:
                file.write(msg)
                who.send('next'.encode())
