#!/usr/bin/env python3
"""
Network Scanner: ARP + ICMP
 (authorized use only)

Author: Dhruv Bhoir

License: MIT

Version: 1.0

"""

from scapy.all import srp, sr1
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP
import ipaddress
import sys


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <target_network>")
    print(f"Example: {sys.argv[0]} 192.168.1.0/24")
    sys.exit(1)

target_network = sys.argv[1]
online_clients = []

# --- ARP SCAN ---
print("[+] Scanning with ARP...")
ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Destination MAC address broadcast
arp = ARP(pdst=target_network)          # Target network
probe = ether / arp

answered, unanswered = srp(probe, timeout=3, verbose=0)
# [ answer , unanswered ]
# answered cosists of [ sent , received ]

for _, received in answered:
    online_clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("\n[+] Available hosts (ARP):")
print("IP".ljust(20) + "MAC")
for client in online_clients:
    print(f"{client['ip'].ljust(20)} {client['mac']}")


# --- ICMP SCAN ---
print("\n[+] Scanning with ICMP...")
ip_list = [str(ip) for ip in ipaddress.IPv4Network(target_network, strict=False)]

for ip in ip_list:
    probe = IP(dst=ip) / ICMP()
    result = sr1(probe, timeout=2, verbose=0)
    if result:
        print(f"[+] {ip} is online (ICMP reply)")
