#!/bin/python3
import socket
from IPy import IP

class PortScan():
    banners = []
    open_ports = []


    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num
    
    def scan(self):
        for port in range(1, 500):
            scan_port(port)
        
    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)
            
    def get_banner(self):
        return s.recv(1024)
            
            
    def scan_port(self,port):
        try:
            converted_ip = self.check_ip(target)
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
           
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass
            
 # Port scanner shows the ports on 
 # The header is the banner of the software
 # it list out the vulnerability of the software (list of vulnerbale application running in port          
            
 # Any open port is running a service which the banner grabber (getting the header of the service)      
            
            
            
            
