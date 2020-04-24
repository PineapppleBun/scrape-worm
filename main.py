import requests, bs4, lxml

url = "https://parahumans.wordpress.com/table-of-contents/"
page = requests.get(url)
doc = bs4.BeautifulSoup(page.content, 'html')
divc = doc.find('div', attrs = {'class': 'entry-content'})

for link in divc.find_all('a'): 
    print(link.get('href')) 

