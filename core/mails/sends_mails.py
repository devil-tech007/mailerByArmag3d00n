from asyncio import sleep, wait
from core.cfg.config import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import random
import os
import socks
import socket
class mailing:
    def __init__(self):
        cfg = config()
        self.cfg = cfg
        self.MY_PASSWORD = self.cfg.MY_PASSWORD
        self.MY_MAILHOST = self.cfg.MY_MAILHOST
        self.MY_MAILHOST_PORT = self.cfg.MY_MAILHOST_PORT
        self.MY_ADRESS = self.cfg.MY_ADRESS
        self.MSG_FILE_NAME ='mail_content.txt'
        self.PROXY_LIST = 'proxy_list.txt'
        self.RECIPIENTS_LIST = 'mails_list.txt'
    def sendLoopedMail(self,  proxy_status):
        if proxy_status == True:
            proxy_status = 1
        else:
            proxy_status = 0
        with open('core/mails/'+self.MSG_FILE_NAME, 'r') as file:
            try:
                message = file.read()
            except:
                print('error');
                sys.exit();
        with open('core/mails/'+self.RECIPIENTS_LIST, 'r') as file:
            recipients = file.readlines()
            try:
                for i in range(len(recipients)):
                    recipients[i] = recipients[i].replace('\n','')
            except:
                print('error');
                sys.exit();
        with open('core/proxy/'+self.PROXY_LIST, 'r') as file:
            try:
                proxy = file.readlines()
                for i in range(len(recipients)):
                    proxy[i] = proxy[i].replace('/n', '')
            except:
                print('error')
                sys.exit();
            while(True):
                for i in range(len(recipients)):
                    try:
                        randomint = random.randint(100,999)
                        string = str(randomint)
                        port_number = 1025
                        msg = MIMEMultipart()
                        msg['From'] = self.MY_ADRESS
                        msg['To'] = recipients[i]
                        msg['Subject'] = "My Test Mail - "+string
                        msg.attach(MIMEText(message))
                        if proxy_status == 1:
                            try:
                                proxy_host = proxy.split(':')[0]
                                proxy_port = proxy.split(':')[1]
                                proxy_user = ""
                                proxy_password = ""
                                socks.set_default_proxy(socks.SOCKS5,proxy_host, proxy_port, True, proxy_user, proxy_password) 
                                socket.socket = socks.socksocket
                                mailserver = smtplib.SMTP('', port_number)
                                mailserver.login(self.MY_ADRESS, self.MY_PASSWORD)
                                recipients[i] = recipients[i].replace(',','')
                                mailserver.sendmail(self.MY_ADRESS, recipients[i], msg.as_string())
                                mailserver.quit()
                                print('Mail sent - ',msg['Subject']," to: ",recipients[i], "used proxy: ",proxy_host[0],':',proxy_port[1])
                            except Exception as e: # 
                                print('Error: %s' % e)
                        else:
                            mailserver = smtplib.SMTP('', port_number)
                            mailserver.login(self.MY_ADRESS, self.MY_PASSWORD)
                            recipients[i] = recipients[i].replace(',','')
                            mailserver.sendmail(self.MY_ADRESS, recipients[i], msg.as_string())
                            mailserver.quit()
                            print('Mail sent - ',msg['Subject']," to: " ,recipients[i])
                    except:
                        print('proxy - error')
                        sys.exit();
                    if i > len(recipients):
                        i = 0
                        continue
                    else:
                        print('Mail sent to all recivers');
                        continue
    def sendMail(self):
        with open('core/mails/'+self.MSG_FILE_NAME, 'r') as file:
            try:
                message = file.read()
            except:
                print('error');
                sys.exit();
        with open('core/mails/'+self.RECIPIENTS_LIST, 'r') as file:
            recipients = file.readlines()
            try:
                for i in range(len(recipients)):
                    recipients[i] = recipients[i].replace('\n','')
            except:
                print('error');
                sys.exit();
        with open('core/proxy/'+self.PROXY_LIST, 'r') as file:
            try:
                proxy = file.readlines()
            except:
                print('error')
                sys.exit();
        for i in range(len(recipients)):
            try:
                randomint = random.randint(100,999)
                string = str(randomint)
                port_number = 1025
                msg = MIMEMultipart()
                msg['From'] = self.MY_ADRESS
                msg['To'] = recipients[i]
                msg['Subject'] = "My Test Mail - "+string
                msg.attach(MIMEText(message))
                mailserver = smtplib.SMTP('', port_number)
                mailserver.login(self.MY_ADRESS, self.MY_PASSWORD)
                recipients[i] = recipients[i].replace(',','')
                mailserver.sendmail(self.MY_ADRESS, recipients[i], msg.as_string())
                mailserver.quit()
                print('Mail sent - ',msg['Subject']," to: " ,recipients[i])
            except:
                print('error');
                sys.exit();
        print('done')
        sys.exit()
