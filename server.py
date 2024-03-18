#server
import socket
import ssl
import threading
import json
import time

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        print(f"Error occurred while fetching local IP: {e}")
        return None

def handle_client(client_socket, ip_h, delay):
    open_ports = {}
    in_use_ports = {}

    def ports(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(delay)
        res = s.connect_ex((ip_h, port))
        if res == 0:
            open_ports[port] = 'open'
            # Attempt to grab banner
            try:
                banner, service = grab_banner_and_service(ip_h, port)
                open_ports[port] = {'status': 'open', 'banner': banner, 'service': service}
            except Exception as e:
                print(f"Error grabbing banner and service from port {port}: {e}")

        if res == 1:
            in_use_ports[port] = 'in use'

        s.close()

    def grab_banner_and_service(ip, port, timeout=2):
        try:
            service = "Unknown"  # Default service name if not recognized
            banner = ""
            # Attempt to connect to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                # Receive banner (first 1024 bytes)
                banner = s.recv(1024).decode().strip()
                # Determine service based on port
                service = get_service(port)
            return banner, service
        except socket.timeout:
            return "Timeout: Unable to grab banner", "Unknown"
        except Exception as e:
            return f"Error: {e}", "Unknown"

    def get_service(port):
        # Add logic to map ports to service names
        if port == 80:
            return "HTTP"
        elif port == 443:
            return "HTTPS"
        elif port == 22:
            return "SSH"
        elif port == 21:
            return "FTP"
        elif port == 20:
            return "FTP-data"
        elif port == 7:
            return "Echo"
        elif port == 23:
            return "Telnet"
        elif port == 25:
            return "SMTP"
        elif port == 53:
            return "DNS"
        elif port == 69:
            return "TFTP"
        elif port == 88:
            return "Kerberos"
        elif port == 102:
            return "Iso-tsap"
        elif port == 110:
            return "POP3"
        elif port == 135:
            return "Microsoft EPMAP"
        elif port == 137:
            return "NetBIOS-ns"
        elif port == 139:
            return "NetBIOS-ssn"
        elif port == 143:
            return "IMAP4"
        elif port == 381:
            return  "HP openview"
        elif port == 383:
            return  "HP openview"
        elif port == 464:
            return "Kerberos"
        elif port == 465:
            return "SMTP over TLS/SSL, SSM"
        elif port ==587:
            return "SMTP"
        elif port == 593:
            return  "Microsoft DCOM"
        elif port == 636:
            return "LDAP over TLS/SSL"
        elif port == 691:
            return "MS Exchange"
        elif port == 902:
            return "VMware Server"
        elif port == 989:
            return "FTP over SSL"
        elif port == 990:
            return "FTP over SSL"
        elif port == 993:
            return "IMAP4 over SSL"
        elif port == 995:
            return "POP3 over SSL"
        elif port == 1025:
            return "Microsoft RPC"
        elif port == 1194:
            return  "OpenVPN"
        elif port == 1337:
            return  "WASTE"
        elif port == 1589:
            return  "Cisco VQP"
        elif port == 1725:
            return  "Steam"
        elif port == 2082:
            return  "cPanel"
        elif port == 2083:
            return  "radsec, cPanel"
        elif port == 2483:
            return  "Oracle DB"
        elif port == 2484:
            return  "Oracle DB"
        elif port == 2967:
            return  "Symantec AV"
        elif port == 3074:
            return  "XBOX Live"
        elif port == 3306:
            return  "MySQL"
        elif port == 3724:
            return  "World of Warcraft"
        else:
            return "Unknown"

    for port in range(0, 4092):
        ports(port)

    vulnerabilities = []
    for key in open_ports.keys():
        with open('vulnerabilities.txt', encoding='utf8') as file:
            for line in file:
                parts = line.split(':')
                if parts[0] == str(key):
                    vulnerabilities.append(parts[0] + ": " + parts[1].strip())

    if not vulnerabilities:
        vulnerabilities.append("None")

    json_vul = json.dumps(vulnerabilities)

    client_socket.send(json.dumps(open_ports).encode())
    client_socket.send(json_vul.encode())
    client_socket.close()
    print("\nConnection closed")

def start_server(ip_h, port, delay, certfile, keyfile):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    server_socket_ssl = context.wrap_socket(server_socket, server_side=True)

    print(f"\nServer is listening on {ip_h}:{port}")
    while True:
        client_socket, client_address = server_socket_ssl.accept()
        time.sleep(6)
        print(f"\nConnection from {client_address} has been established securely\n")
        time.sleep(3)
        print(f"Waiting to retrieve information from {client_address}(this may take a while).........")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, ip_h, delay))
        client_thread.start()

ip_h = get_local_ip()
if ip_h:
    SERVER_PORT = 5050
    DELAY = 0.001
    CERT_FILE = 'server.crt'
    KEY_FILE = 'server.key'
    start_server(ip_h, SERVER_PORT, DELAY, CERT_FILE, KEY_FILE)
else:
    print("Unable to retrieve local IP address. Exiting.")
