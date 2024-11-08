# server.py
import socket

# Server setup
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 65432      # Port to bind to
control_mode = False  # Flag to toggle control mode

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept new connection
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected to {client_address}")

            while True:
                # Receive data from the client
                data = client_socket.recv(1024).decode()
                if not data:
                    break

                if data == "control mode":
                    control_mode = True
                    client_socket.sendall("Entering control mode".encode())
                    print("Control mode activated")
                elif data == "exit control":
                    control_mode = False
                    client_socket.sendall("Exiting control mode".encode())
                    print("Control mode deactivated")
                elif control_mode:
                    print(f"Key pressed: {data}")
                    client_socket.sendall(f"Acknowledged key: {data}".encode())
                else:
                    print(f"Command received: {data}")
                    client_socket.sendall(f"Acknowledged command: {data}".encode())
