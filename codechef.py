from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
codes=[]
questions=[]
driver.get("https://www.codechef.com/problems/DEMTREE")
content =driver.page_source
soup=BeautifulSoup(content)
for a in soup.findAll('a',href=True,attrs={'class':'ember251'}):
	code=a.find('div', attrs={'class':'large-12 columns'})
	codes.append(code)
print(codes)