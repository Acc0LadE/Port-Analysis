# Port Service Detection

#### The features of this project is:
1) **Open Port Detection** that scans all ports and determines ports that are open using flag values like `0` and `1`.
2) **Service Detection** that attempt to identify the service running on each open port by sending application-specific probes or analyzing response patterns.
3) **Multithreading or Asynchronous I/O**, which can significantly improve the speed and efficiency by scanning multiple ports simultaneously, reducing the overall scan time.
4) **Vulnerability** scanning capabilities by integrating with vulnerability databases or `.csv` or `.txt` files to warn users of different vulnerabilities of known ports.
5) **Banner Grabbing** involves capturing and analyzing the response from open ports to gather information about the service, such as version number and server type.

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

## Troubleshooting:

1) `Timeout: Unable to grab banner`

#### This could happen for several reasons:
* No Service Running: There might be no service running on these ports, so attempting to grab the banner resulted in a timeout because there was no response from the server.
* Firewall or Network Configuration: The connection might be blocked by a firewall or there could be network configuration issues preventing the server from accessing the services running on these ports.
* Timeout Settings: The timeout value used for attempting to grab the banner might be too short for these ports, especially if the services running on them take longer to respond.

To troubleshoot this issue, you can try the following:
* Verify that there are services running on ports 135, 139, and 445.
* Check the firewall settings to ensure that connections to these ports are allowed.
* Increase the timeout value used for attempting to grab the banner to give the services more time to respond.
* Ensure that the server has proper network access to reach the services running on these ports.
