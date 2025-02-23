import socket
from _thread import *
import threading

print_lock = threading.Lock()


def threaded_server(conn):
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        str_data = str(data)
        conn.send(str(f'{str_data} ---> received').encode())

    conn.close()  # close the connection


def run_server():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance

    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        start_new_thread(threaded_server, (conn,))

    conn.close()  # close the connection
    
if __name__ == '__main__':
    run_server()
