import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""\033[1;32m
                ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓
                ┃┏━┓┃  ┃┏━┓┃  ┃┏━┓┃  ┗┓┏┓┃
                ┃┃━┗┛  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                ┃┃┏━┓  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                ┃┗┻━┃  ┃┗━┛┃  ┃┗━┛┃  ┏┛┗┛┃
                ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── ONEONE ────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m 3.0                                   \033[1;32m║
\033[1;32m║   \033[1;39mFACEBOOK           :  1767860155                     \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  ZALO.ME/G/QHUZFX800            \033[1;32m║
\033[1;32m║   \033[1;39mGITHUB             :  ONEONE                         \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER           :  ONEONE ☊                       \033[1;32m║
\033[1;32m║   \033[1;39mTOOL WORLD         :  WIFI AND DATA                  \033[1;32m║
\033[1;39m└────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║   \033[1;39mTRAO DOI SUB    \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;32mTOOL TDS PROFILE \033[1;31m[\033[1;33mv2\033[1;31m]         ")
	print("\033[1;31m[\033[1;39m2.1\033[1;31m] \033[1;32mTOOL TDS COOKIE               ")
	print("\033[1;31m[\033[1;39m3.1\033[1;31m] \033[1;32mTOOL TDS COOKIE \033[1;31m[\033[1;33mv2\033[1;31m]           ")
	print("\033[1;31m[\033[1;39m4.1\033[1;31m] \033[1;32mTOOL TDS TIKTOK ")
	print("\033[1;31m[\033[1;39m5.1\033[1;31m] \033[1;32mTOOL TDS NOW ")
	print("\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;32mTOOL TDS INSTAGRAM ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m   TTC \033[1;31m[\033[1;33mNEW\033[1;31m]     \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m7.1\033[1;31m] \033[1;32mTOOL TTC TIKTOK ")
	print("\033[1;31m[\033[1;39m8.1\033[1;31m] \033[1;32mTOOL TTC TOKEN  ")
	print("\033[1;31m[\033[1;39m9.1\033[1;31m] \033[1;32mTOOL TTC PROFILE")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐          ")
	print("\033[1;32m║  \033[1;39m     TOOLS       \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m10\033[1;31m] \033[1;32mTOOL SPAM MESSAGE ")
	print("\033[1;31m[\033[1;39m11\033[1;31m] \033[1;32mTOOL GET TOKEN FB ")
	print("\033[1;31m[\033[1;39m12\033[1;31m] \033[1;32mTOOL REG PAGE VỊ TRÍ ")
	print("\033[1;31m[\033[1;39m13\033[1;31m] \033[1;32mTOOL RÚT GỌN TRAFFIC1S")
	print("\033[1;31m[\033[1;39m14\033[1;31m] \033[1;32mTOOL MAXCARE \033[1;39m4.9.6 \033[1;31m[\033[1;33mNEW\033[1;31m] ")
	print("\033[1;31m[\033[1;39m15\033[1;31m] \033[1;32mWEB LẤY CODE TOOL FREE  \033[1;31m[\033[1;33mNEW\033[1;31m] ")
	print("\033[1;31m[\033[1;39m16\033[1;31m] \033[1;32mDOWNLOAD TOOL REG TIKTOK \033[1;31m[\033[1;33mNEW\033[1;31m] ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m    PROFILE      \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m17\033[1;31m] \033[1;32mTOOL BUFF VIEW STORY MAX SPEED PROFILE ")
	print("\033[1;31m[\033[1;39m18\033[1;31m] \033[1;32mTOOL REG PAGE PROFILE ")
	print("\033[1;31m[\033[1;39m19\033[1;31m] \033[1;32mTOOL GET TOKEN PROFILE ")
	print("\033[1;31m[\033[1;39m20\033[1;31m] \033[1;32mTOOL MENBER GROUP PROFILE \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
	print("\033[1;31m[\033[1;39m21\033[1;31m] \033[1;32mTOOL SHARE ẢO PROFILE \033[1;31m[\033[1;39mMAX SPEED\033[1;31m] ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mCHOSE\033[1;39m]\033[1;39m: \033[1;32m')
	print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
	if chon == '1.1' :
		exec(requests.get('https://run.mocky.io/v3/a500b829-0087-4a8f-b3f6-101ebb79ecf7').text)
	if chon == '2.1':
		exec(requests.get('https://run.mocky.io/v3/5a3644c0-e217-4e49-a8cf-9d74f6552b1d').text)
	if chon == '3.1' :
		exec(requests.get('https://run.mocky.io/v3/8b1c1152-aff3-4f40-a3a8-f8a92ab4acfa').text)
	if chon == '4.1' :
		exec(requests.get('https://run.mocky.io/v3/929d0ec1-24fb-403f-a7a6-5b625188ded0').text)
	if chon == '5.1' :
		exec(requests.get('https://run.mocky.io/v3/d6322f1e-0713-42dc-bbc4-c58565b444d0').text)
	if chon == '6.1':
		exec(requests.get('https://run.mocky.io/v3/d6322f1e-0713-42dc-bbc4-c58565b444d0').text)
	if chon == '6.2' :
		exec(requests.get('https://run.mocky.io/v3/4da6d01f-62ba-4836-b9b2-64d79f472fc0').text)
	if chon == '7.1' :
		exec(requests.get('https://run.mocky.io/v3/ef6729a1-1548-48cf-ab14-363208f48b59').text)
	if chon == '8.1' :
		exec(requests.get('https://run.mocky.io/v3/3a6ec16a-3f13-478a-a400-69622182a268').text)
	if chon == '9.1' :
		exec(requests.get('https://run.mocky.io/v3/e6235911-8862-43cc-9561-ed7453b9aadb').text)
	if chon == '10':
		exec(requests.get('https://run.mocky.io/v3/fca278a6-c1b8-40df-a35a-2115a45e2781').text)
	if chon == '11' :
		exec(requests.get('https://run.mocky.io/v3/d38cfa2b-28ab-44ff-8ede-813898ff941f').text)
	if chon == '12' :
		exec(requests.get('https://run.mocky.io/v3/91bcc211-369d-4c2c-9e89-650e1e9271ad').text)
	if chon == '13':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '14':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '15':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '16':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '17' :
		exec(requests.get('https://run.mocky.io/v3/3a6ec16a-3f13-478a-a400-69622182a268').text)
	if chon == '18' :
		exec(requests.get('https://run.mocky.io/v3/4b6ca251-283b-4d49-85e9-cd0a731485ec').text)
	if chon == '19' :
		exec(requests.get('https://run.mocky.io/v3/7c0b1444-8685-4a33-98c8-18713bca2211').text)
	if chon == '20' :
		exec(requests.get('https://run.mocky.io/v3/94c0852d-7373-474f-ae39-b2dd2b8d78aa').text)
	if chon == '21' :
		exec(requests.get('https://run.mocky.io/v3/1e0c4843-6aa2-4af0-8955-55fe1e1c4d34').text)
	else :
		continue