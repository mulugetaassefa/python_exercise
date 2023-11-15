from  pathlib import path
import socket
path=path("ecommerce")
print(path.exists())


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("IP Address:", ip_address)