import socket  # Import socket module

path = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/file.txt'
cPath = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/cFile.txt'
cmaPath = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/cmaFile.txt'
linPath = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/linFile.txt'
comPath = 'C:/Users/Brendan van Walstijn/PycharmProjects/server/comFile.txt'

while True:
    port = 60000  # Reserve a port for your service.
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    s.bind((host, port))  # Bind to the port
    s.listen(5)  # Now wait for client connection.

    print('Server listening....')

    conn, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    decodedData= data.decode()
    sub = decodedData[8:11]

    if 'c++' in sub:
        # write to file
        saveFile = open(path, "a")
        saveFile.write(decodedData + "\n")
        saveFile.close()

    if 'c# ' in sub:
        # Write to c# file
        cFile = open(cPath, "a")
        cFile.write(decodedData + "\n")
        cFile.close()

    if 'cma' in sub:
        # write to cma file
        cmaFile = open(cmaPath, "a")
        cmaFile.write(decodedData + "\n")
        cmaFile.close()

    if 'lin' in sub:
        # write to cma file
        linFile = open(linPath, "a")
        linFile.write(decodedData + "\n")
        linFile.close()

    if 'com' in sub:
        # write to cma file
        comFile = open(comPath, "a")
        comFile.write(decodedData + "\n")
        comFile.close()

    s.close()
