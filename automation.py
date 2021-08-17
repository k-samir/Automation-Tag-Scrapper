from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyperclip

url = input("Enter your url: ")


# We use try-except incase the request was unsuccessful because of 
# wrong URL
try:
   page = urlopen(url)
except:
   print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div', {"class": "styles__box--2Ufmy styles__display-flex--2Ww2j styles__flexWrap-wrap--2Gdde"})

article = ''
div1 = content.findAll('div')
for i in div1:
    div2 = i.find_all('a')
    for j in div2:
        div3 = j.find_all('span')
        for k in div3:
            article = article + ',' +  k.text

fixed = article[1:]
print(fixed)
pyperclip.copy(fixed)

