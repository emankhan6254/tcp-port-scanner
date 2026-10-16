# 🛡️ Asynchronous TCP Port Scanner

A lightweight, high-performance TCP port scanner built in Python using `asyncio` and `socket`. Designed to scan common ports on a target IP or domain concurrently to identify active services and open ports efficiently.

## ✨ Features
- **Asynchronous Execution**: Uses Python's `asyncio` event loop for concurrent socket connections, making scans significantly faster than traditional sequential scripts.
- **Hostname Resolution**: Automatically resolves domain names (e.g., `scanme.nmap.org`) to their target IP addresses using built-in DNS lookup.
- **Zero External Dependencies**: Built entirely using Python's standard library (`asyncio`, `socket`, `sys`, `datetime`)—no heavy packages required.

## 🚀 Usage

Run the script from your terminal specifying either a target IP address or a domain name:

```bash
python scanner.py <target_ip_or_domain>

##example

python scanner.py scanme.nmap.org

##sample output

--------------------------------------------------
Scanning target: scanme.nmap.org (45.33.32.156)
Time started: 2026-10-16 10:17:59.224882
--------------------------------------------------
[+] Port 22 is OPEN
[+] Port 80 is OPEN
--------------------------------------------------
Scan completed!

##disclaimer

This tool is intended strictly for educational purposes, authorized security research, and network auditing. Do not scan networks or systems without explicit permission from the owner.

Created by Eman Khan