# client.py
import socket
import keyboard  # Library to capture keypresses in real-time

# Replace with your Raspberry Pi's IP address
HOST = '192.168.1.168'  #IP address
PORT = 65432              # Port to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    while True:
        # Command prompt for user input
        command = input("Enter command ('control mode' to start, 'exit control' to stop): ")
        client_socket.sendall(command.encode())
        
        # Receive acknowledgment
        response = client_socket.recv(1024).decode()
        print("Server:", response)
        
        if command == "control mode":
            print("Press 'Esc' to exit control mode")

            # Listen for keypresses and send each one to the server
            while True:
                if keyboard.is_pressed('esc'):
                    client_socket.sendall("exit control".encode())
                    print("Exiting control mode")
                    break
                
                # Capture and send each key pressed
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name  # Capture key name
                    client_socket.sendall(key.encode())
                    response = client_socket.recv(1024).decode()
                    print("Server:", response)
