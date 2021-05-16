# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 SoHag.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER SHAZAHN HOWLADEAR >
 \033[1;96m ------------------------
\033[1;91m    
…………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀

\033[1;92m    
\033[1;91m 
\033[1;92m 
\033[1;91m 
           \033[1;93m     
            \033[1;92m
            \033[1;91m
          \033[1;92m  
           \033[1;91m                                           
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : ShAZahn HoWlAdEaR
 FACEBOOK   : FACEBOOK.COM/Shazahn howladear 
 YOUTUBE    :https://youtube.com/channel/UC3WcGIpTdNldsXAYWED7BuQ
 GITHUB     : GITHUB.COM/Shazahn-Howladear
\033[1;32m
--------------------------------------------------
                                """

cusr = "Shazahn"
cpwd = "HOWLADEAR"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://youtube.com/channel/UC3WcGIpTdNldsXAYWED7BuQ')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : SHAZAHN (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : SoHag(correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://youtube.com/channel/UC3WcGIpTdNldsXAYWED7BuQ ')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : SHAZAHN (correct)")
    print(" TOOL PASSWORD : HOWLADEAR(correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Chacking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
