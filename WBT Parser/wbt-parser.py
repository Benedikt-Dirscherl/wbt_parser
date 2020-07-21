import bs4
from bs4 import BeautifulSoup

html = open("wbt.html").read()
soup = BeautifulSoup(html)


print (soup.get_text())

my_url= "https://wbt.share.i40.de/b2a3240b390db1964aa245441ec2db16/#/id/5ebbbd8ea7ff6206a428b910"



