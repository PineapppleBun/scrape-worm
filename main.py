import requests, bs4, lxml

url = "https://parahumans.wordpress.com/table-of-contents/"
page = requests.get(url)
doc = bs4.BeautifulSoup(page.content, 'html')
print(doc)