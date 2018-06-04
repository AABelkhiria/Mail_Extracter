import sys
import os
from time import sleep
from gensen import *
import re

def check(mail):
    with open('mail.txt','r') as f :
        for line in f:
            if mail in line:
                found = True
                break

def fill():
    if found == False :
        with open('mail.txt','a') as f :
            f.write(mail)
            f.write('\n')

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
    
##    try:
##        html = browser.page_source
##        for a in browser.find_elements_by_xpath('//a'):
##            if len(a.get_attribute('innerHTML')):
##                if "@" in a.get_attribute('innerHTML') :
##                    txt = a.get_attribute('innerHTML')
##                    with open('mail.txt','a') as f :
##                        check()
##                        if found == False :
##                            f.write(txt)
##                            f.write('\n')
##    except:
##        browser.switch_to.frame(browser.find_element_by_xpath("//iframe"))
