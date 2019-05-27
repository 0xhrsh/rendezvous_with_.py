from pprint import pprint
import requests
import urllib.request
#import
from bs4 import BeautifulSoup     #try replaceing bs4 with BeautifulSoup
from selenium import webdriver
import pandas as pd 
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
codes=[]
questions=[]
#driver.get("https://www.codechef.com/problems/DEMTREE")
#content =driver.page_source
response = requests.get("https://www.codechef.com/problems/DEMTREE")
soup = BeautifulSoup(response.text, "html.parser")
#soup=BeautifulSoup(content)
#print(soup)
Text=soup.get_text()
n=len(Text.split('\n'))
print(n)
A=Text.split('\n')
pprint(A[290:n//2])
# for a in soup.findAll('div'):
# 	print(a,1)
	#code=a.find('div', attrs={'class':'large-12 columns'})
	#codes.append(a)
#print(codes)