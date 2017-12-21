import time
import schedule
import csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = "http://www.bloomberg.com/quote/SPX:IND"
page = urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')

name_box = soup.find('h1',attrs={'class':'name'})
name = name_box.text.strip()
print(name)

print(name_box)

price_box = soup.find('div',attrs={'class':'price'})
price = price_box.text
print(price)
def job():
    with open('index.csv','a') as c:
        writer = csv.writer(c)
        writer.writerow([name,price,datetime.now()])
schedule.every(1).minute.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)