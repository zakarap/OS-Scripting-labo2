import netifaces
import socket


gates = netifaces.gateways()

gateway = gates['default'][netifaces.AF_INET][0]
print("default gateway is",gateway)
print(gateway,"is reachable")

DNS = socket.gethostbyname("digitap.be")
print("found nameserver",DNS)
print(DNS,"is reachable")