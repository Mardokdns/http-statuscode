import requests
import os
import sys
from colorama import Fore

os.system("clear")

url = sys.argv[1]

r = requests.get(url)

print(f"Status Code: {r.status_code}")
