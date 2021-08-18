from __future__ import print_function

import time
import threading
import errno
import sys

import grpc
import protocol_pb2_grpc as chatrpc
import protocol_pb2 as chat

ip = ''
port = ''

while (len(ip) and len(port)) <= 0:
    ip = input('IP: ')
    port = input('PORT: ')

channel = grpc.insecure_channel(ip + ':' + str(port))
stub = chatrpc.ChatServerStub(channel)
chat_list = []


class Client:

    def __init__(self, name: str):
        self.username = name
        threading.Thread(target=self.__listen_for_messages,
                         daemon=True).start()

    def __listen_for_messages(self):
        for data in stub.ChatStream(chat.Empty()):
            if data.name != username:
                print("[{}] {}".format(data.name, data.message))
            chat_list.append("[{}] {}\n".format(data.name, data.message))


if __name__ == '__main__':
    username = None

    while username is None:
        username = input("Username: ")
    c = Client(username)
    try:
        while True:
            message = input('')
            if message != '':
                d = chat.Data()
                d.name = username
                d.message = message
                stub.SendData(d)

    except KeyboardInterrupt:
        print('Keyboard Interrupt, CTRL + C pressed')
        print('Program closed')
        sys.exit()
