from platform import system
from os import name, system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
                                                      
        
   '''+Style.RESET_ALL+Fore.RED+Style.BRIGHT+''' 


 _______ ___________________________________________________________________________________
 |_   _| \ | |/ ____|__   __|/\   / ____|  __ \     /\   |  \/  | |__   __/ __ \ / __ \| |     
   | | |  \| | (___    | |  /  \ | |  __| |__) |   /  \  | \  / |    | | | |  | | |  | | |     
   | | | . ` |\___ \   | | / /\ \| | |_ |  _  /   / /\ \ | |\/| |    | | | |  | | |  | | |     
  _| |_| |\  |____) |  | |/ ____ \ |__| | | \ \  / ____ \| |  | |    | | | |__| | |__| | |____ 
 |_____|_| \_|_____/   |_/_/    \_\_____|_|  \_\/_/    \_\_|  |_|    |_|  \____/ \____/|______|
                                                                                               
                                                                                               

        '''+Style.RESET_ALL+Fore.RED+Style.BRIGHT+'''
# '''+Style.RESET_ALL+Fore.WHITE+Style.BRIGHT+''' Coded by'''+Style.RESET_ALL+Fore.RED+''' kaje.dev
'''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "kullanıcı tarafından durduruldu..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Lütfen internet bağlantınızı kontrol edin...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.WHITE+Style.BRIGHT+"Sisteme giriş sağlanıyor"+Fore.RESET)
        for i in tqdm(range(9999)):
            print(end=Fore.WHITE+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "kullanıcı tarafından durduruldu" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.WHITE+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.RED+" TAKİPCİ"+Fore.WHITE+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.RED+" BEĞENİ "+Fore.WHITE+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.RED+" ÇIKIŞ")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n  >>> "+Fore.RESET))
            if opt=='2':
                domain=str(input(Fore.WHITE+Style.BRIGHT+"Gönderi link >>> "+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='1':
                ip = input(Fore.WHITE+Style.BRIGHT+"Kullanıcı adı girin >>> "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"Yine Bekleriz :D"+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'Hata!'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.WHITE+Style.BRIGHT+"Takipci Sayısı >>> "+Fore.RESET))


        print(Fore.YELLOW+Style.BRIGHT+"başlangıç...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.BLACK+Back.LIGHTWHITE_EX+"TAKİPÇİLER GÖNDERİLİYOR..."+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.WHITE+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"Bir şeyler yanlış gitti!")
        print("Hata: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sent=sent+1
            port=port+1
            color_list = [Fore.WHITE+Style.BRIGHT+Back.BLACK ]
            color_random = random.choice(color_list)

            print(color_random+"TAKİPÇİLER %s PAKETİNDE %s ADRESİNE GİDİYOR, GÖNDERİLEN TAKİPÇİ SAYISI >>> %s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Terminado\nhata: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nKapatılıyor..."+Fore.RESET)



ddos()
