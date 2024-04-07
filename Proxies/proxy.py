import random
from Proxies.auth_data import login, password, ip_list


def random_ip(_ip_list):
    ip = random.choice(_ip_list)
    return ip


def get_proxy():
    proxy_AK = {
        "proxy": {
            "https": f"https://{login}:{password}@{random_ip(_ip_list=ip_list)}"
        }
    }
    proxy_MV = {
        "proxy": {
            "https": "https://dB3PqQ:dJVVEo@193.233.125.150:8000"
        }
    }
    proxies = [proxy_AK, proxy_MV]

    return random.choice(proxies)

