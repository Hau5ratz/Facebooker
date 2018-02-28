from __future__ import print_function
import mechanize
import pickle
import sys
import os
import getpass

if os.path.isfile('tastes'):
    with open('./tastes', 'rb') as file:
        tastes = pickle.load(file)
else:
    tastes = dict()
def resnames(l):
    tc, c, ret = len(l), 0, []
    for url in l:
        if not url in tastes.keys():
            tastes[url] = browser.open(url).geturl()[25:]
        ret += [tastes[url]]
        c +=1
        print('%s out of %s done'%(c, tc))
    return ret
    
phrase = 'InitialChatFriendsList'
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

burl = 'http://www.facebook.com/login.php'
url = 'https://www.facebook.com/'
browser.open(burl)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = input('Username: ')
browser.form['pass'] = getpass.getpass()
browser.submit()
texty = url + browser.form['email'].replace(' ','.').lower() + '?redif=8'
r = browser.open(texty)
html = r.read()
html = html[html.index(phrase):]
html = html[html.index('list:'):]
html = html[html.index('[')+2:]
html = html[:html.index(']')-1]
x = html.split('","')
x = [url+x[:-2] for x in x]
print(resnames(x))
with open('./tastes', 'wb') as file:
    pickle.dump(tastes, file)
#print html.index(phrase)
