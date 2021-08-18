import socket  # To manage sockets
import select  # To manage many connections on any system
import errno
import sys

HEADER_LENGTH = 10

IP = ""
PORT = ""

while (len(IP) and len(PORT)) <= 0:
    IP = input("IP: ")
    PORT = input("PORT: ")

print('Please type your username below')
while True:
    my_username = input("Username: ")
    if len(my_username) > 0:
        break
    else:
        print('Invalid username')

addressfamily = socket.AF_INET  # IPv4
connection = socket.SOCK_STREAM  # TCP

# Socket created CLIENT
client_socket = socket.socket(addressfamily, connection)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

# Username set
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    message = input('{} > '.format(my_username))

    # Checks message is not empty
    if len(message) != 0:

         # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # Get and print received messages
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header):
                print('Data not received')
                print('Connection closed by the server')
                sys.exit()

            # Convert, decode, recive username
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            # Decode, recive message
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Print username and respective message
            print('{} > {}'.format(username, message))


    #Exceptions
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Exception, something happened, then exit
        print('Reading error: {}'.format(str(e)))
        sys.exit()

    except KeyboardInterrupt as e:
        print('Reading error: {}'.format(str(e)))
        sys.exit()
