import mechanize
import sys

phrase = 'Chat'
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
print sys.argv
browser.form['email'] = sys.argv[1] +' '+ sys.argv[2]
browser.form['pass'] = sys.argv[3]
browser.submit()
r = browser.open('http://facebook.com')
html = r.read()
print(html[html.index(phrase):500])
