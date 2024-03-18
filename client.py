#client
import socket
import ssl
import json
import time

def start_client(host, port, certfile):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(certfile)
    context.check_hostname = False
    ssl_socket = context.wrap_socket(client_socket, server_hostname=host)

    ssl_socket.connect((host, port))
    print("\nEstablishing SSL connection....\n")
    time.sleep(6)
    print("Connected to server successfully\n")
    time.sleep(3)
    print("Extracting information (this may take a while)...........\n")

    data = ssl_socket.recv(4096).decode()
    open_ports = json.loads(data)
    print("***********************")
    print("Port scan results:\n")
    for port, info in open_ports.items():
        if isinstance(info, dict):
            status = info.get('status')
            banner = info.get('banner')
            service = info.get('service')
            if status == 'open':
                print(f"Port {port}: {status}, Banner: {banner}, Service: {service}")
            else:
                print(f"Port {port}: {status}")
        else:
            print(f"Port {port}: {info}")


    vulnerabilities = ssl_socket.recv(4096).decode()
    print("***********************")
    print("Known vulnerabilities:\n")
    vul = json.loads(vulnerabilities)
    for v in vul:
        print(v)
    print("***********************\n")

    ssl_socket.close()

SERVER_HOST = "192.168.29.196"  # CHANGE SERVER IP HERE
SERVER_PORT = 5050
CERT_FILE = 'server.crt'

start_client(SERVER_HOST, SERVER_PORT, CERT_FILE)
