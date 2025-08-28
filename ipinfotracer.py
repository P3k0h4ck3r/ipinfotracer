import requests
import pyfiglet
from colorama import Fore, Style

def banner():
    ascii_banner = pyfiglet.figlet_format("ipinfotracer")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.GREEN + "Created by: Peko Sarshu\n\tp3k0h4ck3r\t\tInstagram:@pekopekoboy5" + Style.RESET_ALL)

def ip_tracker(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            print(f"{Fore.YELLOW}[+] IP Address : {data['query']}")
            print(f"[+] ISP        : {data['isp']}")
            print(f"[+] Org        : {data['org']}")
            print(f"[+] Country    : {data['country']}")
            print(f"[+] Region     : {data['regionName']}")
            print(f"[+] City       : {data['city']}")
            print(f"[+] ZIP        : {data['zip']}")
            print(f"[+] Latitude   : {data['lat']}")
            print(f"[+] Longitude  : {data['lon']}")
            print(f"[+] Google Maps: https://www.google.com/maps/?q={data['lat']},{data['lon']}{Style.RESET_ALL}")
        else:
            print(Fore.RED + "[-] Could not fetch details for this IP." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    banner()
    ip = input(Fore.CYAN + "Enter IP Address or Domain: " + Style.RESET_ALL)
    ip_tracker(ip)
