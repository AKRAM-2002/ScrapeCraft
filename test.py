from bs4 import BeautifulSoup
import requests 
import re 

## get the data using url
url =  "https://editorial.rottentomatoes.com/guide/popular-movies/"
page = requests.get(url)

print(page.content)