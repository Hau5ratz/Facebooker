import mechanize
import requests
import sys

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
browser.form['email'] = sys.argv[1]
browser.form['pass'] = sys.argv[2]
browser.submit()
texty = url + sys.argv[1].replace(' ','.').lower() + '?redif=8'
r = browser.open(texty)
html = r.read()
html = html[html.index(phrase):]
html = html[html.index('list:'):]
html = html[html.index('[')+2:]
html = html[:html.index(']')-1]
x = html.split('","')
x = [url+x[:-2] for x in x]
res = requests.get(x[0], allow_redirects=True)
print res.history

#print html.index(phrase)
