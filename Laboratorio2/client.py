from __future__ import print_function

import time
import threading
import errno
import sys

import grpc
import protocol_pb2_grpc as chatrpc
import protocol_pb2 as chat

address = '127.0.0.1'  # IP of the server
port = 4444  # PORT of the server
channel = grpc.insecure_channel(address + ':' + str(port))
conn = chatrpc.ChatServerStub(channel)
chat_list = []

class Client:

    def __init__(self, u: str):
        self.username = u
        self.conn = chatrpc.ChatServerStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        for note in self.conn.ChatStream(chat.Empty()):
            if note.name != username:
                print("[{}] {}".format(note.name, note.message))
            chat_list.append("[{}] {}\n".format(note.name, note.message))

if __name__ == '__main__':
    username = None
    while username is None:
        username = input("Username: ")
    c = Client(username)
    try:
        while True:
            message = input('')
            if message != '':
                n = chat.Note()
                n.name = username
                n.message = message
                conn.SendNote(n)
            

    except KeyboardInterrupt:
        print('Keyboard Interrupt, CTRL + C pressed')
        print('Program closed')
        sys.exit()
