import sys
import os
from time import sleep
from gensen import *
import re


browser = init("pc")
geturl(browser,"http://www.reply.com/breed-reply/en/#/breed-reply/en/office-locations")
reobj = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)

while (1):
    sleep(2)
    found = False
    html = browser.page_source
    for mail in re.findall(reobj, html):
        print(mail)
        with open('mail.txt','r') as f :
            for line in f:
                if mail in line:
                    found = True
                    break
        if found == False :
            with open('mail.txt','a') as f :
                f.write(mail)
                f.write('\n')
