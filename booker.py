import requests
import datetime
from bs4 import BeautifulSoup as bs
epoch = str(datetime.datetime.now())
session = requests.Session()
result = session.get(self.url % c, headers=headers)
soup = bs(result.content, 'lxml')
s =  
