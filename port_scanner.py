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
             time_sleep(10) # Time in seconds
             p = port 
             p.scan(ip, port)
        print(f"[+] Your Port is vulnerable to hackers")
else:
        print(f"[-] Your Port is secure")

try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(5)
     def ip():
          def port():
               s.connect_ex((ip, port))
               s.close()
               return s
except:
            def port_scanner(ip, port):
              def time_sleep():
               time_sleep(15) # Time in seconds
               p = port
               p.scan(ip, port)
            print(f"[+] Your Port has been intercepted by hackers")
else:
            print(f"[-] Your Port is not vulnerable to hackers")
