from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.indeed.co.in/jobs?q=python&l=Mohali%2C+Punjab'
html=urlopen(url)
