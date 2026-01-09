#!/usr/bin/env python3
import os
import sys
import datetime

# Ensure script runs as root
if os.geteuid() != 0:
    print("[!] Please run this script as root (sudo).")
    sys.exit(1)

XML_DIR = "reports/xml"
HTML_DIR = "reports/html"

os.makedirs(XML_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)

def banner():
    print("=" * 60)
    print("        NMAP AUTOMATION TOOL - KALI LINUX")
    print("        Network & Domain Scanner")
    print("=" * 60)

def menu():
    print("\nSelect Scan Type:")
    print("1. Quick Network Scan")
    print("2. Full Network Scan (Aggressive)")
    print("3. Domain Scan")
    print("4. Custom Nmap Command")
    print("5. Exit")

def run_nmap(target, options, scan_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    xml_file = f"{XML_DIR}/{scan_name}_{timestamp}.xml"
    html_file = f"{HTML_DIR}/{scan_name}_{timestamp}.html"

    print("\n[+] Running Nmap Scan...")
    cmd = f"nmap {options} {target} -oX {xml_file}"
    os.system(cmd)

    print("[+] Converting XML to HTML...")
    convert_cmd = f"xsltproc {xml_file} -o {html_file}"
    os.system(convert_cmd)

    print("\n[✓] Scan Completed Successfully!")
    print(f"[✓] XML Report : {xml_file}")
    print(f"[✓] HTML Report: {html_file}")

def quick_network_scan():
    target = input("Enter Network Range (e.g. 192.168.1.0/24): ")
    options = "-sn"
    run_nmap(target, options, "quick_network")

def full_network_scan():
    target = input("Enter Network Range (e.g. 192.168.1.0/24): ")
    options = "-A -T4"
    run_nmap(target, options, "full_network")

def domain_scan():
    target = input("Enter Domain (e.g. example.com): ")
    options = "-A -Pn"
    run_nmap(target, options, "domain_scan")

def custom_scan():
    target = input("Enter Target (IP/Range/Domain): ")
    options = input("Enter Custom Nmap Options (e.g. -sV -p 1-1000): ")
    run_nmap(target, options, "custom_scan")

def main():
    while True:
        banner()
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            quick_network_scan()
        elif choice == "2":
            full_network_scan()
        elif choice == "3":
            domain_scan()
        elif choice == "4":
            custom_scan()
        elif choice == "5":
            print("Exiting... Stay Safe 🛡️")
            sys.exit(0)
        else:
            print("[!] Invalid Choice")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

