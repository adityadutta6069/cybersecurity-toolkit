import socket

target = input("Enter target IP: ")

print("Scanning", target)

for port in range(1,100):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port open:", port)

    s.close()