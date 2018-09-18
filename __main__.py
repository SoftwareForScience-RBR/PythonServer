import socket                   # Import socket module
path = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/file.txt'
import datetime

while True:
    port = 60000  # Reserve a port for your service.
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    s.bind((host, port))  # Bind to the port
    s.listen(5)  # Now wait for client connection.

    print('Server listening....')

    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    #write to file
    saveFile = open(path, "a")
    saveFile.write(data.decode() + "\n")
    saveFile.close()

    s.close()
