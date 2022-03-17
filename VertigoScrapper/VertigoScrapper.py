import requests
import colorama
from colorama import Fore
import os 
import sys
from time import sleep
import fade
import concurrent.futures
import pyfiglet

test_url = r'https://www.youtube.com/channel/UCR55c-mtcH86O-QvOQC_oFg?sub_confirmation=1'


figlet = pyfiglet.figlet_format("VertigoScraper", font = "slant"  )
text = (figlet)
faded_text = fade.brazil(text)
print(faded_text)

colorama.init()

text = "\033[0;91m[+] This program will scrape (Https,Socks4,Socks5) proxies into separate files"
for x in text:
  sleep(0.02) # In seconds
  sys.stdout.write(x)
  sys.stdout.flush()
print()

whatproxy = int(input('''\033[0;37m
[+] Which type of proxy do you need?
    
[1] Https 
[2] Socks4
[3] Socks5
    \n
[Enter a No. (1-3) ]> '''))

if whatproxy == 1:
    out_file = "Https.txt"
    proxies = open(out_file,'wb')
    r1 = requests.get('https://api.openproxylist.xyz/http.txt')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    os.system('pause')
    sys.exit()
    
elif whatproxy == 2:
    r1 = requests.get('https://api.openproxylist.xyz/socks4.txt')
    out_file = "Socks4.txt"
    proxies = open(out_file,'wb')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    os.system('pause')
    sys.exit()
   
elif whatproxy == 3:
    r1 = requests.get('https://api.openproxylist.xyz/socks5.txt')
    out_file = "Socks5.txt"
    proxies = open(out_file,'wb')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
    os.system('pause')
    sys.exit()
   

else:
    print("Not a valid choice!")
    

