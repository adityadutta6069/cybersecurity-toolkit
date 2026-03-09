import requests
import socket

target = input("Enter website (example: example.com): ")

print("\nScanning website:", target)

response = None   # define response first

# -----------------------
# 1. Check Website Status
# -----------------------

try:
    response = requests.get("http://" + target)
    print("\n[+] Website reachable")
    print("Status Code:", response.status_code)

except:
    print("\n[-] Website not reachable")


# -----------------------
# 2. Server Information
# -----------------------

if response:
    server = response.headers.get("Server")
    print("\n[+] Server:", server)


# -----------------------
# 3. Security Headers
# -----------------------

security_headers = [
    "X-Frame-Options",
    "X-XSS-Protection",
    "Content-Security-Policy",
    "Strict-Transport-Security"
]

print("\nChecking security headers:")

if response:
    for header in security_headers:

        if header in response.headers:
            print(f"[+] {header} is present")
        else:
            print(f"[-] {header} is missing")


# -----------------------
# 4. Port Scan
# -----------------------

print("\nScanning common ports...")

ports = [21,22,23,80,443,8080]

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    s.close()