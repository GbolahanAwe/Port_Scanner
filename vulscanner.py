#!/bin/python3
import portscanningfinal

targets_ip = input( ' [+] * Enter Targets to Scan for vulnerable Open Ports: ')
port_number = int(input( ' [+] * Enter Amounts of Ports you want to scan(500 - First 500 ports): '))
vul_file = input( ' [+] * Enter path to the file with Vulnerability Softwares: ')
print('\n')

target = portscanningfinal.PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERBLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
        count += 1



