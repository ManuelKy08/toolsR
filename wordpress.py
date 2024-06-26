import requests
from bs4 import BeautifulSoup

def wpscan(target_url):
    # Mencoba mendapatkan versi WordPress
    try:
        response = requests.get(target_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_generator = soup.find('meta', attrs={'name': 'generator'})
        if meta_generator and 'WordPress' in meta_generator['content']:
            print(f"WordPress version: {meta_generator['content']}")
        else:
            print("WordPress version not found or site is not WordPress.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve WordPress version: {e}")

    # Mencoba mengambil daftar pengguna (hanya untuk WordPress)
    try:
        response = requests.get(target_url + '/wp-json/wp/v2/users')
        if response.status_code == 200:
            users = response.json()
            if users:
                print("Enumerated users:")
                for user in users:
                    print(f"- ID: {user['id']}, Name: {user['name']}, Username: {user['slug']}")
            else:
                print("No users enumerated.")
        elif 'WordPress' in meta_generator['content']:
            print("Failed to enumerate users.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to enumerate users: {e}")

def main():
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

    # Meminta input URL dari pengguna
    target_url = input("Enter the target URL (e.g., https://example.com): ").strip()

    # Memanggil fungsi untuk melakukan pemindaian WordPress
    wpscan(target_url)

if __name__ == "__main__":
    main()
