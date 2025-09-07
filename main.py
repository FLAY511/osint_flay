#!/usr/bin/env python3
import sys
from modules import features

R="\033[91m"; G="\033[92m"; Y="\033[93m"; C="\033[96m"; W="\033[0m"

def banner():
    print(C + """
============================
   FLAY OSINT NO-API v1.0
   by Flay
============================
""" + W)

def menu():
    print(f"""{Y}
[1] Public IP              [9]  Security Headers
[2] IP Geolocation         [10] Wayback URLs
[3] IP ASN/Org             [11] SPF/DMARC TXT
[4] Reverse DNS            [12] SSL/TLS Info
[5] DNS Records            [13] Robots.txt / Sitemap
[6] Subdomain via crt.sh   [14] Report Generator
[7] ASN Lookup             [15] Email Breach Checker
[8] WHOIS Domain
[0] Exit
{W}""")

def main():
    banner()
    while True:
        menu()
        choice = input(f"{C}Pilih menu: {W}").strip()
        if choice == "0":
            print(G+"Bye."+W); sys.exit(0)
        try:
            idx = int(choice)
        except:
            print(R+"Input salah."+W); continue
        try:
            features.run(idx)
        except KeyboardInterrupt:
            print(R+"\nDibatalkan."+W)
        except Exception as e:
            print(R+f"[!] Error: {e}"+W)

if __name__ == "__main__":
    main()
