# 🔎 Network Scanner (ARP + ICMP)

A lightweight Python network scanner that discovers devices in a target network using ARP requests and ICMP ping sweeps. Built with Scapy
, this tool is ideal for system administrators and penetration testers who want quick visibility into active hosts on their network.

## ✨ Features

🖧 ARP Scan – Discover hosts on your local network with MAC addresses.

🌐 ICMP Scan – Perform a ping sweep to find additional reachable hosts.

📊 Detailed Output – Lists IP + MAC (for ARP) and online status (for ICMP).

🐍 Pure Python – Uses the Scapy library, no heavy dependencies.

## ⚡ Installation

Clone the repository:
```
git clone https://github.com/dhruva127/Network-Scanner-
cd network-scanner
```

Install dependencies:
```
pip install scapy
```

## 🚀 Usage

Run the scanner with root privileges (required for Scapy):
```
sudo python3 net_scan.py 192.168.1.0/24
```

## Example Output
```
[+] Scanning with ARP...

[+] Available hosts (ARP):
IP                   MAC
192.168.1.1          00:11:22:33:44:55
192.168.1.20         aa:bb:cc:dd:ee:ff

[+] Scanning with ICMP...
[+] 192.168.1.1 is online (ICMP reply)
[+] 192.168.1.10 is online (ICMP reply)
```
## 🛡️ Legal Disclaimer

This project is for educational purposes and authorized network testing only.
⚠️ Do not scan networks without explicit permission – unauthorized scanning is illegal.

## 📜 License

This project is licensed under the MIT License – you’re free to use, modify, and share, with attribution.


