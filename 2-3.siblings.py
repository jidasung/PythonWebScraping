from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
# 객체는 자기 자신의 형제가 될 수 없다.