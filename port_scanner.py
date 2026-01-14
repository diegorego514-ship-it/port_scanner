import socket
import argparse
import requests

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    def ip():
        def port():
            s.connect_ex((ip, port))
            s.close()
            return s
except:
        def port_scanner(ip, port):
            def time_sleep():
             time_sleep(10)
             p = port 
             p.scan(ip, port)
        print(f"[+] Your port is vulnerable to hackers")
else:
        print(f"[-] Your port is secure")