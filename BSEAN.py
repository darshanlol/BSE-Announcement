import requests
from bs4 import BeautifulSoup
import requests
import tkMessageBox
page = requests.get("http://www.bseindia.com/corporates/ann.aspx?expandable=0")
soup = BeautifulSoup(page.content, "lxml")
name = soup.find(attrs={"a", "TTHeadergrey"}).get_text().strip()
desp = soup.find('td', attrs={"class", "TTRow_leftnotices"}).get_text().strip()
link = soup.select_one("a[href*=corpfiling]")['href'].strip()
print name
print desp
print link
tkMessageBox.showinfo(title="BSE Announcement", message=name)
