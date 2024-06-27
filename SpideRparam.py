import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
from collections import defaultdict

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

# Fungsi untuk mendapatkan URL dari halaman
def get_urls_from_page(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        return [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
    except requests.RequestException as e:
        print(f"Failed to retrieve URLs from {url}: {e}")
        return []

# Fungsi untuk menemukan parameter URL
def find_url_parameters(urls):
    params = defaultdict(list)
    for url in urls:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        for param, value in query_params.items():
            params[param].append(value)
    return params

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., https://example.com): ")
    print(f"Scanning {target_url} for URL parameters...\n")
    
    # Inisialisasi daftar URL
    urls_to_scan = [target_url]
    seen_urls = set()

    # Crawling halaman untuk mendapatkan URL
    while urls_to_scan:
        current_url = urls_to_scan.pop(0)
        if current_url in seen_urls:
            continue
        seen_urls.add(current_url)
        print(f"Scanning {current_url}...")
        urls_on_page = get_urls_from_page(current_url)
        urls_to_scan.extend(urls_on_page)
    
    # Mencari parameter URL
    url_parameters = find_url_parameters(seen_urls)
    
    # Menampilkan hasil
    print("\nScan complete. Found the following URL parameters:")
    for param, values in url_parameters.items():
        print(f"{param}: {values}")
