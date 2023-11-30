

import socket
import ipaddress

def scan_specific_ip(ip, start_port, end_port):
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
    except socket.error:
        print("\nError scanning {ip}")
    return open_ports

def scan_subnet(subnet, port):
    up_ips = []
    for ip in ipaddress.IPv4Network(subnet, strict=False):
        open_ports = scan_specific_ip(str(ip), port, port)
        if open_ports:
            up_ips.append((str(ip), open_ports))
    
    return up_ips

if __name__ == "__main__":
    while True:
        print("\nPort Scanner\n")
        print("\n1. Scan a specific IP address with a specific port")
        print("2. Scan a specific IP address with a specific port range")
        print("3. Scan a specific IP address with well-known ports (1-1024)")
        print("4. Scan a subnet for active IP addresses")
        print("0. Exit\n")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            ip = input("\nEnter the IP address to scan: ")
            port = int(input("\nEnter the port to scan: "))
            open_port = scan_specific_ip(ip, port, port)
            
            if open_port:
                print(f"\nPort : {port} is open")
            else:
                print(f"\nPort : {port} is closed")
                
        elif choice == "2":
            ip = input("\nEnter the IP address to scan: ")
            start_port = int(input("\nEnter the start port: "))
            end_port = int(input("\nEnter the end port: "))
            open_ports = scan_specific_ip(ip, start_port, end_port)
            
            if open_ports:
                print(f"\nOpen ports : {', '.join(map(str, open_ports))}")
            else:
                print("\nNo open ports found ")
                
        elif choice == "3":
            ip = input("\nEnter the IP address to scan: ")
            open_ports = scan_specific_ip(ip, 1, 1024)  
            
            if open_ports:
                print(f"\n open ports : {', '.join(map(str, open_ports))}")
            else:
                print("\nNo open ports found ")
                
        elif choice == "4":
            subnet = input("\nEnter the subnet to scan (e.g., 192.168.1.0/24): ")
            port = int(input("\nEnter the port to scan: "))
            up_ips = scan_subnet(subnet, port)
            
            if up_ips:
                print("\nActive IP addresses with open ports:")
                for ip, open_ports in up_ips:
                    print(f"{ip}: {', '.join(map(str, open_ports))}")
            else:
                print(f"\nNo active IP addresses found with {port} in the subnet.")
        elif choice == "5":
            break
        else:
            print("\nInvalid choice !!!")
