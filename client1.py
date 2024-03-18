#client
import socket
import ssl
import json

def start_client(host, port, certfile):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(certfile)
    context.check_hostname = False
    ssl_socket = context.wrap_socket(client_socket, server_hostname=host)

    ssl_socket.connect((host, port))
    print("\nSSL cert received. Connected to server securely.\n")

    data = ssl_socket.recv(4096).decode()
    open_ports = json.loads(data)
    print("Port scan results:")
    for port, info in open_ports.items():
        if isinstance(info, dict):
            print(f"Port {port}: {info['status']}, Service: {info['service']}")
        else:
            print(f"Port {port}: {info}")

    vulnerabilities = ssl_socket.recv(4096).decode()
    print("\nKnown vulnerabilities:\n")
    vul = json.loads(vulnerabilities)
    for v in vul:
        print(v)

    ssl_socket.close()

SERVER_HOST = "192.168.33.223"  # CHANGE SERVER IP HERE
SERVER_PORT = 5050
CERT_FILE = 'server.crt'

start_client(SERVER_HOST, SERVER_PORT, CERT_FILE)
