import requests

def scan_subdomains(domain, subdomains_file):
    with open(subdomains_file, "r") as file:
        for line in file:
            subdomain = line.strip()
            full_url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(full_url)
                if response.status_code < 400:
                    print(f"[+] Found subdomain: {full_url}")
            except:
                pass

def main():
    domain = input("Enter target domain: ")
    subdomains_file = input("Enter subdomains file: ")
    scan_subdomains(domain, subdomains_file)

if __name__ == "__main__":
    main()
