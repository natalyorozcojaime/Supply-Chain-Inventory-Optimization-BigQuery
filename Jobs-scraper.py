
import requests
from bs4 import BeautifulSoup

# 1.- Fetch the raw HTML content of the webpage
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)