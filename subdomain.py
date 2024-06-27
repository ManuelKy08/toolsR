import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

banner = """
 /$$   /$$           /$$                 /$$               /$$$$$$                     
| $$  /$$/          | $$                | $$              /$$__  $$                    
| $$ /$$/   /$$$$$$ | $$   /$$  /$$$$$$ | $$   /$$       | $$  \__/  /$$$$$$   /$$$$$$$
| $$$$$/   /$$__  $$| $$  /$$/ /$$__  $$| $$  /$$//$$$$$$|  $$$$$$  /$$__  $$ /$$_____/
| $$  $$  | $$  \ $$| $$$$$$/ | $$  \ $$| $$$$$$/|______/ \____  $$| $$$$$$$$| $$      
| $$\  $$ | $$  | $$| $$_  $$ | $$  | $$| $$_  $$         /$$  \ $$| $$_____/| $$      
| $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$ \  $$       |  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/  \__/ \______/ |__/  \__/ \______/ |__/  \__/        \______/  \_______/ \_______/
                                                                        
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================
"""

print(banner)

# Daftar subdomain umum
subdomains = [
    'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'webdisk', 'cpanel', 'whm', 
    'autodiscover', 'autoconfig', 'admin', 'test', 'blog', 'shop', 'api', 'dev', 'staging'
]

# Fungsi untuk memeriksa subdomain
def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return url
    except requests.RequestException:
        return None

# Fungsi utama untuk mencari subdomain
def find_subdomains(domain):
    valid_subdomains = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(check_subdomain, domain, subdomain): subdomain for subdomain in subdomains}
        for future in as_completed(future_to_subdomain):
            subdomain = future_to_subdomain[future]
            try:
                result = future.result()
                if result:
                    print(f"Valid subdomain found: {result}")
                    valid_subdomains.append(result)
            except Exception as exc:
                print(f"{subdomain}.{domain} generated an exception: {exc}")
    return valid_subdomains

if __name__ == "__main__":
    domain = input("Enter the target domain (e.g., example.com): ")
    print(f"Scanning {domain} for subdomains...\n")
    found_subdomains = find_subdomains(domain)
    print("\nScan complete. Found the following valid subdomains:")
    for subdomain in found_subdomains:
        print(subdomain)
