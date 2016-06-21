# Special thanks to mat https://github.com/mat 
# and his work on besticon https://github.com/mat/besticon
# which allows me to solve this icon problem and yield better icons than
# Google s2 service.

from urllib.request import urlopen, Request
from socket import timeout
from urllib.error import *
from bs4 import BeautifulSoup
import MySQLdb

PRE_URL = "http://icons.better-idea.org/icons?url="

# Database Connection
host = "*"
user = "*"
password = "*"
db_name = "*"
db = MySQLdb.connect(host=host, user=user, passwd=password, db=db_name)
# intialise Cursor object
cursor = db.cursor()

# Query the news_icons Table
cursor.execute("*")
result = cursor.fetchall()
flag = 0
for item in result: # source, url, link
    source_name = item[0]
    url_queried = item[1]
    complete_url = PRE_URL + url_queried
    try:
        if source_name == "*" or flag: # continue point
            flag = 1  # unlock
            print("Working on " + source_name + "...")
            # access url
            req = Request(complete_url, headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req, timeout=20)
            content = url.read()
            soup = BeautifulSoup(content, "html.parser")
            first_icon = soup.find_all('td')[0].find('a').get("href")
            # print('''UPDATE news_icons SET link=\"%s\" WHERE source=\"%s\"''' % (first_icon,source_name))
            cursor.execute("*")
            db.commit()
    except HTTPError:
        print(source_name + " does not have an icon!")
        continue  # skip if no icons
    except timeout:
        print("Socket Time out!")
        continue
