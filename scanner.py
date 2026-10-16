import asyncio
import socket
import sys
from datetime import datetime

async def scan_port(ip: str, port: int):
    """Attempts to connect to a specific port on a target IP."""
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        print(f"[+] Port {port} is OPEN")
        writer.close()
        await writer.wait_closed()
    except (asyncio.TimeoutError, ConnectionRefusedError):
        pass
    except Exception as e:
        pass

async def main():
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <target_ip_or_domain>")
        sys.exit(1)

    target_input = sys.argv[1]
    
    # Resolve domain name to IP address safely
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {target_input}")
        sys.exit(1)

    print(f"-" * 50)
    print(f"Scanning target: {target_input} ({target_ip})")
    print(f"Time started: {datetime.now()}")
    print(f"-" * 50)

    # Scan common ports (e.g., 1 to 1024)
    tasks = [scan_port(target_ip, port) for port in range(1, 1025)]
    await asyncio.gather(*tasks)

    print(f"-" * 50)
    print("Scan completed!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting script...")
        sys.exit(0)