import sys
import os
from core.mails.sends_mails import mailing

from core.cfg.config import config


#first script checking are config is setup good.

cfg = config() #creating object of config class

cfg.checkTextFile('/core/mails/mail_content.txt') #checking if file exists
cfg.checkTextFile('/core/proxy/proxy_list.txt') #checking if file exists


cfg.varSetupChecker()
print('Setting up is good, prining menu...')

mails_tool = mailing()
menu = cfg.menu_init()

proton_status = False

if menu == '1':
    print('Sending mails to ALL recivers from list of recipients (in loop) ')
    print('configure your proxy.')
    proxy = input('use proxy? (y/n): ')
    if proxy == 'y':
        proxy_status = True
        mails_tool.sendLoopedMail(proxy_status)
        print('proxy is on')
    elif proxy == 'n':
        proxy_status = False
        print('proxy is off')
        mails_tool.sendLoopedMail(proxy_status)
elif menu == '2':
    print('send mails to ALL recivers from list but one time ')
    mails_tool.sendMail()
elif menu == '3':
    print('configure your proxy.')
    proxy = input('use proxy? (y/n): ')
    if proxy == 'y':
        proxy_status = True
        print('proxy is on')
    elif proxy == 'n':
        proxy_status = False
        print('proxy is off')
        menu = cfg.menu_init()
elif menu == '4':
    print('sending message via protonmail?')
    chooice_proton = input('use protonmail? (y/n) or (i <--- to get instructions): ')
    print('all recivers in loop?')
    chooice_loop = input('use loop? (y/n): ')
else:
    print('Wrong option')
    sys.exit();
    

#finito.