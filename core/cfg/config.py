import sys
import os

class config:
    def __init__(self):
        self.MY_PASSWORD = 'd'
        self.MY_MAILHOST = ''
        self.MY_MAILHOST_PORT = 
        self.MY_ADRESS = ''
        self.MSG_FILE_NAME = 'mail_content.txt'

    def varSetupChecker(self):
        if self.MY_PASSWORD == '':
            print('You need to set MY_PASSWORD in /core/config/config.py')
            sys.exit()
        if self.MY_MAILHOST == '':
            print('You need to set MY_MAILHOST in /core/config/config.py')
            sys.exit()
        if self.MY_MAILHOST_PORT == '':
            print('You need to set MY_MAILHOST_PORT in /core/config/config.py')
            sys.exit()
        if self.MY_ADRESS == '':
            print('You need to set MY_ADRESS in in /core/config/config.py')
            sys.exit()
        if self.MSG_FILE_NAME == '':
            print('You need to set MSG_FILE_NAME in /core/config/config.py') #REMEMBER PUT FILE WITH MESSAGE CONTENT IN /CORE/MAILS. AND DO IT IN TXT FORMAT
            sys.exit()
        return self.MY_PASSWORD, self.MY_MAILHOST, self.MY_MAILHOST_PORT, self.MY_ADRESS, self.MSG_FILE_NAME

    def checkTextFile(self, file_name):
        if file_name == 'mail_content.txt':
            if not os.path.exists('/core/mails/'+file_name):
                print('You need to put'+ file_name +'in /core/mails')
                sys.exit()
            else:
                return True
        elif file_name == 'proxy_list.txt':
            if not os.path.exists('/core/proxy/' + file_name):
                print('You need to put ' + file_name + ' in /core/mails or /core/proxy')
                sys.exit()
    def menu_init(self):
        print('#############################################################')
        print('#1. send mails to ALL recivers from list of recipients')
        print('#2. send mails to ALL recivers from list but one time')
        print('#3  configure your proxy.')
        print("#4  sending message via protonmail?")
        print('remember to read README.md for more info')
        print('soon new futhers, multpile senders e-mails :O better loops. More configuration options ')
        print('#############################################################')
        chooice = input('chooice option: ')
        return chooice
# Path: core/cfg/credentials.py
