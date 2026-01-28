import socket

# Define the robot's IP address and port
ur_ip = "0.0.0.0"
ur_port = 30002

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ur_ip, ur_port))

# URScript command to move the robot
urscript_command = "movej([0, -1.57, 1.57, -1.57, 1.57, 0], a=1.2, v=0.25)\n"

# Send the command
sock.sendall(urscript_command.encode('utf-8'))

# Read the response (if there is any)
data = sock.recv(1024)  # Adjust the buffer size if needed

# Close the socket
sock.close()

# Print the response (human-readable form)
print(data.decode('utf-8', 'ignore'))  # Ignore non-readable characters
