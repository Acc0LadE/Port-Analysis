# Port Service Detection
******
#### The features of this project is:
1) Detects open ports in client machine.
2) Checks wether the port is being blocked by a service and determines the service that is using the port.
3) Has Multithreading or Asynchronous I/O, which allows connection of multiple clients to the server.

## Steps to execute:

1) Download Server and Client files
2) If you haven't downloaded python yet, you can do so from the link https://www.python.org/downloads/
3) Run the following commands in a terminal to install the required packages
  ```
  pip install socket
  ```
  ```
  pip install ssl
  ```
  ```
  pip install threading
  ```
  ```
  pip install json
  ```
4) Change IP address to server IP address that you want to connect to at line 31 in the `client.py` file.
5) Run this command in the terminal in the directory where you have saved the `server.py` file.
  ```
   openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -node
  ```
   This command generates `server.cert` and `server.key` files which are required for SSL (Secure Socket Layers) to create a secure connection between the Server and Client.
6) Save the `server.cert` file in the directory where the `client.py` file is saved.

7) Now run the server file, after which, run the client file  
