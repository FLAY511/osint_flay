# FLAY OSINT NO-API

Toolkit OSINT sederhana (15 fitur) yang bisa langsung dipakai di Termux tanpa API key.

## 🚀 Install di Termux
```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
pip install requests python-whois

unzip FLAY_OSINT_NOAPI.zip
cd FLAY_OSINT_NOAPI

python main.py
```

## 📚 Fitur
1) Public IP (ipify)
2) IP Geolocation (ip-api)
3) IP ASN/Org (ipinfo free)
4) Reverse DNS
5) DNS Records (DoH Google)
6) Subdomain via crt.sh
7) ASN Lookup (hackertarget)
8) WHOIS Domain
9) Security Headers Check
10) Wayback URLs (Archive.org)
11) SPF/DMARC TXT records
12) SSL/TLS Server Info
13) robots.txt / sitemap fetch
14) Report Generator (Markdown)
15) Email Breach Checker (redirect ke HIBP)

## ⚠️ Disclaimer
Gunakan hanya untuk edukasi & target legal (bug bounty / lab sendiri).
