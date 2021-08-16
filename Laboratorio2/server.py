from concurrent import futures

import time
import sys
import grpc
import protocol_pb2_grpc as chatrpc
import protocol_pb2 as chat

class ChatServer(chatrpc.ChatServerServicer):

    def __init__(self):
        self.chats = []

    def ChatStream(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def SendNote(self, request: chat.Note, context):
        print("[{}] {}".format(request.name, request.message))
        self.chats.append(request)
        return chat.Empty() 


if __name__ == '__main__':
    port = 4444
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  #max workers = number of clients able to connect
    chatrpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print('Starting server')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        try:
            time.sleep(64 * 64 * 100)

        except KeyboardInterrupt:
            print('Keyboard Interrupt, CTRL + C pressed')
            server.stop()
            sys.exit()