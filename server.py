#!/usr/bin/env python3

import socket
import thereading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0, 0, 0, 0', 10000))
        self.sock.listen(1)
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connections in self.connections:
                connections.send(data)
            if not data:
                print(str(a[0]) + ': ' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = thereading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ': ' + str(a[1]), "connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = thereading.Thread(target = self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data, 'utf-8')

if(len(sys.argv) > 1)
    client = Client(sys.argv[1])
else:
    while True:
        print "Enter help for usage, enter continue to start the server."
            action = raw_input()
                if action == "help":
                    print("Enter your message, all users will receive.")
                elif action == "continue":
                    break

    server = Server()
    server.run()
        

