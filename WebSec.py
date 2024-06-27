import requests
from bs4 import BeautifulSoup

# Banner ASCII
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

# Fungsi untuk melakukan scanning URL
def scan_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Scanning {url}...")
            # Misalnya, dapatkan informasi header
            print("\nServer headers:")
            print("----------------")
            for header, value in response.headers.items():
                print(f"{header}: {value}")

            # Misalnya, analisis teks dalam konten HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            # Contoh: Cari tag <form> untuk mencari potensi masalah keamanan
            forms = soup.find_all('form')
            if forms:
                print("\nForms found:")
                for form in forms:
                    print(form)

            # Implementasikan lebih banyak pengecekan keamanan yang relevan di sini
        else:
            print(f"Failed to retrieve {url}: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error scanning {url}: {str(e)}")

# Main program
if __name__ == "__main__":
    print(banner)
    target_url = input("Enter the target URL (e.g., https://example.com): ").strip()
    scan_url(target_url)
