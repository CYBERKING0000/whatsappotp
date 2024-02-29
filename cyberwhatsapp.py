import os
import sys
import time
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


os.system ('clear')

p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'


print("")
print("")

def security():
    url = "https://telecrm.in/blog/whatsapp-otp/"
    senum=input (h+"[×] enter sender number : ")
    print("  ")
    renum= input (h+"[×] enter recipient number : ")
    print("  ")

    tables = pd.read_html(url)

    payload = {
        "custom_data": {"Body": {
            "1": "Damilola",
            "2": "Olotu",
            "3": "Lagos"
        }},
        "sender": (senum),
        "recipient": (renum),
        "template_code": "TEMPLATE_CODE",
        "type": "template"
}
    headers = {
        "User-agent" : "Mozilla/5.0 (windows NT 10.0; win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer "
}

    response = requests.request("POST", url, json=payload, headers=headers)


    x=print(m+"A message will arrive within twenty-four minutes 48....")

    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char =="\n":
            time.sleep(0.5)
        else:
            time.sleep(0.1000)
def githup():
    os.system('xdg-open https://github.com/Cyberking12346/Dbom')
def whatsapp():
    os.system('xdg-open https://Wa.me//+94717804134?text=_මං_කොහොමද_උදව්_කරන්න_ඕනා')


def banner():
    
    print(m+"""                             ／⌒ヽ
　　　                       /° ω°
　                        ノ ヽ　ノ ＼＿
                       `/　`/ ⌒Ｙ⌒ Ｙ　ヽ  𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣 𝗢𝗧𝗣 𝗕𝗬𝗣𝗔𝗦𝗦
                         ( 　(三ヽ人　 / |        [ 𝗧𝗢𝗢𝗟 ]
                       |　ﾉ⌒＼ ￣￣ヽ　 ノ
                       ヽ＿＿＿＞､＿＿_／
　　                       ｜( 王 ﾉ〈
　                          /ﾐ`ー―彡ヽ
　     　                   /　ヽ_／　\.
    
                      𝗧𝗢𝗢𝗟 𝗕𝗬 𝗖𝗬𝗕𝗘𝗥 𝗞𝗜𝗡𝗚""")
    print(k+"                   __𝗽𝗮𝘀𝗶𝗻𝗱𝘂__")

    
    
    print("")
    print("")
    print("       [1] start : ")
    print("   ")
    print("       [2] my githup tool : ")
    print("")
    print("       [3] my whatsapp : ")
    print("")
    print("")
    mg=(u+"I made this tool not to do wrong things to you. We can get whatsapp otp in this tool but this is very scary thing.I am not responsible for any of this tool. If you can, use a VPN. This tool is experimental and may not always work.  TOOL BY   ____CYBER KING____ ")
    print("")
    for char in mg:
        sys.stdout.write(char)
        sys.stdout.flush()

    if char =="\n":
        time.sleep(0.5)
    else:
        time.sleep(0.100)
        
    print("") 
    print("")
    print("")   
    choi=int(input(h+"[×] enter your choice : "))
    print("")




    if choi == 1:
        security()
    elif choi ==2:
        githup()
    elif choi ==3:
        whatsapp()
    else:
        print(m+" no choice incorrect🖕🖕")


banner()